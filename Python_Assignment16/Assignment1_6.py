# print hello from fun on console.
def checkNum(num):
    if num > 0 :
        print("The" ,num,  "is Positive")
    elif num < 0:
        print("The" ,num,  "is Negative")
    else:
        print("The number is Zero")

def main():

    no = int (input("Enter Number : "))
    checkNum(no)
    
    
if(__name__ == "__main__"):
    main()