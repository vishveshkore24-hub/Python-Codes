#write a program to accept N numbers from the user and store it into list and accept one number from user and return frequency of that number.
def frequecyofNumber():

    listSize = int(input("Enter the list size: "))

    NumList = []

    for i in range(listSize):
        value = int(input("Add number in list: "))
        NumList.append(value)

    print("NumList:", NumList)

    searchNumber = int(input("Enter the search number : "))
    
    count = 0

    for i in range(listSize):
        if searchNumber == NumList[i]:
           count +=1
    print("frequency of Number is:", count)

def main():

    frequecyofNumber()

if __name__ == "__main__":
    main()
