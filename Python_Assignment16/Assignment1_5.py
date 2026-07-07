def numbers(no):
    for i in range(no, 0, -1):
        print(i,end=" ")

def main():
   num = int(input(" Enter the number : "))
   numbers(num)
    
    
if(__name__ == "__main__"):
    main()