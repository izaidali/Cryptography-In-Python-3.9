import string
def CaesarCipher(PlainText,Key):
    String=string.ascii_uppercase
    PlainText_Len=len(PlainText)
    Encryption=''
    for i in range(PlainText_Len):#ABC
        Character=PlainText[i]
        Location_of_Character=String.find(Character)
        New_Location=Location_of_Character+Key
        if New_Location>=26:
            New_Location=(Location_of_Character+Key)%26
        Encryption=Encryption+String[New_Location]
    print("Encrypted text is",Encryption)

def main():
    PlainText=input("Please Enter Your Text for Encryption\n")
    Key=int(input("Please Enter The Key\n"))
    CaesarCipher(PlainText,Key)
if __name__=="__main__":
    main()