import sys

def main():
    
    file1= sys.argv[1]
    file2 = sys.argv[2]

    fobj = open(file1,"r")

    Data1 = fobj.read()

    fobj = open(file2,"r")

    Data2 = fobj.read()

    if Data1 == Data2:
        print("Success")
    else:
        print("Failure")



if(__name__=="__main__"):
    main()