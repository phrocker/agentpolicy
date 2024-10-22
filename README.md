# Agent Policy Framework

## Overview

The Agent Policy Framework is designed to create, manage, and execute agents that perform various tasks while enforcing compliance and security policies. This framework integrates with [Open Policy Agent (OPA)](https://www.openpolicyagent.org/) for policy decision-making and supports conditions such as PHI/PII detection and access control. The agents can be run on different platforms, including LangChain, OpenAI Swarm, and Crew AI.

## Project Structure

```
agent_policy_framework/
│
├── agents/                    # Directory for agent-related code
│   ├── __init__.py
│   ├── agent.py               # Agent class definition
│   └── task_agent.py          # Example implementation of an agent that handles tasks
│
├── policies/                  # Directory for policies
│   ├── __init__.py
│   ├── policy.py              # Policy class definition
│   ├── condition.py           # Condition class definition
│   └── action.py              # Action class definition
│
├── policy_engine/             # Core logic to apply policies
│   ├── __init__.py
│   └── policy_engine.py       # PolicyEngine class that enforces policies on agents
│
├── config/                    # Configuration files
│   └── config.yaml            # Configuration file that defines policies and agent settings
│
├── platforms/                 # Directory for platform-specific implementations
│   ├── __init__.py
│   ├── langchain_platform.py  # Implementation for running agents on LangChain
│   ├── openai_swarm_platform.py # Implementation for running agents on OpenAI Swarm
│   └── crew_ai_platform.py    # Implementation for running agents on Crew AI
│
├── opa/                       # Directory for OPA integration
│   ├── __init__.py
│   └── opa_client.py          # Client for interacting with OPA
│
├── main.py                    # Main entry point to run the framework
│
├── requirements.txt           # Dependencies for the project
│
├── utils/                     # Utility functions
│   ├── __init__.py
│   ├── logger.py              # Logging setup for the framework
│   └── plugin_loader.py       # Dynamic plugin loader utility
│
└── README.md                  # Project documentation
```

## Features

- **Agent Management**: Define and execute agents that perform tasks on various platforms.
- **Policy Enforcement**: Use OPA to evaluate and enforce policies on agents, ensuring compliance with data handling and access control standards.
- **Platform Support**: Integrate with different platforms, such as LangChain, OpenAI Swarm, and Crew AI, to run agents in diverse environments.
- **PHI/PII Detection**: Leverage [Presidio](https://microsoft.github.io/presidio/) for detecting sensitive information and integrate the results with OPA for decision-making.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [Open Policy Agent (OPA)](https://www.openpolicyagent.org/docs/latest/get-started/) running locally or accessible via an API endpoint

### Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/prhocker/agentpolicy.git
   cd agentpolicy
   ```

2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

### Configuration

Edit the `config/config.yaml` file to define your agents, policies, conditions, and actions. Here is an example configuration:

```yaml
agents:
  - id: "agent_001"
    type: "task_agent"
    task: "data_processing"
    platform: "langchain"
    metadata:
      access_level: 3

policies:
  - policy_id: "policy_001"
    conditions:
      - type: "phi_check"
        description: "Ensure no PHI/PII data is being handled"
    actions:
      - type: "log_task"
        description: "Log the task performed by the agent"
  - policy_id: "policy_002"
    conditions:
      - type: "access_control"
        description: "Ensure the agent has proper access control"
        required_access_level: 3
    actions:
      - type: "log_task"
        description: "Log the task performed by the agent"

pipeline:
  - "policy_001"
  - "policy_002"
```

### Running the Framework

Run the main script to execute the agents with their assigned policies:

```sh
python main.py
```

### Example Workflow

1. **Agent Creation**: Agents are created based on the configuration file. Each agent has a task, platform, and metadata.
2. **Policy Evaluation**: Policies are applied to each agent, and conditions are evaluated. For example, PHI detection is performed using Presidio, and access control is evaluated using OPA.
3. **Task Execution**: If the policies are successfully evaluated, the agent proceeds to execute its task on the specified platform.

## OPA Integration

The framework uses OPA to handle policy decision-making. An OPA client (`opa/opa_client.py`) is used to interact with OPA and evaluate whether an agent is allowed to proceed with a task based on its metadata and context.

To set up OPA, you can run it locally:

```sh
docker run -p 8181:8181 openpolicyagent/opa:latest run --server
```

Define your OPA policies in Rego to evaluate conditions such as access level and PHI detection.

## Dependencies

The project uses the following dependencies, specified in `requirements.txt`:

- **Presidio Analyzer**: For detecting PHI/PII in agent tasks.
- **Requests**: For interacting with the OPA API.
- **PyYAML**: For parsing configuration files.
- **Logging**: For structured logging throughout the framework.

## Extending the Framework

- **Add New Conditions**: Create new condition classes in `policies/condition.py` to add more compliance checks.
- **Add New Actions**: Define actions in `policies/action.py` to determine what happens after policy evaluation.
- **Add New Platforms**: Extend the platform implementations in `platforms/` to support additional platforms for running agents.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## Contact

For questions or support, contact [phrocker@apache.org].