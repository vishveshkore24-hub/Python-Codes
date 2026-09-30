import schedule
import time
import os

def FileSize(filePath):

    if os.path.isfile(filePath):

        fileSize = os.path.getsize(filePath)
        timestamp = time.ctime()

        with open("FileSizeLog.txt", "a") as fobj:
            fobj.write(f"File Path : {filePath}\n")
            fobj.write(f"File Size : {fileSize} bytes\n")
            fobj.write(f"Date and Time : {timestamp}\n")
            fobj.write("-" * 40 + "\n")

        print("File size logged successfully.")

    else:
        print("File does not exist.")

        with open("FileSizeLog.txt", "a") as fobj:
            fobj.write(f"File Path : {filePath}\n")
            fobj.write("Status : File does not exist\n")
            fobj.write(f"Date and Time : {time.ctime()}\n")
            fobj.write("-" * 40 + "\n")

def main():

    filePath = input("Enter file path: ")

    FileSize(filePath)

    schedule.every(30).seconds.do(FileSize, filePath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()