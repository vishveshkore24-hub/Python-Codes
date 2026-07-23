def DigitCountFunc(no):
    count = 0
    
    for i in str(no): 
        count += 1
    return count
    

def main():
    Number = int(input("Enter Number is : "))
    print("count of digit is :",DigitCountFunc(Number))

if(__name__=="__main__"):
    main()