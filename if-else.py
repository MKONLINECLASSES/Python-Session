'''
q3. Ask the user for a sentence and a starting and ending index, and then extract and print the substring within the specified range.'''

# str = 'Hi everyone good evening'
# startIndex = int(input('Enetr starting index'))
# endIndex = int(input('Enetr ending index'))

# print(str[startIndex : endIndex+1])

'''
q4. Ask the user for a sentence and two words. Write a program that finds the first occurrence of the first word in the sentence and replaces it with the second word, then displays the modified sentence
'''
# str = 'Hi everyone, how are you ?'
# word1 = input('Enter the first string ')
# word2 = input('Enter the second string ')
# print(str.replace(word1, word2))

# If else 

# age  = int(input('Enter your age : '))

# if age >=18:
#   print('Yes you are eligible for the movie')
# else :
#   print('No, you are not eligible')

# Grades 
'''
90-100 --> S
80-90 --> A
70-80 --> B
60-70 --> C
Others --> D'''
# marks = int(input('Enter your marks : '))
# # if marks >=90 and marks<=100:
# if 90<marks<=100:
#   print('S')
# elif 80<marks<=90:
#   print('A')
# elif 70<marks<=80:
#   print('B')
# elif 60<marks<=70:
#   print('C')
# else :
#   print('D')

# x = 30 
# y = 20
# if x == 10:
#   x = x+10
# elif y== 20:
#   y = y-10

# print(x+y)

# x = ''
# y = 'ranjan'
# print(bool(x))
# print(bool(y))
# if x and y:
#   result = 'Hello'
# else :
#   result ='World'

# print(result)

a = 10
b = 20

print(a==10)
if a==10 and b==30 :
  result = 'A'
elif a == 10 or b==30:
  result = "B"
else:
  result ='C'
print(result)
