"""
print("hello world")

name = "Hardik"
print(name)


#PRINTING DIFFERENT TYPE OF DATATYPE
a = 10
b = 5.5
c = True

print(a)
print(b)
print(c)

#PRINT TYPE OF VARIABLE
print(a ,",Type = ",type(a))
print(b ,",Type = ",type(b))
print(c ,",Type = ",type(b))
print(name ,",Type = ",type(name))


# CHANGING STR TO INT
x = "100"
print(x ,",Type = ",type(x))
y = int(x)
print(y ,",Type = ",type(y))


"""

#Arthematic Operator in Pyhton:

"""
| Operator | Name                | Example   | Output |
| -------- | ------------------- | --------- | ------ |
| `+`      | Addition            | `10 + 5`  | `15`   |
| `-`      | Subtraction         | `10 - 5`  | `5`    |
| `*`      | Multiplication      | `10 * 5`  | `50`   |
| `/`      | Division            | `10 / 5`  | `2.0`  |
| `%`      | Modulus (Remainder) | `10 % 3`  | `1`    |
| `//`     | Floor Div(quotient) | `10 // 3` | `3`    |
| `**`     | Exponent (Power)    | `2 ** 3`  | `8`    |
"""



#CONTROL FLOW STATEMENT

#IF ELSE ELIF
"""
age = int(input("Enter your age = "))

if age>=18:
    print("You are eligible to drive")

else:
    print("You are not eligible")


#ODD EVEN CHECK
x = int(input("Enter number = "))

if x%2==0:
    print(x ,"is even")
else:
    print(x,"is odd")


#STRUCTURE
marks = int(input("Enter Marks = "))
if(marks>=90):
    print("Grade A")
elif(marks>=75 and marks<90):
    print("Grade B")
elif(marks>=50 and marks<75):
    print("Grade C")
else:
    print("Grade D")



#CHECK WHICH NO. IS BIGGER

x = int(input("Enter x = "))
y = int(input("Enter y = "))

if (x>y):
    print(x ,"is greater")
elif(x==y):
    print("BOTH are equal")
else:
    print(y,"is greater")
    


x = input("Enter Color = ").lower()

if(x=="green"):
    print("You can GO")
elif(x=="yellow"):
    print("Get ready")
else:
    print("STOP")
"""

"""
#LOPPING IN PYTHON

# FOR LOOP

for i in range(1,10):
    print(2*i)

# ODD NUMBER FROM 1 to 16
#METHOD 1
for i in range(1,16):
    if(i%2!=0):
        print(i)
#METHOD 2
for i in range(1,16,2):
    print(i)


#STAR PATTERN

x = "* "
for i in range(1,6):
    print(i*x)
  


#WHILE LOOP

i = 1
while(i<=5):
    print(i)
    i = i+1

# PRINTING TABLE

x = int(input("Enter num = "))
i = 1;
while(i<=10):
    print(x,"X",i,"=",x*i)
    i += 1
    
"""


"""
#FUNCTION IN PYTHON

#without argument
def greet():
    print("HELLO")

greet()

#with argument without return
def add(a,b):
    print(a+b)

add(10,20)

#with argument with return
def sum(a ,b):
    return (a+b)

sum(10,20)
print(sum(10,20))

"""


"""
#LAMBDA FUNCTION

add = lambda x,y:x+y
print(add(10,20))



#square of any num using lambda function

square = lambda x:x*x
print(square(10))
"""

#DATA STRUCTURE IN PYTHON
'''
| Data Structure | Ordered | Mutable | Allows Duplicates | How to Access       |
| -------------- | ------- | ------- | ----------------- | --------------------|
| **List**       | ✅ Yes   | ✅ Yes   | ✅ Yes          | Index (`list[i]`)  |
| **Tuple**      | ✅ Yes   | ❌ No    | ✅ Yes          | Index (`tuple[i]`) |
| **Set**        | ❌ No    | ✅ Yes   | ❌ No           | Loop only          |
| **Dictionary** | ✅ Yes*  | ✅ Yes   | ❌ Keys         | Key (`dict[key]`)  |

'''



