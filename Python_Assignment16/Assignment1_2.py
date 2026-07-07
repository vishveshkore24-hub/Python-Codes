# print hello from fun on console.
def ChkNum(num):
    if num % 2 == 0 : 
        print("Its Even Number")
    else:
        print("Its Odd Number")  

def main():

    no = int (input("Enter Number : "))
    ChkNum(no)
    
    
if(__name__ == "__main__"):
    main()