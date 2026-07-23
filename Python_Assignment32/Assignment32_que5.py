import schedule
import os
import time

def CleanupFunc(directory):

    logFile = open("DeleteLog.txt", "a")

    for files in os.listdir(directory):

        filePath = os.path.join(directory,files)

        if os.path.isdir(filePath):
            CleanupFunc(filePath)    # Recursive call
        else:
            try:
                if os.path.getsize(filePath) == 0:

                        os.remove(filePath)

                        print(f"Deleted : {filePath}")
                        logFile.write(f"Deleted : {filePath}\n")

            except Exception as e:
                        print(f"Unable to delete {filePath} : {e}")
                        logFile.write(f"Failed : {filePath} : {e}\n")

        logFile.close

def main():

    scannedDirectory = input("Enter the directory which required clean up : ")

    CleanupFunc(scannedDirectory)

    schedule.every().hour.do(CleanupFunc,scannedDirectory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if(__name__=="__main__"):
    main()