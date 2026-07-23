#write a program to accept N numbers from the user and store it into list and return the sum of the all elements of the that list.
def ListSum():

    listSize = int(input("Enter the list size: "))

    NumList = []

    for i in range(listSize):
        value = int(input("Add number in list: "))
        NumList.append(value)

    print("NumList:", NumList)

    total = sum(NumList)

    print("Addition of list numbers is:", total)


def main():

    ListSum()


if __name__ == "__main__":
    main()