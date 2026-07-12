#write a program which accepts one number and print below patteren input is 3
# 1
# 1 2
# 1 2 3
def DisplayPattern(no):

    for i in range(1, no+1,1):
        for j in range(i):
            print(j + 1, end=" ")
        print()

def main():

    value = int(input("Enter a number: "))
    DisplayPattern(value)


if __name__ == "__main__":
    main()