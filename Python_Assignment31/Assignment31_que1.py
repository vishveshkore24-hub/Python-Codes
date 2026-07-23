# Write a program that accepts A message from the user. And A time interval in seconds
# Schedule the program to display the message repeatedly after the specified interval of time. 
# Example input:- Enter Message: Jay Ganesh , Enter interval in seconds: 5 
# Expected output: Jay Ganesh Every 5 seconds
# Validate the interval is greater than Zero

import schedule
import time

def Display(message):

    print(message)

def main():

    message = input("Enter a message : ")
    interval = int(input("Enter the interval in seconds : "))

    if interval <=0:
        print("Please enter the interval greater than zero")
        return

    print(f"{message} will be displayed at every {interval} seconds")

    schedule.every(interval).seconds.do(Display,message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if(__name__=="__main__"):
    main()