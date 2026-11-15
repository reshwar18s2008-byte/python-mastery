class Student:
    college_name="ABC college"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print(Student.college_name)

    def welcome(self):
        print("welcome everyone",self.name)
    def get_marks(self):
        return self.marks
    
s1=Student("hare",8)
s1.welcome()
print(s1.get_marks())
print(s1.name)
