numbers = []
sum=0
for j in range(5):
    Number=int(input('Number: '))
    numbers.append(Number)
largest_number = max(numbers)
smallest_number = min(numbers)
length = len(numbers)
for number in numbers:
    sum=sum+number
average = sum/length
print('The first number is {}'.format(numbers[0]))
print('The last number is {}'.format(numbers[4]))
print('The smallest number is {}'.format(smallest_number))
print('The largest number is {}'.format(largest_number))
print('The average of the numbers is {}'.format(average))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_name = input('enter name: ')
if user_name in usernames:
    print('Access granted')
else:
    print('Access denied')