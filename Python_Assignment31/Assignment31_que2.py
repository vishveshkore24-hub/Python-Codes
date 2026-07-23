# Create a Function named : DisplayMessage(message)
# Schedule the function using 
# schedule.every(5).seconds.do(DisplayMessage, message)
# The message should be accepted from user
import schedule
import time

def DisplayMessage(message):
    print(message)

def main():
    message = input("Enter Message: ")

    print(f'Your message "{message}" will be displayed every 5 seconds.')

    # Schedule the function
    schedule.every(5).seconds.do(DisplayMessage, message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()