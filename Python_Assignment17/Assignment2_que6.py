#write a program which accepts one number and print below patteren input is 3
# * * *
# * *
# *
def DisplayPattern(no):

    for i in range(no, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()


def main():

    value = int(input("Enter a number: "))
    DisplayPattern(value)


if __name__ == "__main__":
    main()