#LIST
"""
Marks = [10,20,30,40]
print(Marks[2])         #access element
Marks.append(100)       #inserting at end
print(Marks)
Marks.insert(2,222)         #inserting at any pos
print(Marks)
Marks.remove(10)          #removing element by value
print(Marks)
Marks.pop()               # remove last element
print(Marks)
Marks.pop(1)              #remove element by index
print(Marks)
print(Marks.index(30))     #searching element by index
print(Marks.count(20))     #count the no. of

Marks1 = [10,20,30,40,25,34]
Marks1.sort()               #sort the list
print(Marks1)



Marks1.reverse()            #reverse the list
print(Marks1)
print(len(Marks1))         #length of list

print(sum(Marks))           #sum of list
print(max(Marks))           #max ele from list

avg = sum(Marks)/ len(Marks)
print(avg)


Marks.clear()               #to clear the list
print(Marks)
"""


"""
City = ["Mumbai" , "Delhi" , "Chennai" , "UK" , "Jammu"]

City[0] = "Kashmir"                         #TO CHANGE VALUE AT GIVEN INDEX 
print(City)

for i in City:                              #TO PRINT ALL USING FOR LOOP
    print(i)

print(City[2])                              # TO ACCESS SPECIFIC ELEMENT AT GIVEN INDEX

City.append("UP")                               # TO INSERT AR LAST POSITION
print(City)

City.insert(2,"Himachal")       # TO INSERT AT DESIRED POSITION
print(City)

City.pop()               # TO REMOVE LAST ELEMENT
print(City)

City.remove("Delhi")     # TO REMOVE BY VALUE
print(City)

City.reverse()          # TO REVERSE
print(City)

City.sort()             # TO SORT
print(City)

print(len(City))        # TO PRINT LENGTH

print(max(City))        #TO PRINT MAX

City.clear()            #TO CLEAR
print(City)



"""


#TUPLE
"""
tup = [10,20,30,40,50]

print(tup[-1])          #last ele

print(tup[0])           #first ele

print(tup[0:5:2])       #SLICING ------ start:end:step

print(len(tup))         #print length of tuple


t = [80,90,100,70,60]

t3 = tup+t                      # CONCATINATING TWO TUPLE
print(t3)

t3.sort()                       #sorting tuplw
print(t3)

t3.reverse()                    #reverse of tuplw
print(t3)

print(t3.count(10))             # frequecy of element

print(t3.index(50))             # index of element by val

print(min(t3))                  #min of tuple
print(max(t3))                  #max of tuplw

lst = list(t3)                  #COnvereting tuple to list
print(lst)

"""

"""
t = [ "sanjeeta" , "rohit", "rahul" , "anshika" , "ram"]

print(t)

for i in t:
    print(i)

print(t[0:5:2])

print(len(t))

print(max(t))
print(min(t))

t.sort()
print(t)

t.reverse()
print(t)

print(t.index("rahul"))

"""


#SET


s = {10,20,30,40,50,10}
print(len(s))
print(s)

for i in s:
    print(i)

s.add(100)              #TO ADD ELEMENT
print(s)

s.update([4,5,6])       #TO ADD MULTIPLE ELEMENT
print(s)

s.remove(40)            #TO REMOVE ELEMENT
print(s)

s.discard(2000)         #TO REMOVE ELEMENT WITHOUT ERROR IF ITS NOT PRESENT
print(s)

s.pop()                 # REMOVE RANDOM ELEMENT
print(s)

s1 = {1,2,3,5,4}
s2 = {2,3,5}

print(s1.union(s2))                 #all unique element in s1 and s2
print(s1 | s2)

print(s1.intersection(s2))          # element common in s1 and s2
print(s1 & s2)

print(s1.difference(s2))            #s1 - s2 the rest element is output
print(s1-s2)

print(s1^s2)                        #element in which are different in both

print(s2.issubset(s1))          #all element of s2 are present in s1

print(s1.issuperset(s2))        #element in s1 are in s2 ,s1 are more element beside s2 but those element are common







