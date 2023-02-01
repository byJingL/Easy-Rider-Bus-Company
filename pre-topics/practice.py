import re

template = 'match'
result1 = re.match(template, "no match")
result2 = re.match(template, "match match")
print(result1)  # None
print(result2)  # <re.Match object; span=(0, 5), match='no match'>

template = r'.*good'
print(re.match(template, "very good").group())  # very good
print(re.match(template, "not good").group())  # not good

result = re.match('FLAG ME.', 'flag me\n', 
flags=re.IGNORECASE + re.DOTALL)  # match


string = "roads? where we're going we don't need roads."

result_1 = re.match(r'roads?', string)  # match
result_2 = re.match(r'roads.', string)  # no match 
print(result1, result2)

template = 'to be'
string = "To be, or not to be, that is the question"
print(re.match(template, string))
print(re.search(template, string))

import re 

pets = 'HamsTerCatPARROTdoG'
# your code here

pattern = r'dog|cat|parrot|hamster'

res = re.findall(pattern, pets, flags=re.IGNORECASE)
print(res)

# ====================== Group ======================== #
template = r"ha(\?!)?"  
print(re.match(template, "ha?!"))
print(re.match(template, "ha"))  
print(re.match(template, "ha?"))
print(re.match(template, "ha!"))
# <re.Match object; span=(0, 4), match='ha?!'>
# <re.Match object; span=(0, 2), match='ha'>
# <re.Match object; span=(0, 2), match='ha'>
# <re.Match object; span=(0, 2), match='ha'>

# ====================== Group emumerlation======================== #
template = r"(Python (\d) ){2,}"
print(re.match(template, "Python 2 Python 3 ").group(1))
print(re.match(template, "Python 2 Python 3 ").group(2))

template = r"((\w+) group) ((\w+) group)"
match = re.match(template, "first group second group group")

template = r"python|java|kotlin"
print(re.match(template, "python c++"))