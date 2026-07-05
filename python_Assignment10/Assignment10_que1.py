def MultiplyOp(no):
    
    table = []

    for i in range(11):
        if( i != 0):
            ret = no * i
            table.append( ret)
    print("Multiplication table is : ", table)
    
    
def main():
    Number = int(input("Enterr the Number to print Multiplication table is : "))
    MultiplyOp(Number)

if(__name__ == "__main__"):
    main()