def divBy5(num):

    if(num % 5 == 0):
        print(True)
    else:
        print(False)


def main():
    no = int(input("Enter the Number : "))
    divBy5(no)

if(__name__== "__main__"):
    main()