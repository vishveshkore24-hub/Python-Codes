import schedule

def LunchTime():

    print("Lunch Break Time")

def WrapUpWork():
    
    print("Wrap UP Work")

def main():
    
    print("Automation Script Started")

    schedule.every().day.at("13:00").do(LunchTime)

    schedule.every().day.at("17:00").do(WrapUpWork)

if(__name__=="__main__"):
    main()