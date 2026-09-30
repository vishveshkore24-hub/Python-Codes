# Write a python program that performs a file backup every hour
# The Program Should 
# Accept the source file path
# Accept the destination directory Path
# Copy the source file to the destination directory
# Add Current date and time to the backup File Name
# Write backup operation details into-: Example backup fileName:backup_log.txt, Example log Entry: Data_25_07_2026_16_30_00.txt
# BAckup successfully completed at 25-07-2026 04:30:00 PM Use the Shutil module for file Copying.

import shutil
import datetime
import time
import os
import schedule

def backupFile():

    sourceFile = input("Enter the source file path : ")

    Ret = False

    Ret = os.path.isfile(sourceFile)

    if(Ret == False):
        print("Source file does not exist")

    destinationDir = input("Enter the destination Directory")

    Ret = os.path.isdir(destinationDir)
    if(Ret == False):
        print("There is no such directory")

    filename = os.path.basename(sourceFile)
    name, ext = os.path.splitext(filename)

    # Current date and time
    timestamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    # New backup filename
    backup_name = f"{name}_{timestamp}{ext}"

    # Complete destination path
    dest_path = os.path.join(destinationDir, backup_name)

    # Copy file
    shutil.copy(sourceFile, dest_path)

    # Write log entry
    with open("backup_log.txt", "a") as log:
        log.write(f"{backup_name}\n")
        log.write("Backup successfully completed at "
                  + datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
                  + "\n\n")

    print("Backup completed successfully.")

def main():
    print("Automation Script Started")

   

    schedule.every(2).minutes.do(backupFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if(__name__=="__main__"):
    main()