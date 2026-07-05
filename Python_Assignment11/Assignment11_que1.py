# Check whether it is prime or Not. 

def CheckPrime(no):

    if no <= 1:
        print(no, "is not a prime number.")
        return

    for i in range(2, no):
        if no % i == 0:
            print(no, "is not a prime number.")
            return

    print(no, "is a prime number.")


def main():
    Number = int(input("Enter the Number : "))
    CheckPrime(Number )


if __name__ == "__main__":
    main()