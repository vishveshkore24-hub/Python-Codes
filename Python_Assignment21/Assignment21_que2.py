# Design a python application that creates two threads
# Thread 1 should calculate and display the maximum elemts from the list
# Thread 2 should calculate and display the Minimum elemts from the list
# The list should accept from the user.

# Design Python applicationt that creats two threads named prime and non prime
# Both threads shuld accept List of integers
# The Prime Thread should display all prime numbers from the list
# The non-Prime thread should display all Non Prime Numbers
import threading
import time
from functools import reduce

def MaxNumber(listSize):
    inputList = []

    for i in range(listSize):
        ListValues = int(input("Enter the List values :"))
        inputList.append(ListValues)
    print("Print User List : ", inputList)
    
    maxElement = reduce(lambda no1, no2  : no1 if no1 >= no2 else no2, inputList)

    print("Maximum number is : ", maxElement)

def MiniNumber(listSize):

    inputList = []

    for i in range(listSize):
        ListValues = int(input("Enter the List values :"))
        inputList.append(ListValues)
    print("Print User List : ", inputList)
    
    minElement = reduce(lambda no1, no2  : no1 if no1 <= no2 else no1, inputList)
    print("Minimum number is : ", minElement)


def main():

    start_time = time.perf_counter()
    
    print("Execution starts")
    no = int(input("Enter the input : "))
    t1 = threading.Thread(target=MaxNumber,args=(no,))
    t2 = threading.Thread(target=MiniNumber,args=(no,))

    t1.start()
    t1.join()
    
    t2.start()
    t2.join()

    end_time = time.perf_counter()

    print("Calculate the time : ", end_time-start_time)

if(__name__ == "__main__"):
    main()