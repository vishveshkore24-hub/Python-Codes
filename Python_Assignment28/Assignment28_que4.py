def main():
    
    try:
        File1 = open("Demo.txt","r")

        File2 = open("Demo1.txt","w")

        Data = File1.read()

        Data2 = File2.write(Data)

        print(Data2)

        File1.close()
        File2.close()

    except FileNotFoundError:
        print("There is no such file present")


if(__name__=="__main__"):
    main()