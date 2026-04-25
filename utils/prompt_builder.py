def build_prompt(scenario, memory):
    prefs = {}
    if memory and isinstance(memory[-1], dict):
        prefs = memory[-1].get("metadata", {})

    task1 = (
        scenario.get("event1")
        or scenario.get("taskA")
        or scenario.get("activity_x")
    )
    task2 = (
        scenario.get("event2")
        or scenario.get("taskB")
        or scenario.get("activity_y")
    )
    priority = (
        scenario.get("priority")
        or scenario.get("importance")
        or scenario.get("focus")
    )
    message = (
        scenario.get("email")
        or scenario.get("message")
        or scenario.get("note")
    )

    return f"""
You are an executive personal assistant.
You are part of an autonomous multi-agent personal OS.

Resolve this scheduling conflict.

Task 1: {task1}
Task 2: {task2}
Priority: {priority}
Message: {message}
Persona: {scenario.get('persona', 'Balanced Professional')}
Policy version: {scenario.get('policy_version', 'v1')}
Predicted future conflict: {scenario.get('predicted_conflict', False)}
Memory hints: {prefs}

Return ONLY this format:

Decision -> one sentence
Reason -> one sentence
Delegation -> one sentence
Negotiation -> one sentence
Prediction -> one sentence
Email -> one polite email
"""