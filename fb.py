#Fizzbuzz

fizz_buzz="FizzBuzz"

for i in range(0, 31):
    if i % 3 == 0 and i % 5 ==0:
        print(fizz_buzz)

    elif i % 3 ==0:
        print(fizz_buzz[:4])

    elif i % 5 ==0:
        print(fizz_buzz[-4:])

    else:
        print(i)

