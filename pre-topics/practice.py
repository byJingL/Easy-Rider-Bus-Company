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

# ====================== Set Create ======================== #
empty_set = set()

flowers = {'rose', 'lilac', 'daisy'}
print(flowers) # {'daisy', 'rose', 'lilac'}

letters = set("hello")
print(letters) # {'e', 'h', 'l', 'o'}

states = ['Russia', 'USA', 'USA', 'Germany', 'Italy']
print(set(states)) # {'USA', 'Italy', 'Russia', 'Germany'}

set1 = {'A', 'B', 'C'}
set2 = {'B', 'C', 'A'}
print(set1 == set2)  # True

# ====================== Set work with ======================== #
nums = {1, 2, 2, 3}
nums.add(5)
print(nums)  # {1, 2, 3, 5}

more_nums = {6, 8}
nums.update(more_nums)
print(nums)  # {1, 2, 3, 5, 6, 8}
 
# add a list
text = ['how', 'are', 'you']
nums.update(text)
print(nums)  # {'you', 1, 2, 3, 5, 6, 7, 'are', 'how'}
 
# add a string
word = 'hello'
nums.add(word)
print(nums)  # {1, 2, 3, 'how', 5, 6, 7, 'hello', 'you', 'are'}

# ====================== Set Union ======================== #
A = {'Kennedy', 'Obama'}
B = {'Trump', 'Lincoln'}
presidents = A.union(B)
also_presidents = A | B
print(presidents, presidents == also_presidents)
# {'Lincoln', 'Obama', 'Trump', 'Kennedy'} True
A |= B
print(A)  # {'Lincoln', 'Obama', 'Trump', 'Kennedy'}

# ====================== Set Intersection ======================== #
creatures = {'human', 'rabbit', 'cat'}
pets = {'dog', 'cat'}
both = creatures.intersection(pets)
also_both = creatures & pets
print(both, both == also_both) # {'cat'} True

creatures &= pets # or creatures.intersection_update(pets)
print(creatures) # {'cat'}

# ================ Operation and Method ================= #
a = set('hello')
b = 'Hello'
both = a.intersection(b)
print(both)  # {'e', 'l', 'o'}
