# write a function using filter which accepts list of strings and returns list of strings having length grater than 5
def StringLength5():

    strList = ["Vishvesh", "Aishwarya", "Jay", "Ram", "Shri", "Rahul", "Nanda"]
    
    result = list(filter(lambda i : i.__len__() >5 ,strList))
    
    print("List of strings having length 5 is : ", result)

def main():
    StringLength5()

if(__name__=="__main__"):
    main()