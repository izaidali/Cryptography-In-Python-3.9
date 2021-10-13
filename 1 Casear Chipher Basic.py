alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Input=input("Please Enter Your String\n")
Input_Len=len(Input)
Output_Shift=int(input("Pelase Enter The Shifting length\n"))
Output=''
for i in range(Input_Len):#ABC
    Char=Input[i]
    Loc_Char=alphabet.find(Char)
    New_Loc=Loc_Char+Output_Shift
    Output=Output+alphabet[New_Loc]
print("The Encrypted Text is",Output)