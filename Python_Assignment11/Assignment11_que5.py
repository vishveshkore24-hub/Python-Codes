#write a program which accepts one number and print reverse of that number
def ReverseNum(no):
    eneteredNum = no 
    reverseNum = 0
    for i in str(no):
        i = no % 10
        reverseNum = reverseNum * 10 + i
        no = no // 10
    if(reverseNum == eneteredNum):
        print("Given Number is palindrome")
    else:
        print("Given number is not palindrome")
    

def main():
    Num = int(input("Enter the Number : "))
    ReverseNum(Num)

if(__name__=="__main__"):
    main()