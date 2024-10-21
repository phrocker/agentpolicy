class Agent:
    def __init__(self, agent_id, task, platform):
        self.agent_id = agent_id
        self.task = task
        self.platform = platform
        self.policies = []

    def add_policy(self, policy):
        self.policies.append(policy)

    def execute_pipeline(self):
        for policy in self.policies:
            if not policy.evaluate(self):
                print(f"Agent {self.agent_id} failed at policy {policy.policy_id}.")
                return False
            policy.enforce(self)
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