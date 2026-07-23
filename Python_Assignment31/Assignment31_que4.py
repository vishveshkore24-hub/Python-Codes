# write a program the reated a new log file after every 10 Minutes.
# The file name should contains date and time. Example: MarvellousLog_25_07_2026_16_30_00.txt
# Log file created successfully. Creation Time : 
import schedule
import time

def LogFile():

    timestamp = time.ctime()
    logFile = "MarvellousLog_%s.log"%(timestamp)

    logFile = logFile.replace(" ","_")
    logFile = logFile.replace(":","_")
    fobj = open(logFile,"a")

    fobj.write("Log File Create Successsfully at "+ timestamp)
    fobj.close()

def main():

    print("Automation Script started : ")

    schedule.every(2).minutes.do(LogFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if(__name__=="__main__"):
    main()