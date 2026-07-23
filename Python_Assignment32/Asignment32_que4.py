import schedule
import os
import time
import shutil

def CopyFunc(srcPath,destPath):

    Ret = False
    Ret = os.path.isdir(srcPath)

    if(Ret == False):
        print("Source file directory is not found ")

    Ret = False
    Ret = os.path.isdir(destPath)

    if(Ret == False):
        print("Desitnation Directory is not correct")

    logFile = open("CopyLogFile.txt" , "a")

    for folderNames,subFolders,fileNames in os.walk(srcPath):
        for fname in fileNames:
            if fname.endswith(".txt"):

                srcFile = os.path.join(folderNames, fname)
                destFile = os.path.join(destPath, fname)

                try:
                    shutil.copy2(srcFile,destFile)
                    print(f"Copied : {srcFile}")
                    logFile.write(f"Copied from {srcFile} to destination folder { destFile}\n")

                except Exception as e:
                    print(f"Unable to copy {fname}")
                    logFile.write(f"Failed to copy {srcFile}\n")

    logFile.close()

def main():
    srcFilePath = input("Please enter the source file Path : ")
    destFilePath = input("Please enter the destination path : ")

    CopyFunc(srcFilePath, destFilePath)

    schedule.every(10).minutes.do(CopyFunc,srcFilePath,destFilePath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if(__name__=="__main__"):
    main()