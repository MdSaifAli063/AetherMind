import gradio as gr
from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

def assistant(event1, event2, priority, email):
    prompt = f"""
You are a smart assistant.

Event1: {event1}
Event2: {event2}
Priority: {priority}
Email: {email}

Give:
1. Decision
2. Reason
3. Reply
"""

    result = generator(
        prompt,
        max_length=150,
        do_sample=True,
        temperature=0.7
    )[0]["generated_text"]

    return result.replace(prompt, "")

demo = gr.Interface(
    fn=assistant,
    inputs=[
        gr.Textbox(label="Event 1"),
        gr.Textbox(label="Event 2"),
        gr.Dropdown(["event1", "event2"], label="Priority"),
        gr.Textbox(label="Email")
    ],
    outputs="text",
    title="LifeOS AI Assistant",
    description="AI that resolves life conflicts intelligently"
)

if __name__ == "__main__":
    demo.launch()