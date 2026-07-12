# Design a python application that creates three threads named small, capital and Digits
# All threads should accepts a string as input 
# The samll thread should count and display the number os lowercase characters
# The Capital thread should count and display the number os UpperCase characters
# The Digit thread should count and dipslay the number of numeric digits
# Each thread must also Display: ThreadID and Thread Name
import threading
import time

def smallThread(strValue):
    lowerCharacter = 0
    for i in strValue:
        if (i.islower()):
            lowerCharacter = i
        print("Print lower case characters : ", lowerCharacter )

def capitalThread(strValue1):
    upperCharacter = 0
    for j in strValue1:
        if (j.isupper()):
            upperCharacter = j
        print("Print upper case characters : ", upperCharacter)

def digitThread(strValue2):
    digits = 0
    for k in strValue2:
        if (k.isdigit()):
            digits = k
        print("Print all digits : ", digits)

def main():
    
    start_time = time.perf_counter()
    value = input("Enter the input : ")

    t1 = threading.Thread(target=smallThread, args= (value,))
    t2 = threading.Thread(target=capitalThread, args= (value,))
    t3 = threading.Thread(target=digitThread, args= (value,))

    print(f"Print the name of thread {t1} is  {threading.current_thread().name}")
    print(f"Print the Id of thread {t1} is {threading.get_ident()}")
    print(f"Print the name of thread {t2} is  {threading.current_thread().name}")
    print(f"Print the Id of thread {t2} is {threading.get_ident()}")
    print(f"Print the name of thread {t3} is  {threading.current_thread().name}")
    print(f"Print the Id of thread {t3} is {threading.get_ident()}")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end_time = time.perf_counter()

    print(f"Required time is : {end_time - start_time:.4f}")
    
if(__name__=="__main__"):
    main()