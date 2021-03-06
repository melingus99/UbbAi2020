from PyQt5.QtCore import QRunnable, pyqtSlot


class Worker(QRunnable):

    def __init__(self, fn,fn2,option,*args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.option=option
        self.fn = fn
        self.fn2=fn2
        self.args = args
        self.kwargs = kwargs
        self.stopCondition=False

    @pyqtSlot()
    def run(self):
        if(self.option==1):
                result,matrix = self.fn(*self.args, **self.kwargs)
                self.fn2(result,matrix)
        else:
            for result,matrix,score,iteration in self.fn(*self.args, **self.kwargs):
                if(self.stopCondition==True):
                    break;
                self.fn2(result,matrix,score,iteration)

    def stop(self):
        self.stopCondition=True