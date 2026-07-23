import os

def FileCount():
    
    try:
        fobj = open("Demo.txt","r")

        #Data = fobj.read()
        CountLines = fobj.readlines()
        
        print("Total Lines present in file are : ",len(CountLines))

    except FileNotFoundError as fobj:
        print("No such file is present")

def main():
    FileCount()

if(__name__=="__main__"):
    main()