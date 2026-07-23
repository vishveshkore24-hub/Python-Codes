#write a program to accept N numbers from the user and store it into list and return the maximum number from that list.
def MaxNumber():

    listSize = int(input("Enter the list size: "))

    NumList = []

    for i in range(listSize):
        value = int(input("Add number in list: "))
        NumList.append(value)

    print("NumList:", NumList)

    maximum = NumList[0]

    for i in range(1, listSize):
        if NumList[i] > maximum:
            maximum = NumList[i]

    print("Maximum Number is:", maximum)

def main():

    MaxNumber()

if __name__ == "__main__":
    main()
