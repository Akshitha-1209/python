class Vote:
    #constructor
    def __init__(self):
        print("age")
    def input(self):
        self.age=int(input("Enter the age"))
    def process(self):
        if self.age>18:
            print("Eligible")
        else:
            print("Not Eligible")
            print(18-age,"years")
#instantiate the object
obj=Vote()
obj.input()
obj.process()
obj1=Vote()
obj1.input()
obj1.process()

        
