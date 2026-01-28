#OOP'S(Object Oriented Programming) :

# blueprint to make obj ----------------------> class
# instance of class is  ----------------------> object

#eg:
"""
class Student:
    print("Hello")

s1 = Student()

print(s1)
"""

#Constructor : func which automatically call when object is created

# parameterised : which has values
# default : no value

# self = representing current object
# eg :
"""
class Student:
    print("hi")
    def __init__(self):
        print("this is constructor")

s1 = Student()
print(s1)
"""

# eg.
"""
class Student:
    def __init__(self):
        self.name= "rahul"
        print("This is constructor")

s1 = Student()
print(s1.name)
"""

#eg.
"""
class student:
    def __init__(self,name):
        self.name = name

s1 = student("hardik")
print(s1.name)
"""

# eg:
"""
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = student("Hardik " , 19)
print(s1.name , s1.age)

"""


# eg:
"""
class Car:
    model = "BMW"
    print(model)
    print("This is a Car")
    def __init__(self,model,type):
        print("Inside Constructor")
        self.model = model
        self.type = type

c1 = Car("Mercedes","Diesel")
print(c1.model , c1.type)
"""


#Attribute : data or variable
# 2 Type:|----------------> Class Attribute
#        |
#        |----------------> Object Attribute

"""
class Student:
    clg_name = "LPU"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

s1 = Student("Hardik" , 20)                 #  -----------|______________THESE ARE OBJECT ATTRIBUTES
s2 = Student("Rohit" , 21)                   # -----------|
print(s1.name)
print(s2.name)
print(s1.clg_name)
print(s2.clg_name)
print(Student.clg_name)                                    #can be called using class name

"""

"""
class Employee:
    company_name = "Google"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

e1 = Employee("Hardik",100000)
e2 = Employee("Rohit",200000)
print("name = ",e1.name ,",Salary = ", e1.salary)
print("name = ",e2.name ,",Salary = ", e2.salary)
print("Compant Name = ",Employee.company_name)
print(e1.company_name)
print(e2.company_name)
"""

"""
class Car:
    Showroom  = "Mercedes"
    def __init__(self,model,price):
        self.model = model
        self.price = price

c1 = Car("E class",200000000)
c2 = Car("Benz",150000000)
print("Car = ",c1.Showroom,c1.model , ",Price = ",c1.price)
print("Car = ",c2.Showroom,c2.model , ",Price = ",c2.price)
print("Shpwroom = ",Car.Showroom)
"""

"""
class College:
    cllg = "LPU"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

c1 = College("Hardik" , 20)
c2 = College("Rohit", 40)

print("Name: ",c1.name,", Marks: ",c1.marks)
print("Name: ",c2.name,", Marks: ",c2.marks)
print("COLLEGE NAME BEFORE : ",College.cllg)
College.cllg = "CU"
print("COLLEGE NAME AFTER : ",c1.cllg)
"""

"""
class Employee:
    company_name = "Google"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

e1 = Employee("Hardik",100000)
e2 = Employee("Rohit",200000)
print("name = ",e1.name ,",Salary = ", e1.salary)
print("name = ",e2.name ,",Salary = ", e2.salary)
print("Compant Name = ",Employee.company_name)
print("Old Salary = ",e1.salary)
print("Old Salary = ",e1.salary)
e1.salary=3000000
e2.salary=4000000
print("New Salary = ",e1.salary)
print("New Salary = ",e2.salary)
"""


# class student
# total student = class attribute: aand we have to increase this count wheneverr object is created
"""
class student:
    total_student = 0
    def __init__(self, name):
        self.name = name
        student.total_student +=1

s1 = student("Hardik")
s2 = student("Rohit")
s3 = student("Rahul")
print("Total Number of Students =",s1.total_student)

"""


# METHODS/FUNCTIONS = belong to specific object

# actions which gonna be performed inside class

"""
class Student:
    def __init__(self,name):
        self.name = name
    def hello(self):
        print("hello",self.name)

s1 = Student("Hardik")
print(s1.name)
s1.hello()
"""

# STATIC METHOD  =  belongs to the class, not to a specific object
"""
class Student:
    def __init__(self,name):
        self.name = name
    def hello(self):
        print("Hello",self.name)
    @staticmethod
    def college_name():                     # belongs to the class, not to a specific object
        print("How are u")

s1 = Student("Hardik")
s1.hello()
s1.college_name()
"""

# create a class student such that , name marks obj atttrite and normal methods (DISLPAY) which will display "hi , name , your marks = , marks "
"""
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def Display(self):
        print("Name =",self.name,", Marks =",self.marks)

s1 = Student("Hardik",34)
s1.Display()

"""




'''

immutable    |     mutable        |
-----------------------------------               tuple access =  index    
 Boolean     |      list []       |               list access  =  index
 int         |      set   {}      |               set access   =  loop
 float       |      dictionary {} |               Dict access =   key , value (loop)
 String      |                    |
 tuple ()    |                    |
_____________|________________    |
                
                
'''
#create a class student show name with class method , static method show cllg name

"""
class Student:
    def __init__(self,name,cllg):
        self.name = name
        self.cllg = cllg
    def full_name(self):
        print("Name =",self.name)
    @staticmethod
    def cllg_name(cllg):
        print("College name =",cllg)

s1 = Student("Hardik","LPU")
s1.full_name()
s1.cllg_name(s1.cllg)
"""


# 4 Pillars Of OOP's :
'''
1 > Encapsulation
2 > Abstraction
3 > Inheritance
4 > Polymorphism

'''

# 1 > Encapsulation = access control and data hiding
# eg general :
"""
class Student:
    def __init__(self,name):
        self.name = name
    def Display(self):
        print("Hello",self.name)

s1 = Student("Hardik")
s1.Display()
"""


# __ = used for making variable private
# private variable = which cannot be directly accesed outside class
#set_ = to update private variable
#get_ = to access private variable

# eg
"""
class Student:
    def __init__(self,marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,new_marks):
        self.__marks = new_marks
s1 = Student(91)
print(s1.get_marks())
s1.set_marks(84)
print(s1.get_marks())

"""

# eg>>create class bank balance where balance is hiddien acces it using get
"""
class Bank:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):             # Method used to access private data variable
        return self.__balance
    def set_balance(self,new_balance): # Method used to update private data variable
        self.__balance = new_balance
B1 = Bank(87000)
print(B1.get_balance())
B1.set_balance(100000)
print(B1.get_balance())
"""

#eg  BALANCE BANK ACCOUNT
"""
class Balance:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def withdraw(self,amount):
        if self.__balance < amount:
            print("Insufficient Balance")
        else:
            self.__balance-=amount
            print("Withdrwan =",amount)


x = Balance(10000)
print(x.get_balance())
x.withdraw(100)
print(x.get_balance())

"""



# 2 > Abstraction = data hiding and internal features are hidden (hiding proces)

# eg :
"""
class ATM:
    def withdraw(self):
        print("Money withdrawn")

    def check_balance(self):
        print("Balance shown")

atm = ATM()
atm.withdraw()
atm.check_balance()

"""
