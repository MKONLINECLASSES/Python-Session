# # end and sep
# print('Shyam',end='-->')
# print('Ram', end='-->')
# print('geeta')

# # Shyam --> Ram --> geeta

# str1 = 'Apple'
# str2 = "Banana"
# str3= 'Orange'

# print(str1,str2,str3, sep='-->')
# # Shyam-->Ram-->geeta

name = input('Enter your name:') # Deepak
age = int(input('Enter your age :'))
place = input('Where do you live:')
# print(name, age)
# Using f-Strings

# message = f'Hello my name is {name} and i am {age} years old.'
# print(f'Hello my name is {name} and i am {age} years old.')
# print(message)
# print(f'Hello my name is {name}')

# .format() method

# message1 = 'Hello my name is {} and i am {} years old.'.format(name, age)

# message2 = 'Hello my name is {} and i am {} years old.'.format(age, name)

# message3 = 'Hello my name is {2} and i am {1} years old. I live in {0}'.format(name, age, place)

# print(message1)
# print(message2)
# print(message3)
# print('Hello my name is {2} and i am {1} years old. I live in {0}'.format(name, age, place))

# % methods
# %s --> String
# %d --> Integer
# %f --> Decimal
print('Name --> %s Age--> %d Place--> %s'%(name,age,place))
