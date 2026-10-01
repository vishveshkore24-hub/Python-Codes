# write a lambda function using filter which accepts list of numbers and returns list of numbers which are divisible by 3 & 5
def divBy():

    Data = [ 12,20,18,30,45,75,5,3,105,120]

    result = list(filter(lambda i : i % 3 == 0 and i % 5 ==0, Data))

    print("Return the list which contains numbers divisible by 3 & 5 : ", result)

def main():
    
    divBy()

if(__name__ == "__main__"):
    main()