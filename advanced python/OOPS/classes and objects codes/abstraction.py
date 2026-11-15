class Car:
    def __init__(self):
        self.acc=False      #this step is hidden
        self.brk=False       #this step is hidden
        self.clutch=False    #this step is hidden    

    def start(self):
        self.acc=True      #this step is hidden
        self.clutch=True     #this step is hidden
        print("car is started:")    
c1=Car()
c1.start()

#abstraction is nothing but hiding the
#  implementation details and showing only the functionality to the user.