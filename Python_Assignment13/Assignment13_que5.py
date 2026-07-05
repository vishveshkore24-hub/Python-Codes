#write a program which accepts marks and display grade
def display_grade(marks):
    if marks < 0 or marks > 100:
        print("Invalid Marks")
    elif marks >= 75:
        print("Grade: Distinction")
    elif marks >= 65:
        print("Grade: First Class")
    elif marks >= 55:
        print("Grade: Second Class")
    else:
        print("Grade: Fail")


def main():
    marks = float(input("Enter marks: "))
    display_grade(marks)


if __name__ == "__main__":
    main()