import schedule
import time
import datetime

def Display():
    print("Current data and time are : ",datetime.datetime.now())

def main():
    print("Automation Script started")
    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if(__name__=="__main__"):
    main()