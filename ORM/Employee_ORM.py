# ORM = Object Relational Mapping

# technique that uses python class and object to create database manually instead of sql queries
"""
database table = python class 
database rows = python objects
"""

from sqlalchemy.orm import declarative_base, Session  # creates base class
from sqlalchemy import Column, Integer, String, table  # inserting table
from sqlalchemy.orm import sessionmaker                 # create session to talk to database
from sqlalchemy import create_engine                    # connect with database

# STEP 1 : CREATING DB
engine = create_engine("sqlite:///company.db")            # file name

# STEP 2 :
Base = declarative_base()                                 # all class inherits from base class

# STEP 3 :
class Employee(Base):
    __tablename__ = "employee"                            #   __tablename__ is used to create table
    id=Column(Integer,primary_key=True)                   # for id column
    name = Column(String)                                 # for name column
    age = Column(Integer)                                 # for age column
    department = Column(String)                           # for department column

# STEP 4 :
Base.metadata.create_all(engine)                          # if the table will already be in database it will not recreate it

# STEP 5 : INSERT
Session = sessionmaker(bind = engine)                     # link session with engine
session = Session()                                       # object created for inserting ,deleting ,updating data
e1 = Employee(name = "hardik",age = 19,department = "HR")   # create 1st row
e2 = Employee(name = "Rohit",age = 23,department = "IT")    # create 2nd row
session.add(e1)                                             # add 1st row
session.add(e2)                                             # add 2nd row
session.commit()                                            # save the changes permanently

# STEP 6 : FETCH
employees=session.query(Employee).all()                     # fetching data
for i in employees:                                         # to print all the data in console
    print(i.id,i.name,i.age,i.department)


employees=session.query(Employee).filter_by(id =1).first()
employees.name = "Gian"
session.commit()
print("\nEmployee updated\n")
employees=session.query(Employee).all()
for i in employees:                                         # to print all the data in console
    print(i.id,i.name,i.age,i.department)

