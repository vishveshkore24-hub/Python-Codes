# write a function using filter which accepts list of strings and returns list of strings having length grater than 5
def StringLength5():

    strList = ["Vishvesh", "Aishwarya", "Jay", "Ram", "Shri", "Rahul", "Nanda"]
    len5List =[]
    
    for i in strList:
        if i.__len__() >= 5:
            result = i
            len5List.append(result)
    print("List of strings having length 5 is : ", len5List)

def main():
    StringLength5()

if(__name__=="__main__"):
    main()