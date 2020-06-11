from lab10Fuzzy.repository import Repo
from lab10Fuzzy.Controller import Controller
from lab10Fuzzy.View import View
def main():
    repo=Repo('problem.in',"input.in")
    ctrl=Controller(repo)
    view=View(ctrl)
    view.menu()

main()
