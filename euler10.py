def primeOrNot(number):
    if number == 2:
        return True

    if number < 2:
        return False

    if number % 2 == 0:
        return False

    for i in range(3, (number**1/2)-1, 2):
        if number % i == 0:
            return False

    return True

primes = [i for i in range(2000000) if primeOrNot(i)]
print sum(primeOrNot)
