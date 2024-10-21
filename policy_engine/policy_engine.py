from policies.policy import Policy

class PolicyEngine:
    def __init__(self, policy_store):
        self.policy_store = policy_store

    def apply_policy(self, agent):
        policy = self.policy_store.get_policy_for_agent(agent)
        if policy and policy.evaluate(agent):
            policy.enforce(agent)
