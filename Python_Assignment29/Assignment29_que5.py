import sys
def occurences(fileName,word):

    try:

        fobj = open(fileName,"r")
        Data = fobj.read()
        count = Data.count(word)
        return count
    
    except FileNotFoundError as fobj:
        print("There is no such file is present")

def main():
    
    FileName = sys.argv[1]

    inputValue = input("Enter the word to search : ")

    Ret = occurences(FileName,inputValue)

    if Ret != None:
        print(f"In {FileName} the count of {inputValue} is : ", Ret)

if(__name__=="__main__"):
    main()