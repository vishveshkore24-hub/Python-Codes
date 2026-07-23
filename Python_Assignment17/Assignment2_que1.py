# Write a program which accepts a number and displays the pattern

def startPattern(no):
    for i in range(no):
        print("* " * no)

def main():
    value = int(input("Enter the value: "))
    startPattern(value)

if __name__ == "__main__":
    main()