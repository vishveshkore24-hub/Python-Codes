# Write a program that accepts a directory name from the user and counts the number of files inside it every five minutes
# Write the result into: DirectoryCountLog.txt
# Each Entry should contains: Directory Path, Number of files, Data and Time
import schedule
import time
import os

def DirectoryLog(DirectoryName):
        timestamp = time.ctime()
        FileCount = 0
     
        for folderName, subFolders, Files in os.walk(DirectoryName):
            FileCount += len(Files)
    
        print("Number of files are : ", FileCount)
    
        fobj = open("DirectoryCountLog.txt" , "a")
    
        fobj.write(f"Total Number files are {FileCount} in {DirectoryName} at {timestamp}\n")
    
        fobj.close()

def main():
    DirectoryName = input("Please Enter the directory Name : ")

    Ret = False
    Ret = os.path.isdir(DirectoryName)

    if ( Ret == False):
        print("Please enter the corect directory Name ")

    schedule.every(2).minutes.do(DirectoryLog, DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)
   
if(__name__=="__main__"):
    main()