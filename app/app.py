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

What should you do?
"""

    result = generator(prompt, max_length=120)[0]["generated_text"]
    return result

demo = gr.Interface(
    fn=assistant,
    inputs=[
        gr.Textbox(label="Event 1"),
        gr.Textbox(label="Event 2"),
        gr.Dropdown(["event1", "event2"], label="Priority"),
        gr.Textbox(label="Email")
    ],
    outputs="text",
    title="LifeOS AI Assistant"
)

if __name__ == "__main__":
    demo.launch()