# write lambda function using filter which accepts list of numbers and returns the count of even numbers
def countOfEven():

    Data = [20,33,40,50,75,8,9,4,6,98]

    evenlist= []

    result = list(filter(lambda i : i % 2 == 0 , Data))

    evenlist.append(result)

    count = 0
    for _ in result:
        count += 1
    
    print("Count of even numbers is : ",count)

def main():
    countOfEven()

if(__name__ == "__main__"):
    main()