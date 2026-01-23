
#DICTIONARY
"""
student = {"Name":"Hardik","Age":19,"City":"Haldwani","Course":"BTECH"}

print(student['Name'])                  #TO ACCESS SPECIFIC VALUE IN DICT WITH ERROR IF NOT FOUND

dict2 = student.copy()                  #TO COPY THE DICT
print(student)

print(student.get("Course"))            #TO ACCESS SPECIFIC VALUE IN DICT WITHOUT ERROR

print(student.keys())                   #TO DISPLAY KEYS IN DICT

print(student.values())                 #TO DISPLAY VALUES IN DICT

print(student.items())                  #TO DISPLAY ALL ITEM PRESENT IN DICT

student.update({"Age":46 ,"Course":"Django"})           #TO MAKE CHANGES IN DICT
print(student)

student["age"]=21                   #TO UPDATE KEY VALUE IN DICT
print(student["age"])

student.pop("City")                 #DELETE SPECIFIC ITEM
print(student)

student.popitem()                   #TO DELETE LAST INSERTED ITEM
print(student)

print(len(student))                 #LENGTH OF DICT

dict2.update(student)               #TO MERGE DICT
print(dict2)

student.clear()                     #TO DELETE EVERYTHING IN DICT
print(student)

"""
from traceback import print_tb

# CONTACT BOOK MINI PROJECT:
"""
contact = {}

while True:
    print("\n-------CONTACT BOOK------------")
    print("1 ADD CONTACT")
    print("2 VIEW CONTACT")
    print("3 SEARCH CONTACT")
    print("4 DELETE CONTACT")
    print("5 EXIT")

    choice = input("Enter Your choice: ")

    if(choice=="1"):
        name = input("Enter Name: ")
        phone = input("Enter contact: ")
        contact[name] = phone
        print("Contact added successfully!! ")

    elif(choice=="2"):
        if contact:
            print("\nSAVED CONTACT: ")
            for name,phone in contact.items():
                print(name,":",phone)
        else:
            print("No contact found")

    elif(choice=="3"):
        name = input("Enter name to Search: ")
        if name in contact:
            print("Phone number:",contact[name])
        else:
            print("NO contact found")

    elif(choice=="4"):
        name = input("Enter the name you want to delete: ")
        if name in contact:
            del contact[name]
            print("Contact Deleted")
        else:
            print("Contact not found")

    elif(choice=="5"):
        print("THANK YOU FOR USING CONTACT BOOK")
        break

    else:
        print("INVALID CHOICE")


"""

# STUDENT SEARCH BOOK
"""
student={}

while True:
    print("\n--------- STUDENT BOOK---------------")
    print("1 ADD STUDENT")
    print("2 VIEW ALL STUDENT")
    print("3 SEARCH STUDENT")
    print("4 DELETE STUDENT")
    print("5 EXIT")

    choice = input("Enter Your Choice: ")

    if(choice=="1"):
        name = input("Enter name: ")
        roll = input(("Enter Roll Number: "))
        student[name] = roll
        print("Student Added Successfully")
    elif(choice=="2"):
        if student:
            print("ALL STUDENTS ")
            for name,roll in student.items():
                print(name,":",roll)
        else:
            print("No Student Found")
    elif(choice=="3"):
        name = input("Enter name to search : ")
        if name in student:
            print("Roll Num = ",student[name])
            print("Student found")
        else:
            print("No student found")
    elif(choice=="4"):
        name = input("Enter name to delete: ")
        if name in student:
            del student[name]
            print("Student deleted Successsfully")
        else:
            print("No Student Found")
    elif(choice=="5"):
        print("Thank for using student book")
        break
    else:
        print("Invalid Choice")


"""

# STRING
"""
s = " Python Programming"

print(len(s))           #Length of String

print(s[-1])            #last character
print(s[2:15:2])        #slicing start:end:step
print(s[:5])

print(s.upper())        #uppercase
print(s.lower())        #lowercase

print(s.strip())        #remove space from start and end

print(s.replace("Python","java"))       #replace old word with new

word = s.split()        #convert string to list
print(word)

a = "abc1"
print(a.isalpha())              #check if string is alphabet
print(a.isdigit())              #check if string is digit
print(a.isalnum())              #check if string is either num or alphabet

print(s.count("P"))             #Counts how many times character appear

print(s.startswith(" Pyth"))      #Check whether string starts with this or not
print(s.endswith("ing"))          #Check whether string end with this or not

"""

"""
name = "Hardik Pant"
print(name)

print(name[:8])

print(name[2:8:2])

print(len(name))

print(name.upper())

print(name.lower())

print(name.replace("Pant","Lord"))

x = name.split()
print(x)

print(name.isalpha())
print(name.isdigit())
print(name.isalnum())

print(name.count("a"))

print(name.startswith("har"))

print(name.endswith("nt"))

print(name[::-1])           #REVERSE OF STRING


'''TO COUNT VOWEL'''
count = 0
for i in name:
    if i in "a,e,i,o,u":
        count+=1
print(count)

'''PALINDROME OF STRING'''
#METHOD 1----->>> DOING REVERSE
a = "abcba"
b = a[::-1]
if a == b:
    print("Palindrome")
else:
    print("Npt palindrome")

#METHOD 2 ----->>> TWO POINTER
"""
a = "abcba"

for i in a:
    i
"""

'''FREQUENCY OF CHARACTER'''

a = "this is a boring day"

for i in a:
    count = 0
    count = a.count(i)
    print(i,":",count)

"""
"""
'''REPLACING VOWELS WITH *'''

a = "HeLLO HOW ARE YOU"
b = " "
for i in a:
    if i in "aeiou":
        a=a.replace(i,"*")

print(a)
"""
""""""

#FILE HANDLING IN PYTHON:

'''
                IN NEW FOLDER NAMED FILE HANDLING 
'''

#EXCEPTION HANDLING :
"""
try:
    #RISKY CODE
except:
    //REST OF CODE
"""

#eg :
"""
try:
    a = int(input("enter A = "))
    b = int(input("enter B = "))
    print(a/b)
except:
    print("error Occurred!!!!!!!!!!!!")

"""

"""
try:
    file = open("file.txt")
    print(file.read())
except FileNotFoundError:                   #CHECK IF FILE IS PRESENT OR NOT
    print("FILE NOT FOUND")
finally:                                    #EVERTIME THIS BLOCK RUNS
    print("Program runned")

"""