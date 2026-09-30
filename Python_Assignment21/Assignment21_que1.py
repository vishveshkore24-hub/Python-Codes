# Design Python applicationt that creats two threads named prime and non prime
# Both threads shuld accept List of integers
# The Prime Thread should display all prime numbers from the list
# The non-Prime thread should display all Non Prime Numbers
import threading
import time

def ChkPrime(num):

    if num <= 1:
        return False

    for i in range(2,num):
        if(num % i == 0):
            return False
        
    return True

def PrimeThread(listSize):
    inputList = []

    for i in range(listSize):
        ListValues = int(input("Enter the List values :"))
        inputList.append(ListValues)
    print("Print User List : ", inputList)
    
    primeList = []
    for i in inputList:
        if ChkPrime(i):
            primeList.append(i)
    print("Print Prime List is : ",primeList)

def NonPrimeThread(listSize):

    inputList = []

    for i in range(listSize):
        ListValues = int(input("Enter the List values :"))
        inputList.append(ListValues)
    print("Print User List : ", inputList)
    nonPrimeList = []

    for i in inputList:
        if not ChkPrime(i):
            nonPrimeList.append(i)

    print("Print Non Prime List is :", nonPrimeList)


def main():

    start_time = time.perf_counter()
    
    print("Execution starts")
    no = int(input("Enter the input : "))
    t1 = threading.Thread(target=PrimeThread,args=(no,))
    t2 = threading.Thread(target=NonPrimeThread,args=(no,))

    t1.start()
    t1.join()
    
    t2.start()
    t2.join()

    end_time = time.perf_counter()

    print("Calculate the time : ", end_time-start_time)

if(__name__ == "__main__"):
    main()