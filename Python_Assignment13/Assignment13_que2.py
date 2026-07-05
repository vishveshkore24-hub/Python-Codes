# write program which accepts radius of circle and prints area of circle.
import math

def circle_area(radius):
    return math.pi * radius * radius


def main():
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
    print("Area of Circle:", area)


if __name__ == "__main__":
    main()