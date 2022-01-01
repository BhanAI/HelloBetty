import random

def GetNumber():
    number = [1, 2, 3, 4, 5, 6]
    random.shuffle(number)
    result =number[:1]
    return result[0]
openNumber = GetNumber()

x = input('big or small?')
print(x)

if openNumber > 3:
    if x == 'big':
        print('Congrats! You Won!')
    else:
        print('Sorry U lost! Let\'s play again!')
else:
    if x == 'big':
        print('Sorry U lost! Let\'s play again!')
    else:
        print('Congrats! You Won!')
print(openNumber)