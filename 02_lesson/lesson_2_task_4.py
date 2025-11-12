def fizz_buzz(n):
    num = int(n)
    for num in range(1, n+1):

        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz', end=' ')
        elif num % 3 == 0:
            print('Fizz', end=' ')
        elif num % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(num, end=' ')


fizz_buzz(15)
