import schedule
import time

def Display():
    print("Coding Kar!")

def main():
    print("Automation Script started")
    schedule.every(30).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if(__name__=="__main__"):
    main()