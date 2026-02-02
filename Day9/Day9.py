# Regex Pattern Practice :


"""

difference b/w r" " and re.findall
r" "   -------->>  tell python its regex pattern
re.finall ----->>  findall is a function inside regex
"""
import re

#write a regex to validate a 10 digit mobile
"""
text = "9877366380"
x = r"[0-9]{10}"
if re.match(x,text):
    print("Valid")
else:
    print("invalid")


if re.fullmatch(r"[6-9][0-9]{9}", text):
    print("Valid Indian mobile number")
else:
    print("Invalid mobile number")
"""





# write a string a = "contact me at test@gmail.com or admin@yahoo.in"

"""
a = "hardikpant@gmail.com"

if re.match(x,a):
    print("valid")
else:
    print("Invalid")

"""


# a = "Hardik@pant1"
# x = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
# if re.match(x,a):
#     print("valid pass")





#MOBILE NUMBER

# a = "6433499490"
# x = r"^[6-9]{1}[0-9]{9}$"
# if re.match(x,a):
#     print("valid")

#PAN CARD :

# x = "ABCDE1234A"
# y = r"^[A-Z]{5}[0-9]{4}[A-Z]$"
# if re.match(y,x):
#     print("valid")

#IPV4  -----------185.127.106.180
# 0-255
#
# x = "185.127.132.288"
#
# y = r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$"
# if re.match(y,x):
#     print("valid")
#
# # IPV6 ------------


#IPV6

x = "A123:78D9:995S:6GH7"

















