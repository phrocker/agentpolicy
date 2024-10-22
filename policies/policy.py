class Policy:
    def __init__(self, policy_id, conditions, actions):
        self.policy_id = policy_id
        self.conditions = conditions
        self.actions = actions

    def evaluate(self, agent):
        total_score = 0.0
        for condition in self.conditions:
            condition_score = condition.check(agent)
            total_score += condition_score
        average_score = total_score / len(self.conditions) if self.conditions else 1.0
        return average_score

    def enforce(self, agent):
        for action in self.actions:
            action.perform(agent)