class Controller:
    def __init__(self,repo):
        self.repo=repo

    def setRules(self):
        self.repo.setRules()

    def setVariables(self):
        self.repo.setFuzzy()

    def setProblemParams(self):
        self.repo.setProblemParams()

    def setInput(self):
        self.repo.setInput()

    def compute(self):
        return self.repo.compute()

    def getInput(self):
        return self.repo.getInput()

    def getProblemParams(self):
        return self.repo.getProblemParams()
