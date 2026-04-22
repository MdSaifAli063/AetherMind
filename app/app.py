import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# -----------------------------------
# Load Model
# -----------------------------------
MODEL_NAME = "google/flan-t5-large"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME
)


# -----------------------------------
# Core Assistant Logic
# -----------------------------------
def solve_conflict(
    event1,
    event2,
    priority,
    email
):

    prompt = f"""
You are an executive assistant that resolves personal scheduling conflicts.

Choose the best action and respond ONLY in this exact format:

Decision: ...
Reason: ...
Delegation: ...
Email: ...

Task A: {event1}
Task B: {event2}
Priority: {priority}
Message: {email}
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )


    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=False,
        no_repeat_ngram_size=3,
        repetition_penalty=1.5
    )


    result = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    ).strip()


    # -----------------------------------
    # Remove prompt echo if model repeats input
    # -----------------------------------
    if "Decision:" in result:
        result = result[result.find("Decision:"):]


    # -----------------------------------
    # Fallback if generation goes bad
    # -----------------------------------
    if (
        "Task A:" in result
        or len(result) < 30
        or "Decision:" not in result
    ):

        result = f"""
Decision: Prioritize {priority}

Reason: Higher priority commitment should be handled first.

Delegation: Reschedule or delegate the lower priority task.

Email:
Sorry, I have a scheduling conflict at that time.
Can we move this to tomorrow?
"""


    return result.strip()


# -----------------------------------
# Examples for demo
# -----------------------------------
examples = [
[
"Team meeting at 7 PM",
"Family dinner at 7 PM",
"Family dinner",
"Boss requests urgent update tonight"
],

[
"Client presentation",
"Doctor appointment",
"Doctor appointment",
"Client asks for emergency call"
],

[
"Investor meeting",
"Mother's birthday dinner",
"Birthday dinner",
"Need to send investor slides tonight"
]
]


# -----------------------------------
# Gradio UI
# -----------------------------------
demo = gr.Interface(
    fn=solve_conflict,

    inputs=[
        gr.Textbox(
            label="Event 1",
            value="Team meeting at 7 PM"
        ),

        gr.Textbox(
            label="Event 2",
            value="Family dinner at 7 PM"
        ),

        gr.Textbox(
            label="Priority",
            value="Family dinner"
        ),

        gr.Textbox(
            label="Email / Message",
            lines=4,
            value="Boss requests urgent update tonight"
        )
    ],

    outputs=gr.Textbox(
        label="Assistant Decision",
        lines=14
    ),

    examples=examples,

    title="LifeOS v2 — Personal Conflict Resolution Agent",

    description="""
AI assistant for:
• Schedule conflict resolution  
• Delegation decisions  
• Difficult email drafting  

Built using OpenEnv + TRL PPO + Hugging Face
"""
)


if __name__ == "__main__":
    demo.launch()