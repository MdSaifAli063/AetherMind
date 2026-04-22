def reward_function(output, scenario):
    output = output.lower()

    reward = 0

    # reward rescheduling if conflict
    if "reschedule" in output:
        reward += 20

    # reward correct priority choice
    if scenario["priority"] == "event1" and "event1" in output:
        reward += 15
    elif scenario["priority"] == "event2" and "event2" in output:
        reward += 15

    # reward polite communication
    if "sorry" in output or "apologize" in output:
        reward += 5

    if reward == 0:
        reward = -10

    return reward