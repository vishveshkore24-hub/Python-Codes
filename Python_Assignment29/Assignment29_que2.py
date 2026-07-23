import os 

def main():
    
    

    try:

        fileName = input("Enter the File Name : ")

        fobj = open(fileName,"w")

        Data = fobj.write("This is Python Scripts")

        print(Data)

        fobj= open(fileName,"r")
        printData = fobj.read()
        print(printData)
        fobj.close()
            

    except FileNotFoundError:
        print("There is no uch file is present")

        

if(__name__=="__main__"):
    main()