def SumOfNumbers():

    no = int(input("Enter the number is : "))
    sum = 0

    for i in range(1 , no + 1):
        sum += i
        
    print("Sum of the given number is : ", sum)

def main():

    SumOfNumbers()

if(__name__ == "__main__"):
    main()