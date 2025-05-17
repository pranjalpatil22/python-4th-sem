class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            raise ValueError("Salary must be positive")

class Company:
    company_name = "TechCorp"
    
    @classmethod
    def get_company_name(cls):
        return cls.company_name
    
    @staticmethod
    def company_info():
        return "TechCorp is a leading software company."

class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

if __name__ == "__main__":
    animals = [Dog(), Cat()]
    for animal in animals:
        print(animal.speak())
    
    person = Person("Alice", 30)
    print(person.get_name())
    person.set_name("Bob")
    print(person.get_name())
    
    emp = Employee(50000)
    print(emp.salary)
    emp.salary = 60000
    print(emp.salary)
    
    print(Company.get_company_name())
    print(Company.company_info())
    
    math_op = MathOperations()
    print(math_op.add(2, 3))
    print(math_op.add(2, 3, 4))
