print("#---------------------- Mathematical Operations -------------------#")

print("------------------- Addition --------------")

print("Enter the 1st Number : ")
No1 = int(input())

print("Enter the 2nd Number : ")
No2 = int(input())



print("select option 1 to do the Addition : ")


print("Please select Correct option")

print("\nSelect Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

ChoiceNumber = int(input())

def Addition():
    Ans  = No1 + No2
    if (ChoiceNumber == 1):
        print("The Sum of two numbers is : ", Ans)
    else:
        print("Please select correct option")

Addition()
print("Addition completed")

print("---------------------------------------")

print("select option 2 to do the Substraction : ")
ChoiceNumber = int(input())

print("You have selected option : ", ChoiceNumber)

def Substraction():
    SubstractionRes = No1-No2
    if (ChoiceNumber == 2):
        print("The substraction of two number is : ", SubstractionRes)
    else:
        print("Please select correct option")
Substraction()
print("Substraction Completed")

print("----------------------------------------")

print('select option 3 for Multiplication : ')
ChoiceNumber = int(input())

def Multiplication():
    Multi = No1 * No2
    if (ChoiceNumber == 3):
        print("Multiplication of two number is : ", Multi)
    else:
        print("Please select correct option")

Multiplication()
print(" Multiplication of two Numbers completed ")

print("--------------------------------------------")

print('select option 4 for division : ')
ChoiceNumber = int(input())

def Division():
    DivisionRes = No1/No2
    if (ChoiceNumber == 4):
        print("The division of two number is : ", DivisionRes)
    else:
        print("Please select correct option")

Division()
print(" Divison of two Numbers completed ")