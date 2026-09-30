def main():
    
    try:
        fobj = open("Demo.txt","r")

        countWords = fobj.read()
        words = countWords.split()
        count = 0
        
        for i in words:
            count +=1
        print("Total words in string are : ", count)

    except FileNotFoundError as fobj:
        print("No such file is present")

if(__name__=="__main__"):
    main()