class View:
    def __init__(self,ctrl):
        self.ctrl=ctrl

    def run(self):
        for str in self.ctrl.run():
            print(str)
