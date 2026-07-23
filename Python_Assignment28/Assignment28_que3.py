def main():
    
    try:
        fobj = open("Demo.txt","r")

        Data = fobj.read()

        print(Data, end="")

    except FileNotFoundError as fobj:
        print("Thereis no such file is present")

if(__name__=="__main__"):
    main()