# write a program which accepts one number and checks whether it is perfect or not
def check_perfect(no):
    number = 0

    for i in range(1, no):
        if no % i == 0:
            number += i

    if number == no:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


def main():
    num = int(input("Enter a number: "))
    check_perfect(num)


if __name__ == "__main__":
    main()