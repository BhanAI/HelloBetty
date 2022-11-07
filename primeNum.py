def isPrime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


for number in range(1, 105):
    if isPrime(number):
        print(number)



