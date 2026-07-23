import schedule
import os
import time

def ReadFile(filePath):

    Ret = False

    Ret = os.path.isfile(filePath)
    if(Ret == False):
        print("There is no such file ")

    fobj = open(filePath,"r")

    try:
        Data = fobj.read()

        if(len(Data) == 0):
            print("File is empty")

        else:
            print("reads Files Content : ", Data)

        fobj.close()

    except PermissionError as fobj:
        print("Permission Denied")

    except OSError as fobj:
        print("File Cannot be opened")


def main():

    filePath = input("Enter the filePath : ")

    schedule.every(2).minutes.do(ReadFile,filePath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if(__name__=="__main__"):
    main()