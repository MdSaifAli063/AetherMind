def build_prompt(scenario, memory):
    return f"""
You are an intelligent personal assistant.

Past Decisions:
{memory}

Current Scenario:
{scenario}

Tasks:
1. Resolve the conflict
2. Decide best action (event1/event2/reschedule)
3. Write a polite reply

Answer:
"""