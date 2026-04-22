def reward_function(output, scenario):
    output = output.lower()
    reward = 0

    # reschedule is best strategy
    if "reschedule" in output:
        reward += 20

    # correct priority
    if scenario["priority"] == "event1" and scenario["event1"].lower() in output:
        reward += 15
    elif scenario["priority"] == "event2" and scenario["event2"].lower() in output:
        reward += 15

    # politeness
    if any(word in output for word in ["sorry", "apologize", "thanks"]):
        reward += 5

    # penalty
    if reward == 0:
        reward = -10

    return reward