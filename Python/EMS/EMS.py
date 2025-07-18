from tabulate import tabulate
print("EMPLOYEE MANAGEMENT SYSTEMS")
class Main:
    def __init__(self):
        self.menu=[("0","EXIT"),("A","ADD"),("D","DELETE"),("E","EDIT"),("I","IMPORT"),("V","VIEW"),("X","XPORT")]
        self.chance=3
    def Menu(self):
        print(tabulate(self.menu,tablefmt="fancy_grid"))
    def Option(self):
        option=input("Please enter your option: ").upper()
        if option not in ["0","A","D","E","I","V","X"]:
            self.chance=self.chance-1
            print(f"Invalid Input, you have only {self.chance} Chance's")
            if self.chance==0: return "0"
            return self.Option()
        return option
    def End(self):
        print("THANK YOU, COME AGAIN!")
app=Main()
app.Menu()
chance=app.Option()
if chance=="0": app.End()
else: print("WORKING")
def Add():
    empid=input("Enter your Empid : ")
    name=input("Enter your Full Name : ")
    gender=input("Enter your Gender(M/F) : ")
    dob=input("Enter your Date Of Birth : ")
    salary=int(input("Enter your Salary : "))
