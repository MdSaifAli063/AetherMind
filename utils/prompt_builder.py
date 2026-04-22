def build_prompt(scenario, memory):
    return f"""
You are an executive personal assistant.

Resolve this scheduling conflict.

Task 1: {scenario.get('event1') or scenario.get('taskA')}
Task 2: {scenario.get('event2') or scenario.get('taskB')}
Priority: {scenario.get('priority') or scenario.get('importance')}
Message: {scenario.get('email') or scenario.get('message')}

Return ONLY this format:

Decision -> one sentence
Reason -> one sentence
Delegation -> one sentence
Email -> one polite email
"""