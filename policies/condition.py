
from opa.opa_client import OPAClient

class Condition:
    def __init__(self, description, check_func):
        self.description = description
        self.check_func = check_func

    def check(self, agent):
        # Return a confidence score between 0 and 1
        return self.check_func(agent)
    

class AccessControlCondition(Condition):
    def __init__(self, description, required_access_level):
        super().__init__(description, self.check_access)
        self.required_access_level = required_access_level
        self.opa_client = OPAClient(opa_url="http://localhost:8181")  # Example OPA URL

    def check_access(self, agent):
        # Check if agent has the required access level using OPA
        input_data = {
            "agent_id": agent.agent_id,
            "metadata": agent.metadata,
            "required_access_level": self.required_access_level
        }
        return 1.0 if self.opa_client.evaluate_policy(input_data) else 0.0