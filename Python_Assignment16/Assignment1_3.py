# print hello from fun on console.
def Add(num,num2):
    ans = num + num2 
    print("Addition of 2 Numbers is : ", ans)

def main():

    no = int (input("Enter First Number : "))
    no2 = int (input("Enter Second Number : "))
    Add(no,no2)
    
    
if(__name__ == "__main__"):
    main()