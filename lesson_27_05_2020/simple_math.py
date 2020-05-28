x = int(input('Enter x: '))
y = int(input('Enter y: '))

res = x - y

print('difference: ', res)

res = x * y;

print('multiplication: ', res)

try:
    res = x / y
except:
    res = 'Cannot be devided by zero'

print('division: ', res)
