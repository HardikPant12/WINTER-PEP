
# ABSTRACTION: show only the needed hide the rest
"""
define rules to write the code
show what to do
hides how to do it
Uses in a big problem

"""
from abc import abstractmethod
from multiprocessing.connection import address_type

# Abstract Class: method name is present but method body is absent
# > Child class completes the method

# eg 1:
"""
class Parent:
    def work(self):
        pass
class child(Parent):
    def work(self):
        print("I am working")
c1 = child()
c1.work()
"""

# eg 2:
"""
class Payment:
    def start(self):
        print("Payment Started")
    def pay(self,amount):
        pass
    def stop(self):
        print("Payment Completed")
class UPI(Payment):
    def pay(self,amount):
        print("Paid using UPI:",amount)
class Card(Payment):
    def pay(self,amount):
        print("Paid using Card:",amount)
class Cash(Payment):
    def pay(self,amount):
        print("Paid using Cash:",amount)

u1 = UPI()
u2 = Card()
u3 = Cash()
u1.start()
u1.pay(10000)
u1.stop()
u2.pay(3522)
u3.pay(8520)
"""

# eg 3.
"""
class Shape:
    def drawing_shape(self):
        print("Drawing Started")
    def choose(self):
        pass
    def completed(self):
        print("Drawing Completed")
class Square(Shape):
    def choose(self):
        print("The shape is Square")
class Circle(Shape):
    def choose(self):
        print("The shape is Circle")
class Rectangle(Shape):
    def choose(self):
        print("The shape is Rectangle")

s1 = Square()
s2 = Circle()
s3 = Rectangle()
s1.drawing_shape()
s1.choose()
s1.completed()
s2.choose()
s3.choose()

"""

# eg 4:
"""
class Parent:
    def work(self):
        print("I can work well ")
    def speak(self):
        pass
class Child(Parent):
    def speak(self):
        print("I can Speak")

c1 = Child()
c1.work()
c1.speak()
"""


#INTERFACE :
"""
abstraction passes rules+ready code+logic to child class  
whereas in interface passes only rules to child class .....interface is 100% strict

"""
# eg:
"""
class Parent:
    @abstractmethod
    def work(self):
        pass
    @abstractmethod
    def speak(self):
        pass
class Child(Parent):
    def work(self):
        print("I can work")
    def speak(self):
        print("I can Speak")

c1 = Child()
c1.work()
c1.speak()
"""

# eg 5:
"""
create a program where abstract class Course , it has two methods course_info and duration then you have to create a exam interface,it has a method examtype
in the last a class python course(course, exam interface),it has duration and exam type 
"""
"""
class Course:
    def course_info(self):
        print("The course is of Python")

    def duration(self):
        pass
class Exam:
    def exam_type(self):
        pass
class Python_Course(Course,Exam):
    def duration(self):
        print("The durarion is of 12 hr")
    def exam_type(self):
        print("The exam will be MCQ based")

s1 = Python_Course()
s1.course_info()
s1.duration()
s1.exam_type()
"""


# COMPOSITION
"""
> Don't reply on Inheritance
> Use Object of other class
> xhas a relationship = when we use a object of different class in a class this relationship is known as has a relationship
"""
# eg :
"""
class Address:
    def __init__(self,city):
        self.city = city
    def show_address(self):
        print("City =",self.city)

class Student:
    def __init__(self,name,city):
        self.name = name
        self.address = Address(city)
    def show_student(self):
        print("Name =",self.name)
        self.address.show_address()
s1 = Student("Hardik","Nainital")
s1.show_student()
"""
"""
create a class engine and then class car, car has a engine 

"""
"""
class Engine:
    def __init__(self, engine_type, horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower

    def show_engine(self):
        print("Engine Type =", self.engine_type)
        print("Horsepower =", self.horsepower)


class Car:
    def __init__(self, car_name, engine_type, horsepower):
        self.car_name = car_name
        self.engine = Engine(engine_type, horsepower)   # composition

    def show_car(self):
        print("Car Name =", self.car_name)
        self.engine.show_engine()

c1 = Car("Tesla Model 3", "Electric", 283)
c1.show_car()

"""


"""

is a  = 

"""
#Create a teacher and subject classes where teacher has a subject
"""
class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name

    def show_subject(self):
        print("Subject =", self.subject_name)


class Teacher:
    def __init__(self, teacher_name, subject_name):
        self.teacher_name = teacher_name
        self.subject = Subject(subject_name)   # composition

    def show_teacher(self):
        print("Teacher =", self.teacher_name)
        self.subject.show_subject()


# Object creation
t1 = Teacher("Mr. Sharma", "Mathematics")
t1.show_teacher()

"""


























