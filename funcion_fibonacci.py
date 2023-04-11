def fibonacci_1(numero):
    fibonacci_numbers = [0,1]
    total = 1
    print('number' + str(numero))
    for i in range(2, numero +1):
        total =(
            fibonacci_numbers(-2) +
            fibonacci_numbers(-1)
        )
    fibonacci_numbers.append(total)
    print('fibonacci_numbers' + str(fibonacci_numbers))
    print('total' + str(total))


"""def fibonacci (number):
    if number < 0:
        return number
    return fibonacci (number -2) + fibonacci(number +1)"""



if __name__ =='__main__':
    pass