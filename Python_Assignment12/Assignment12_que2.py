# write a program which accepts one number and print all factorials of that number
def Factorial(no):
    fact = []
    
    for i in range(no+1):
        if( i != 0 and no % i == 0):
            fact.append(i)
        
    print(f"Factorial numbers of {no} are {fact}")

def main():
    Number = int(input("Please enter the number : "))
    Factorial(Number)

if(__name__=="__main__"):
    main()