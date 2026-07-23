import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python program.py <SourceFile>")
        return
    
    existingFile = sys.argv[1]
    
    try:

        fobj = open(existingFile,"r")

        Data = fobj.read()

        print(Data)

        fobj2 = open("ABCD.txt","w")

        fobj2.write(Data)

    except FileNotFoundError as fobj2:
        print("There is no such file is present")

if(__name__=="__main__"):
    main()