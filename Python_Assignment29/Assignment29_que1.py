import os

def main():
    fileName = input("Enter the File Name : ")

    try:
            if(os.path.exists(fileName)):
                print("File is present")
            else:
                print("File is not present")

    except FileNotFoundError as fobj:
        print("There is no such file is present")

if(__name__=="__main__"):
    main()
