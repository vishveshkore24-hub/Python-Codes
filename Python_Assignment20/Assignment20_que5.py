# Design a python application that creates two threads named as Thread1 and Thread2
# Thread1 should display number from 1 to 50
# Thread2 should display number from 50 to 1
# Ensure that: Thread2 starts execution only after Thread1 has completed.
# Use appropriate Synchronzation
import threading
import time 
def Thread1():

    print("Thread1 : ", end="")

    for i in range(1,51):
        print( i, end="")
    print()

def Thread2():

    print("Thread2 : ", end="")

    for j in range(50,0,-1):
        print( j, end="")
    print()

def main():

    start_time = time.perf_counter()
    
    t1 = threading.Thread(target=Thread1, name="Thread1")
    t2 = threading.Thread(target=Thread2, name="Thread2")

    t1.start()
    t1.join()

    t2.start()
    t2.join()
    
    end_time = time.perf_counter()

    print("Calculae time to complete threads executions is : ",end_time - start_time)

if(__name__=="__main__"):
    main()