def Addition(no1, no2):
    result = no1 + no2
    print("Addition is:", result)


def Substraction(no1, no2):
    result = no1 - no2
    print("Subtraction is:", result)


def Multiplication(no1, no2):
    result = no1 * no2
    print("Multiplication is:", result)


def Divison(no1, no2):

    if no2 == 0:
        print("Division by zero is not allowed.")
        return

    result = no1 / no2
    print("Division is:", result)