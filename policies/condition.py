
class Condition:
    def __init__(self, description, check_func):
        self.description = description
        self.check_func = check_func

    def check(self, agent):
        return self.check_func(agent)
