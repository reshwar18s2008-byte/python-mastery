#PRIVATE ATTRIBUTES AND METHODS ARE MEANT TO BE
#USED ONLY WITHIN THE CLASS AND ARE NOT ACCESSIBLE
#FROM OUTSIDE THE CLASS. THEY ARE NOT INHERITED BY SUBCLASSES.


class Person:
    __name="reshwar"

    def __hello(self):
        print("hello",self.__name)
    def welcome(self):
        self.__hello()

p1=Person()
p1.welcome()