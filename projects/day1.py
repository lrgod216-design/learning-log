class Agent:
    def __init__(self, name, model):   # runs when you create one
        self.name = name               # attribute: data attached to THIS agent
        self.model = model
        self.history = []

    def add_message(self, msg):        # method: behavior for THIS agent
        self.history.append(msg)

researcher = Agent("researcher", "claude-sonnet")   # create an "instance"
writer = Agent("writer", "kimi")

researcher.add_message("find competitors")

class SmartAgent(Agent):        # SmartAgent 继承 Agent
    def add_message(self, msg): # 重写了这个方法
        print("智能版:", msg)
        self.history.append(msg)

smart = SmartAgent("nova", "kimi")

smart.add_message("hi")