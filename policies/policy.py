class Policy:
    def __init__(self, policy_id, conditions, actions):
        self.policy_id = policy_id
        self.conditions = conditions
        self.actions = actions

    def evaluate(self, agent):
        return all(condition.check(agent) for condition in self.conditions)

    def enforce(self, agent):
        for action in self.actions:
            action.perform(agent)
