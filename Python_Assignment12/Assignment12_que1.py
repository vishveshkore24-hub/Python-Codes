#Write a program which accepts one character and check whether it is vowel or consonant
def checkVowel(ch):
    vowel  = ['a','e','i','o','u']
    ch = ch.lower()
    if(ch in vowel):
        print("given charatcter is vowel")
    elif(ch.isalpha()):
        print("Given char is consonants")
    else:
        print("Invalid input")

def main():
    char = input("Enter the character : ")
    checkVowel(char)

if(__name__=="__main__"):
    main()