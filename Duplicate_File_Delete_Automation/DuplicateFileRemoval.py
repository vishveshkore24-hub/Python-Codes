#############################################################################
#
#   Importing Required Libraries
#
##############################################################################
import schedule
import datetime
import os
import time
import sys
import hashlib

from DuplicateFileRemovalModule import (
    findDuplicate,
    DeleteDuplicate,
    CreateLogFile,
    send_email
)

def Job():

    StartTime = datetime.datetime.now()

    DuplicateData = findDuplicate(DirectoryName)

    if DuplicateData is None:
        print("Invalid Directory")
        return

    DuplicateGroups = list(filter(lambda x: len(x) > 1, DuplicateData.values()))

    print("Duplicate Groups :", len(DuplicateGroups))

    DeletedFiles = DeleteDuplicate(DirectoryName)

    EndTime = datetime.datetime.now()

    CreateLogFile(
        DirectoryName,
        DeletedFiles,
        StartTime,
        EndTime
    )

    Subject = "Duplicate File Removal Automation Report"

    Body = f"""
Jay Ganesh,

Duplicate File Removal completed successfully.

Directory : {DirectoryName}

Duplicate Groups : {len(DuplicateGroups)}

Deleted Files : {DeletedFiles}

Start Time : {StartTime}

End Time : {EndTime}

Regards,
Vishvesh Kore
"""
    try:
        send_email(
        SenderEmail,
        AppPassword,
        ReceiverEmail,
        Subject,
        Body
    )
    except Exception as e:
        print("Email sending failed.")
        print("Reason :", e)

    print("Job Completed")
##############################################################################
#
#   Function name:  main
#   Input :         Command Line Arguments
#   Description:    It controls the script
#   Date:           24/07/2026
#   Author:         Vishvesh Pramod Kore
#
##############################################################################

def main():

    Border = "_" * 40
    print(Border)
    print("Duplicate File Removal Automation Script")
    print(Border)

    # Help option
    if (len(sys.argv) == 2 ):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation script is used to Remove Duplicate Files from the Directory.")
            print("This script:")
            print("1. Scans the directory.")
            print("2. Identifies duplicate files using checksum.")
            print("3. Deletes duplicate files.")
            print("4. Creates a log file.")
            print("5. Sends the log file through email.\n")
            print("For better usage please check --u or --U Flags:")
            print("python DuplicateFileRemoval.py <Directory Path> <Interval Minutes> <Receiver Email>")
            return

    # Usage option
        elif (sys.argv[1] =="--u" or sys.argv[1] == "--U"):
            print("Usage:")
            print("python DuplicateFileRemoval.py <Directory Path> <Interval Minutes> <Receiver Email>\n")
            print("Example:")
            print("python DuplicateFileRemoval.py D:Test 30 abc@gmail.com")
            return

    # Validate number of arguments
        elif len(sys.argv) != 4:
            print("ERROR: Invalid number of arguments.")
            print("Use --h for help or --u for usage.")
            sys.exit()

    # Validate directory
    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print("ERROR: Invalid directory path.")
        sys.exit()

    # Validate interval
    interval = int(sys.argv[2])
    try:
        

        if interval <= 0:
            print("ERROR: Interval must be greater than 0.")
            sys.exit()

    except ValueError:
        print("ERROR: Interval must be an integer.")
        sys.exit()

    # Validate email
    email = sys.argv[3]

    if "@" not in email or "." not in email:
        print("ERROR: Invalid email address.")
        sys.exit()

    print("\nCommand line validation successful!")
    print("Directory :", directory)
    print("Interval  :", interval, "minutes")
    print("Email     :", email)

# Global variables
    global DirectoryName
    global ReceiverEmail
    global SenderEmail
    global AppPassword

    DirectoryName = directory
    ReceiverEmail = email

    SenderEmail = "pythontestautomation5@gmail.com"
    AppPassword = "pprwsdddhiqjogdm"

    print("\nAutomation Started...")
    print("Waiting for scheduled execution...")

    schedule.every(interval).minutes.do(Job)

    while True:
        schedule.run_pending()
        time.sleep(1)

##############################################################################
#
# Starter of the Duplicate File Removal Automation Script
#
##############################################################################
if(__name__=="__main__"):
    main()