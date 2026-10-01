# ****************************************************************************
#
# This Module Contains Duplicate File Removal Logic
#
# *****************************************************************************

# ****************************************************************************
# Import Required Libraries
# ****************************************************************************

import os
import sys
import time
import hashlib
import datetime
import smtplib
from email.message import EmailMessage

# ****************************************************************************
# Function Name : CalCulateCheckSum
# Description   : Calculates checksum of file using md5()
# Input         : File Path
# Date          : 25-07-2026
# Author        : Vishvesh Kore
# ***************************************************************************

def CalCulateCheckSum(FileName):
    fobj = open(FileName, "r+b")
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer)> 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()

# *************************************************************************************
# Functiona Name : findDuplicate
# Description    : This function scans all files from Directory and calculate checksum
# Data           : 25-07-2026
# Author         : Vishvesh Kore
# *************************************************************************************

def findDuplicate(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("Invalid Path")

    Ret = os.path.isdir(DirectoryName)

    if( Ret == False):
        print("It is not a directory")
        return

    Duplicate = {}                                                     #Dictionary
    unique = 0
    same = 0

    for folderName,subFolderName,fileName in os.walk(DirectoryName):

        for fname in fileName:
            fname = os.path.join(folderName,fname)

            CheckSum = CalCulateCheckSum(fname)

           # print(f"{fname} : {CheckSum}")

            if(CheckSum in Duplicate):
                same = same + 1
                Duplicate[CheckSum].append(fname)
            else:
                unique = unique + 1 
                Duplicate[CheckSum] = [fname]

    return Duplicate

# *************************************************************************************
# Function name     : DeleteDuplicate
# Description       : It will compare and remove the 1st duplicate file
# Date              : 25-07-2026
# Author            : Vishvesh Kore
# *************************************************************************************

def DeleteDuplicate(DirectoryName): 
    MyDict = findDuplicate(DirectoryName)

    #Result = MyDict.values()
    #return Result
    Count = 0
    TotalDeleted = 0
    Result = list(filter(lambda X : len(X) > 1, MyDict.values()))

    for value in Result:
        for subvlaue in value:
            Count = Count + 1
            if(Count > 1):
                os.remove(subvlaue)
                TotalDeleted = TotalDeleted + 1

        Count = 0
    print("Total Deleted Files : ", TotalDeleted)
    return TotalDeleted

# *****************************************************************************
# Function Name : Email Send Function
# Description   : This function will send an email with gerated log file and details
# Date          : 25-07-2026
# Author        : Vishvesh kore
# *****************************************************************************

def send_email(sender,App_Password,Receiver,subject,body):
    # Create Email Object
    msg = EmailMessage()

    # Setting Email Headers 
    msg["From"]= sender
    msg["To"] = Receiver
    msg["Subject"]= subject

    # Adding Email Body
    msg.set_content(body)

    #Create SMTP Connection manually 
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    # Login using gmail and password
    smtp.login(sender,App_Password)

    # Send email
    smtp.send_message(msg)

    # close connection manually 
    smtp.quit()


# *****************************************************************************
# Function Name : CreateLogFile
# Description   : It will contains all details of the Automation script
# Date          : 25-07-2026
# Author        : Vishvesh kore
# *****************************************************************************

def CreateLogFile(
        DirectoryName,
        DuplicateData,
        DeletedFiles,
        StartTime,
        EndTime):

    Border = "-" * 60

    try:

        if not os.path.exists("Logs"):

            os.mkdir("Logs")

        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

        logFileName = "DuplicateRemovalLog_%s.log" % timestamp

        LogFilePath = os.path.join(
            "Logs",
            logFileName
        )

        DuplicateGroups = list(
            filter(
                lambda X: len(X) > 1,
                DuplicateData.values()
            )
        )

        with open(LogFilePath, "w") as fobj:

            fobj.write(Border + "\n")
            fobj.write("Duplicate File Removal Report\n")
            fobj.write(Border + "\n")

            fobj.write(
                "Directory       : " +
                str(DirectoryName) +
                "\n"
            )

            fobj.write(
                "Start Time      : " +
                str(StartTime) +
                "\n"
            )

            fobj.write(
                "End Time        : " +
                str(EndTime) +
                "\n"
            )

            fobj.write(
                "Duplicate Groups: " +
                str(len(DuplicateGroups)) +
                "\n"
            )

            fobj.write(
                "Deleted Files   : " +
                str(DeletedFiles) +
                "\n"
            )

            fobj.write(Border + "\n")

            fobj.write("Duplicate Files:\n")

            fobj.write(Border + "\n")

            for checksum, files in DuplicateData.items():

                if len(files) > 1:

                    fobj.write(
                        "\nChecksum : " +
                        str(checksum) +
                        "\n"
                    )

                    for file in files:

                        fobj.write(
                            file +
                            "\n"
                        )

            fobj.write("\n")
            fobj.write(Border + "\n")
            fobj.write("End of Report\n")
            fobj.write(Border + "\n")

        print("Log file created :", LogFilePath)

        return LogFilePath

    except Exception as e:

        print("Error :", e)

        return None

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

    send_email(
        SenderEmail,
        AppPassword,
        ReceiverEmail,
        Subject,
        Body
    )

    print("Job Completed")            
               

               
          