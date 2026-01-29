#Inheritance: one class inherits another class features

# eg:
"""
class human:
    def eat(self):
        print("Human can eat")

class student(human):
    def study(self):
        print("students can study")

s1 = student()
s1.study()
s1.eat()
"""

# every animal can speak but dog can bark
"""
class Animal:
    def speak(self):
        print("Animal can speak")

class Dog(Animal):
    def bark(self):
        print("Dog can bark")

d1 = Dog()
d1.bark()
d1.speak()
"""

# phone can only call smartphone which can access both call and internet
"""
class Nokia:
    def __init__(self):
        print("I am parent")
    def call(self):
        print("Nokia can call")
class Iphone(Nokia):
    def __init__(self):
        super().__init__()                          #Using this we can access parent class constructor in child class
        print("I am child")
    def both(self):
        print("Iphone have both call and internet")

p1 = Iphone()
p1.both()
p1.call()
"""
#----------------------------------------------------------------------------------------------------------------------------#

# super().__init__() ----------------->>>> used to access parent constructor using child class

#Method Overriding: child class redefine parent class || child class always override properties of parent class method

# eg:
"""
class Parent:
    def work(self):
        print("Parent go to work")
class Child(Parent):
    def work(self):                                     # Child class overrides method of parent class
        print("child go to work")
c1 = Child()                            
c1.work()
p1 = Parent()
p1.work()
"""

#Multiple Inheritance: single class inherits multiple properties from multiple classes
"""
class Mother:
    def eyes(self):
        print("i have beautiful eyes")
class Father:
    def arms(self):
        print("I have strong arms") 
class Child(Mother,Father):                      # Here child class inherits both mother and father class properties
    def back(self):
        print("I have nice back")
c1 = Child()
c1.eyes()
c1.arms()
c1.back()
"""

#Method overriding with super
"""
class parent:
    def shape(self):
        print("Shape is circle")

class child(parent):
    def shape(self):
        super().shape()
        print("shape is square")
c1 = child()
c1.shape()
"""

# teacher prints teaches, coder prints coding student both teacher and coding
"""
class Teacher:
    def teaching(self):
        print("Teacher know teaching")
class Coder:
    def coding(self):
        print("Coder knows coding")
class Student(Teacher,Coder):
    def both(self):
        super().teaching()
        super().coding()

s1 = Student()
s1.both()
"""

# create a parent class with private varible and access in child class
#METHOD 1
"""
class parent:
    def __init__(self,toast):
        self.__toast = toast
    def get_cook(self):
        print("Parent can cook",self.__toast)

class child(parent):
    def cook(self):
        super().get_cook()

c1 = child("Bread")
c1.cook()
"""
#METHOD 2
"""
class Parent:
    def __init__(self):
        self.__x = 10
    def get_x(self):
        return self.__x
class Child(Parent):
    def show(self):
        print(self.get_x())
obj = Child()
obj.show()
"""

#-------------------------------------------------------------------------------------------------------------------------#

# TYPES OF VARIABLE :
"""

1 PUBLIC : Variable that can be accessed anywhere
eg: 
'''
class A:
    def __init__(self):
        self.x = 10

obj = A()
print(obj.x)   # Accessible

'''

2 PRIVATE : Variable that can be only accessed within class 
eg: 
'''
class A:
    def __init__(self):
        self.__x = 30

    def get_x(self):
        return self.__x

obj = A()
print(obj.get_x())   # Accessible via method

'''

3 PROTECTED : Variable that can be accessed within class or child class
eg:
'''
class Parent:
    def __init__(self):
        self._x = 100
class child(Parent):
    def show(self):
        print(self._x)
obj = child()
obj.show()
'''
"""

#eg
#create a parent class named "Person" in which name is private, constructor to set the name get_name() to return the name, then make class child,it will inherit person, then it has method show_name() it will be showing name using parent method
"""
class Person:
    def __init__(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
class Child(Person):
    def show_name(self):
        print("Your name is",self.get_name())

c1 = Child("Hardik")
c1.show_name()

"""

#eg
# create a parent class account then it sholud have protected variable _balance , then constructur shoudl set the balance then method show balance () should print balance, saving account is a child class of account and then create a method add money then you shoud take input as amount

"""
class Account:
    def __init__(self,balance):
        self._balance = balance
    def show_balance(self):
        print("Balance =",self._balance)
class Saving_Account(Account):
    def add_money(self,add):
        self._balance+=add

b1 = Saving_Account(100000)
b1.add_money(10000)
b1.add_money(2)
b1.add_money(20000000)
b1.show_balance()

"""

# DIAMOND PROBLEM

"""

                              A
                            // \\
                            B   C                                   Diamond Structure
                            \\ //
                              D

                here B & C inherits from A and then D inherits from B & C .....so it form a structure like 
                 diamond this is known as Diamond Problem .
                 
    WHY ITS NEEDED ?----->>>>*



"""


# crate a class A in which method printing a then B print b then C printing c and last d print d  c and b inherit a and d inherit b & c
#eg
"""
class A:
    def printf(self):
        print("A")
class B(A):
    def printf(self):
        print("B")
        super().printf()
class C(A):
    def printf(self):
        print("C")
        super().printf()
class D(B,C):
    def printf(self):
        print("D")
        super().printf()

d = D()
d.printf()
"""

#-------------------------------------------------------------------------------------------------------------------------#

# POLYMORPHISM : same name method but different work
'''
poly = many
morph = form

* same name diffrent behaviour
* depends on object
'''

#eg:
"""
class Dog:
    def speak(self):
        print("dog barks")

class Cat:
    def speak(self):
        print("meoww")

dog = Dog()
dog.speak()
cat = Cat()
cat.speak()

"""

#PRACTICE QUESTIONS :

# eg1:
"""
class Human:
    def speak(self):
        print("Human is talking")

class Baby:
    def speak(self):
        print("Baby is crying")

class Dog:
    def speak(self):
        print("Dog is barking")

h = Human()
b = Baby()
d = Dog()
h.speak()
b.speak()
d.speak()
"""

# eg2.
"""
class Car:
    def move(self):
        print("Car is moving")

class Truck:
    def move(self):
        print("Truck is moving")

class Bike:
    def move(self):
        print("Bike is moving")

c = Car()
t = Truck()
b = Bike()
c.move()
t.move()
b.move()
"""

# eg :
'''
crate a class person with a method role create 2 child of class student teacher printing method(i am student) and 
method(i am teacher) then create another class assitance that inherit from both student and tacher 
now u have to do first thing is create

'''
"""
class Person:
    def role(self):
        print("Hey i am a person")

class student(Person):
    def role(self):
        print("I am a student")
class teacher(Person):
    def role(self):
        print("I am a teacher")
class assistant(student,teacher):
    def role(self):
        pass  

a = assistant()
a.role()
"""



'''
a = [1,2,3]
b = a
b.append(4)
print(b)

'''

"""

                                                TOPICS COVERED 
inheritance
method ovverriding
multiple inheritance
super()
public , private ,protected
Diamond Problem
Polymorphism
Refrence
"""
