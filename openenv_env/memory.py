class Memory:
    def __init__(self):
        self.history = []

    def add(self, scenario, decision):
        self.history.append({
            "scenario": scenario,
            "decision": decision
        })

    def get_context(self, k=3):
        return self.history[-k:] if len(self.history) >= k else self.history