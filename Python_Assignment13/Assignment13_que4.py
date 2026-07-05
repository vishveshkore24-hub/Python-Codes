# write a program which accepts one number and print it's binary equivalent
def decimal_to_binary(no):
    if no == 0:
        return "0"

    binary = ""

    while no > 0:
        remainder = no % 2
        binary = str(remainder) + binary
        no = no // 2

    return binary


def main():
    num = int(input("Enter a number: "))
    print("Binary Equivalent:", decimal_to_binary(num))


if __name__ == "__main__":
    main()