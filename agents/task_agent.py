import yaml
from agents.task_agent import TaskAgent
from policies.policy import Policy
from policies.pipeline import PolicyPipeline
from utils.logger import setup_logger
from utils.plugin_loader import load_class

# Load configuration
with open("config/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

logger = setup_logger("AgentPolicyFramework")

# Create agents
agents = []
for agent_config in config["agents"]:
    agent = TaskAgent(agent_config["id"], agent_config["task"])
    agents.append(agent)

# Create policies and load conditions/actions dynamically
policies = {}
for policy_config in config["policies"]:
    conditions = []
    for cond in policy_config["conditions"]:
        condition_class = load_class(f"policies.condition", cond["type"])
        conditions.append(condition_class(cond["description"]))
    actions = []
    for action in policy_config["actions"]:
        action_class = load_class(f"policies.action", action["type"])
        actions.append(action_class(action["description"]))
    policy = Policy(policy_config["policy_id"], conditions, actions)
    policies[policy_config["policy_id"]] = policy

# Assign policies to agents in a pipeline
pipeline = PolicyPipeline()
for policy_id in config.get("pipeline", []):
    pipeline.add_policy(policies[policy_id])

for agent in agents:
    agent.add_policy(pipeline)

# Execute agents with pipeline
for agent in agents:
    agent.execute_pipeline()
