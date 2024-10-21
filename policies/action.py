class Action:
    def __init__(self, description, perform_func):
        self.description = description
        self.perform_func = perform_func

    def perform(self, agent):
        self.perform_func(agent)
