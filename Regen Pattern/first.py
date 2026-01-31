import re

#1.dot (.)
"""
text="cat cot cut"
result=re.findall("c.t",text)
print(result)
"""

#2.start of a string(^)
"""
text="hello world"
print(bool(re.search("^hello",text)))
print(bool(re.search("^world",text)))
"""

#3.end of a string($)
"""
text="hello world"
print(bool(re.search("hello$",text)))
print(bool(re.search("world$",text)))
"""

#4.0 or more(*)
"""
text="helloooo"
reuslt=re.findall("lo*",text)
print(result)
"""

#5.one or more (+)
"""
text="helloooo" 
result=re.findall("lo+",text)
print(result)
"""

#6. 0 or one time (?)
"""
text="color colour"
result=re.findall("colou?r",text)
print(result)
"""

#7. characyer set([abc])
"""
text="apple ball cat"
result=re.findall("[abc]",text)
print(result)
"""

#8 digits([0-9])
"""
text="My name is 30"
result=re.findall("[0-9]",text)
print(result)
"""

#9. small ([a-z])
"""
text="My name is Sneha"
result=re.findall("[a-z]",text)
print(result)
"""

#10. capital ([A-Z])
"""
text="My name is SNEHA"
result=re.findall("[A-Z]",text)
print(result)
"""

#11.all letters ([A-Za-Z])
"""
text="My name is SNEHA"
result=re.findall("[A-Za-z]",text)
print(result)
"""

#12. digits (\d)
"""
text="Marks: 90"
result=re.findall("\d",text)
print(result)
"""

#13. non digits (\D)
"""
text="Marks: 90"
result=re.findall("\D",text)
print(result)
"""

#14. words (\w)
"""
text="Marks: 90"
result=re.findall("\w",text)
print(result)
"""

#15. digits (\d)
"""
text="Marks: 90"
result=re.findall("\W",text)
print(result)
"""

#16. space (\s)
"""
text="Marks: 90"
result=re.findall("\s",text)
print(result)
"""

#17.no space (\S)
"""
text="Marks: 90"
result=re.findall("\S",text)
print(result)
"""

#18. repetition count ({})
"""
text="phone: 8739391923"
result=re.findall("\d{10}",text)
print(result)
"""

#19. or operation
"""
text="i have a cat and a dog"
result=re.findall("cat|dog",text)
print(result)
"""

#20. grouping (())
"""
tsxt="abab ab"
result=re.findall("(ab)+",text)
print(result)
"""