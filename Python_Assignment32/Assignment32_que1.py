import schedule
import time
import datetime

def FileTimeStamp():

    timestamp = time.ctime()
    FileName = "File%s"%(timestamp)

    FileName = FileName.replace(" ","_")
    FileName = FileName.replace(":","_")

    fobj = open(FileName,"a")

    fobj.write(f"{FileName} is created on this {timestamp} date and time")

    fobj.close()
def main():

    schedule.every(1).minutes.do(FileTimeStamp)

    while True:
        schedule.run_pending()
        time.sleep(0.5)

if(__name__=="__main__"):
    main()