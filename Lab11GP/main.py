
from Lab11GP.Data import Data
from Lab11GP.Controller import Controller
from Lab11GP.View import View
def main():
    data=Data("training.in","input.in")
    ctrl=Controller(data,0.2,0.8,10)
    view=View(ctrl)
    view.run()

main()
