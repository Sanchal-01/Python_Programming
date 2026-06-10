from abc import ABC,abstractmethod #(abstract Base Class)

# Principal = ABC 
# Rules = abstractmethod

class Principal(ABC):

    @abstractmethod
    def wear_uniform(self):
        print("What is your name")  # This won't be printed as it is inside abstract class.
        pass

    @abstractmethod
    def do_homework(self):
        pass

# Student ko rules follow karne hi padenge:
class Student(Principal):

    def wear_uniform(self):
        print("Uniform pehen lo")

    def do_homework(self):
        print("Homework kar liya!!")


s = Student()
s.wear_uniform()
s.do_homework()