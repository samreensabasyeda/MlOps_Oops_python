# initiate the class
class employee:
    print("attributes are printing")
    def __init__(self):
        self.id = 123
        self.salary = 50000
    print("attributes are printed")

    # function inside the class
    def travel(self, destination):
        print("here in function or method attributes are called manually")
        print(f"Employee is traveling to {destination}")

# create object
sam = employee()

# call the method
sam.travel("kerala")

#print(type(sam))