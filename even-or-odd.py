num = int(input('type a random number'))
result = num % 2
if result == 0:
    print('The number {} is even'.format(num))
else:
    print('The number {} is odd'.format(num))