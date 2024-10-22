class Agent:
    def __init__(self, agent_id, task, platform, metadata=None):
        self.agent_id = agent_id
        self.task = task
        self.platform = platform
        self.metadata = metadata if metadata else {}
        self.policies = []
        self.confidence_score = 0.0

    def add_policy(self, policy):
        self.policies.append(policy)

    def execute_pipeline(self):
        total_score = 0.0
        for policy in self.policies:
            policy_score = policy.evaluate(self)
            if policy_score == 0:
                print(f"Agent {self.agent_id} failed at policy {policy.policy_id}.")
                return False
            total_score += policy_score
            policy.enforce(self)
        self.confidence_score = total_score / len(self.policies)
        print(f"Agent {self.agent_id} achieved a confidence score of {self.confidence_score:.2f} for policy adherence.")
        return True

    def execute_on_platform(self):
        # Execute the agent's policy pipeline first
        if self.execute_pipeline():
            platform_module = self.load_platform_module()
            platform_module.run_agent(self)
        else:
            print(f"Agent {self.agent_id} failed to complete policy checks and cannot proceed on {self.platform} platform.")

    def load_platform_module(self):
        import importlib
        module_name = f"platforms.{self.platform}_platform"
        return importlib.import_module(module_name)