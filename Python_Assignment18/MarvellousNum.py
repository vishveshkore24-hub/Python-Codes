def CheckPrime(no):

    if no <= 1:
        print(no, "is not a prime number.")
        return

    for i in range(2, no):
        if no % i == 0:
            return False

    return True