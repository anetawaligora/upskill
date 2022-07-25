# Episode2 Variables - Strings

message = 'Hello world'
print(message)

message_a = "Hello\' world"
print(message_a)

message_b = """Hello world
welcome to the jungle"""
print(message_b)

# Concatenation
greetings = 'Hello'
name = 'Aneta'
mail = greetings + ' ' + name
print(mail)

# function len
message_c = "How long is lenght my message"
print(message_c)
print(len(message_c))

print(len(message))
print(message[6:])

# Lower and upper case
print(message.lower())
print(message.upper())

print(message.find('ello'))

# dir - method and atributes avaiable for variable type
print(dir(message))

# Episode 3 Variables - Integers and Floats
num = 10.0
print(type(num))

# Arthimetric operators
addition = 3 + 2
substraction = 10 - 8
multiplications = 2 * 3
division = 9 / 4
floor_division = 9 // 4
exponent = 3 ** 2
modulus = 4 % 3

print(3 ** 2)
print(addition)
print(substraction)
print(multiplications)
print(division)
print(floor_division)
print(exponent)
print(modulus)

print(abs(-5))
print(round(4.26))
print(round(4.51))

# Equal
print(addition == exponent)

# Episode 4 - Lists, Tuples, Sets
# List = []
# Tuples = ()
# Dict = {}
# Lists (mutable)
courses = ['history', 'maths', 'geography']
print(courses)
print(len(courses))
print(courses[0])
print(courses[0:3])

# Adding item in the end of lists
courses.append('Biology')
print(courses)

# Adding item in choosen place of the lists
courses.insert(1, 'PE')
print(courses)

courses_2 = ['English', 'Polish']
# courses.insert(1, courses_2)
# print(courses)

# extend
courses.extend(courses_2)
print(courses)

# pop - remove item from list
courses.pop(2)
print(courses)

# sort
courses.sort()
print(courses)

num = [4, 6, 3, 0, 2]
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(min(num))
print(sum(num))

for item in courses:
    print(item)

for index, item in enumerate(courses):
    print(index, item)

course_str = '-'.join(courses)
print(course_str)

# Tuples - immutable
tuple_1 = ('apple', 'banana', 'pear', 'orange')
print(tuple_1)

# Sets
set = {'carrot', 'cucumber', 'tomato'}
print(set)

sciences = {'maths', 'physics'}
art = {'history', 'maths'}

print(sciences.intersection(art))

# Episode 5 - Dictionaries
student = {'name': 'Aneta', 'age': 28, 'courses': ['maths', 'geography', 'English']}
print(student)
print(student['courses'])
print(student.get('name'))

student.update({'name': 'Marcin'})
print(student)
del student['age']
print(student)

print(student.keys())

for key in student:
    print(key)

# Episode 6 Conditionals and Booleans - If, Else, and Elif Statements

# if False:
#   print('Conditionals are true')

language = 'python'
if language != 'python':
    print('Conditional is true')
elif language == 'Java':
    print('not true')
else:
    print('Not match')

user = 'Admin'
logged_in = True
if user or logged_in:
    print('Approved')
else:
    print('Bad cred')

# False
# none
# False
# zero of any numeric type
# Any  empty sequence eg. () [] ''
# Ane empty mapping eg {}


# The same values but two different objects
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

condition = ''
if condition:
    print("Confition is True")
else:
    print("Condition is False")

# Episode 7 Loops and iterations For/While loops

nums = [1, 2, 3, 4]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

for num in nums:
    for letter in 'abcd':
        print(num, letter)

for i in range(11):
    print(i)


# x = 0
# while x < 10:
#    if x == 5:
#        break
#    print(x)
#    #x += 1

# while True:
#    print(x)
#    x += 1

# Episode 8 Functions
def hello_func():
    print('hello')


def greetings():
    print("Greetings from Poland!")


def personal_greeting(name, wishes):
    print("Welcome" + '  ' + name + ". Nice to meet you " + wishes)


greetings()
personal_greeting("Aneta", "girl")


# def sum():
#    print("sum=")


#def items(summant_1, summant_2):
    #print("sum=" + ' ' + summant_1 + summant_2)


#items(3, 2)
