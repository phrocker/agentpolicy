class PolicyPipeline:
    def __init__(self):
        self.policies = []

    def add_policy(self, policy):
        self.policies.append(policy)

    def execute(self, agent):
        for policy in self.policies:
            if not policy.evaluate(agent):
                print(f"Pipeline interrupted at policy {policy.policy_id} for agent {agent.agent_id}.")
                return False
            policy.enforce(agent)
        return True