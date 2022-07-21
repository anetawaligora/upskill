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
