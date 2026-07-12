#write a program which accepts one number and print below patteren input is 3
# 1 2 3
# 1 2 3
# 1 2 3
def DisplayPattern(no):

    for i in range(no):
        for j in range(1, no + 1):
            print(j, end=" ")
        print()


def main():

    value = int(input("Enter a number: "))
    DisplayPattern(value)


if __name__ == "__main__":
    main()