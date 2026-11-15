class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def sum_of_marks(self):
        x=sum(self.marks)
        return x
    def ave(self):
        return self.sum_of_marks()/3
s1=Student("hare",[80,90,100])
print("average of 3 is:",s1.ave())