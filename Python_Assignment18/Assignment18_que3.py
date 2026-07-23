#write a program to accept N numbers from the user and store it into list and return the Minimum number from that list.
def minNumber():

    listSize = int(input("Enter the list size: "))

    NumList = []

    for i in range(listSize):
        value = int(input("Add number in list: "))
        NumList.append(value)

    print("NumList:", NumList)

    minimum = NumList[0]

    for i in range(1, listSize):
        if NumList[i] < minimum:
            minimum = NumList[i]

    print("minimum Number is:", minimum)

def main():

    minNumber()

if __name__ == "__main__":
    main()
