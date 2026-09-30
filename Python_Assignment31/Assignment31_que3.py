# Write a program that scans specified directory every minute
# The task should display: Directory Name, Number of files, Number of subdiretories, Date and time of scanning
# Use the OS Module 
import os
import schedule
import datetime
import time

def Directory(directoryName):

    
    FilesCount = 0
    SubdirectoriesCount = 0
    
    for folderName,subFolders,fileName in os.walk(directoryName):

        SubdirectoriesCount += len(subFolders)

        for fname in fileName:
            path = os.path.join(folderName,fname)

            if( os.path.isfile(path)):
                FilesCount = FilesCount + 1

    print("Directory Name : ",directoryName)
    print("Number of files : ",FilesCount)
    print("Number of subdirectories : ", SubdirectoriesCount)
    print("Scanning Time :",datetime.datetime.now())

def main():

    directoryName = input("Enter the directory name : ")

    Ret = False
    Ret = os.path.isdir(directoryName)
    if ( Ret == False):
        print("Please enter the corect directory Name ")

    schedule.every(2).minutes.do(Directory,directoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if(__name__=="__main__"):
    main()