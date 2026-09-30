def main():
    
    File1 = input("Enter File Name : ")
    Word = input("Enter the Word : ")

    try:

        fobj = open(File1, "r")
 
        Data = fobj.read()

        splitDataa = Data.split()

        if Word in splitDataa:

            print("Word found")
        else:
            print("Word not found")


    except FileNotFoundError:
        print("There is no such file is present")

if(__name__=="__main__"):
    main()