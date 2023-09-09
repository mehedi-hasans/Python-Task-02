# 5. Take a number from user and check the number is prime or not prime.
def isPrime(n):
    v = 0
    for i in range(2, n):
        if n%i==0:
            v = 1
    if v == 0:
        print('Prime')
    else:
        print('Not Prime')
userNumber = int(input('Enter your Number: '))
isPrime(userNumber)


