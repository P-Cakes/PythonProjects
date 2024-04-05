
target = 100
for number in range(1, target+1):
    output = ''
    if number %3 == 0 and number%5 ==0:
        output = 'FizzBuzz'
    elif number%3 == 0:
        output = 'Fizz'
    elif number%5 == 0:
        output = 'Buzz'
    else:
        output = number
    print (output)
