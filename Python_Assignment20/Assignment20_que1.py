# Design a python application that creates two separate threads named Even and Odd.
# The Even thread should display the first 10 even numbers.
# The Odd threads should display first 10 odd Numbers.
# Both threads should execute independently using thc:\Marvellous_infosystems_Assignments\Assignment20_que1.pye threading module.
# Ensure proper thread creation and execution

import threading
import time

def EventhreadList(no):
    
    evenList = []

    for i in range(0,21,2):
            evenList.append(i)
    print(f"print even list is {no}: ", evenList)

def OddThreadList(no):
    oddList = []

    for i in range(1,21,2):
            oddList.append(i)
    print(f"print odd list is {no}: ", oddList)

def main():
    
    start_time = time.perf_counter()

    t1 = threading.Thread(target=EventhreadList, args= (100000,))
    t2 = threading.Thread(target=OddThreadList, args= (100000,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"Required time is : {end_time - start_time:.4f}")


if(__name__=="__main__"):
    main()