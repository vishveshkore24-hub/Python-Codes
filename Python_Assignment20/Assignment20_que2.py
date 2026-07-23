# Design a python application that creates two separate threads named EvenFactor and OddFactor.
# Both thread should accepts one integer number as a prameter
# The EvenFactor thread should identify all even factors of the even number. Calculate and display the sum of all even factors
# The OddFactor thread should identify all odd factors of the even number. Calculate and display the sum of all odd factors
# Threads should run concurrently 

import threading
import time

def EvenFactorThreadList(no):

    evenFactorList = []
    sumofEven = 0
    

    for i in range(1,no + 1):
        if(no % i == 0 and i % 2 == 0):
            evenFactorList.append(i)
    print(f"print even list is {no}: ", evenFactorList)

    for j in evenFactorList:
        sumofEven = sumofEven + j
    print("Sum of even factors is : ", sumofEven)

def OddFactorThreadList(no1):
    oddFactorList = []
    sumofOdd = 0
    
    for i in range(1,no1 + 1):
        if(no1 % i == 0 and i % 2 != 0):
            oddFactorList.append(i)
    print(f"print odd list is {no1}: ", oddFactorList)
    
    for k in oddFactorList:
        sumofOdd = sumofOdd + k
    print("Sum of odd factors is : ", sumofOdd)

def main():
    
    start_time = time.perf_counter()
    
    value = int(input("Enter the input : "))
    t1 = threading.Thread(target=EvenFactorThreadList, args= (value,))
    t2 = threading.Thread(target=OddFactorThreadList, args= (value,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"Required time is : {end_time - start_time:.4f}")


if(__name__=="__main__"):
    main()