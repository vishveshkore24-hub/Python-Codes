# write a program which accepts length and width of rectangle and prints area
def calculate_area(length, width):
    return length * width


def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = calculate_area(length, width)

    print("Area of Rectangle:", area)


if __name__ == "__main__":
    main()