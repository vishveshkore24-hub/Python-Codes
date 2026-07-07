# write a lambda function which accepts three numbers and returns largest from that numbers

def MaxNumber(no1,no2,no3):

    Maximum = lambda no1,no2,no3: no1 if (no1 >= no2 and no1 >= no3) else (no2 if  no2 >= no3 else no3)

    print("largest from three numbers is : ", Maximum(no1,no2,no3) )

def main():

    Number1 = int(input("Enter the 1st number : "))
    Number2 = int(input("Enter the 2nd number : "))
    Number3 = int(input("Enter the 3rd number : "))

    MaxNumber(Number1,Number2,Number3)

if(__name__=="__main__"):
    main()