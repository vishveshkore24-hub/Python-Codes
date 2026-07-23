import schedule
import time
import sys
import datetime

def Display():

    fileName = sys.argv[1]
    fobj = open(fileName,"a")

    fobj.write("Task is executed at : " +
                   datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +
                   "\n")

    fobj.close()

def main():
    
    print("Automation Script started")
    schedule.every(2).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if(__name__=="__main__"):
    main()