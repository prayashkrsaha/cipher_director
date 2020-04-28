                               #Python project: Codes and Ciphers Encryption and Decryption.
                                #Made by: Ankan Nath and Prayash Kumar Saha.
                                #College: Techno Main Salt Lake.
                                #Department: Electronics and Communication Engineering.

#importing nescessary module.
import string as st
import sys

#Function for decryption of substitution cipher.
def decryptsubstitution(str,n):
    dict={}
    
    l=[]
    
    for i in range(len(st.ascii_letters)):
        dict[st.ascii_letters[i-n]]=st.ascii_letters[i]
    
    for i in range(len(str)):
        if(str[i]==" " or str[i] in st.punctuation):
            l.append(str[i])
        else:
            l.append(dict[str[i]])
    
    print("Output : ","".join(l))
    
#Function for encryption of substitution cipher.
def encryptsubstitution(str,n):
    dict={}
    l=[]
    
    for i in range(len(st.ascii_letters)):
        dict[st.ascii_letters[i]]=st.ascii_letters[i-n]
    
    for i in range(len(str)):
        if(str[i]==" " or str[i] in st.punctuation):
            l.append(str[i])
        else:
            l.append(dict[str[i]])
    
    print("Output : ","".join(l))
    
#Function for encryption of Morse code.
def encryptMorse(str):
    dict={1:".----",2:"..---",3:"...--",4:"....-",5:".....",6:"-....",7:"--...",8:"---..",9:"----.",0:"-----",'A':".-",'B':"-...",'C':"-.-.",'D':"-..",'E':".",'F':"..-.",'G':"--.",'H':"....",'I':"..",'J':".---",'K':"-.-",'L':".-..",'M':"--",'N':"-.",'O':"---",'P':".--.",'Q':"--.-",'R':".-.",'S':"...",'T':"-",'U':"..-",'V':"...-",'W':".--",'X':"-..-",'Y':"-.--",'Z':"--..",'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
    l=[]
    
    for i in range(len(str)):
        if str[i]==" " or str[i] in st.punctuation:
            l.append(str[i])
        else:
            l.append(dict[str[i]])
            
    print("THE STRING IS ENCODED WITH A SINGLE SPACE BETWEEN EACH LETTER AND DOUBLE SPACE BETWEEN EVERY TWO WORDS:")
    print("Output : "," ".join(l))
    
#Function for decryption of Morse code.
def decryptMorse(str):
    dict={".----":1,"..---":2,"...--":3,"....-":4,".....":5,"-....":6,"--...":7,"---..":8,"----.":9,"-----":0,".-":'A',"-...":'B',"-.-.":'C',"-..":'D',".":'E',"..-.":'F',"--.":'G',"....":'H',"..":'I',".---":'J',"-.-":'K',".-..":'L',"--":'M',"-.":'N',"---":'O',".--.":'P',"--.-":'Q',".-.":'R',"...":'S',"-":'T',"..-":'U',"...-":'V',".--":'W',"-..-":'X',"-.--":'Y',"--..":'Z'}
    l=[]
    
    for i in range(len(str)):
        if(str[i]==''):
            l.append(" ")
        else:
            l.append(dict[str[i]])
            
    print("Output : ","".join(l))

#Function for encryption of Rail fence cipher.
def encryptRailFence(text, key): 
    rail = [['\n' for i in range(len(text))] 
                  for j in range(key)] 

    dir_down = False
    row, col = 0, 0
      
    for i in range(len(text)): 
        if (row == 0) or (row == key - 1): 
            dir_down = not dir_down 

        rail[row][col] = text[i] 
        col += 1

        if dir_down: 
            row += 1
        else: 
            row -= 1

    result = [] 
    for i in range(key): 
        for j in range(len(text)): 
            if rail[i][j] != '\n': 
                result.append(rail[i][j]) 
    
    print("Output : ","" . join(result)) 
      
#Function for decryption of Rail fence cipher.
def decryptRailFence(cipher, key): 
    rail = [['\n' for i in range(len(cipher))]  
                  for j in range(key)] 
      
    dir_down = None
    row, col = 0, 0
      
    for i in range(len(cipher)): 
        if row == 0: 
            dir_down = True
        if row == key - 1: 
            dir_down = False
          
        rail[row][col] = '*'
        col += 1
        
        if dir_down: 
            row += 1
        else: 
            row -= 1
              
    index = 0
    for i in range(key): 
        for j in range(len(cipher)): 
            if ((rail[i][j] == '*') and
               (index < len(cipher))): 
                rail[i][j] = cipher[index] 
                index += 1
          
    result = [] 
    row, col = 0, 0
    for i in range(len(cipher)): 
        if row == 0: 
            dir_down = True
        if row == key-1: 
            dir_down = False
              
        if (rail[row][col] != '*'): 
            result.append(rail[row][col]) 
            col += 1
              
        if dir_down: 
            row += 1
        else: 
            row -= 1
    
    print("Output : ","".join(result))
    
#Function for generation of key for the vignere cipher.    
def generateKey(string, key): 
    key = list(key) 
    
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) -len(key)): 
            key.append(key[i % len(key)]) 
    
    return("" . join(key))

#Function for encryption of vignere cipher.
def encrypt_text_vignere(string, key): 
    cipher_text = [] 
    
    for i in range(len(string)): 
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A') 
        cipher_text.append(chr(x)) 
    
    print("Output : ","" . join(cipher_text)) 
    
#Function for decryption of vignere cipher.
def decrpyt_text_vignere(cipher_text, key): 
    orig_text = [] 
    
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    
    print("Output : ","" . join(orig_text)) 

#Function defining the main menu of the program.
def menu():
    ch='y'
    while(ch=='y' or ch=='Y'):
        print("1.Substitution cipher")
        print("2.Morse code")
        print("3.Rail fence cipher")
        print("4.Vignere cipher")
        print("5.Exit")
        n=int(input("Enter your choice : "))
        
        if(n==1):
            
            print("1.Encrypt\n2.Decrypt")
            i=int(input("Your choice: "))
            
            str=input("Enter your string : ")
            j=int(input("Enter the key : "))
            print()
            
            if (i==1):
                encryptsubstitution(str,j)
                print()
            elif(i==2):
                decryptsubstitution(str,j)
                print()
            else:
                print("Wrong choice")
                break
        
        elif(n==2):
            
            print("1.Encrypt\n2.Decrypt")
            i=int(input("Your choice: "))
            
            print("Note:There must be a single space after each letter and a double space between every two words")
            str=input("Enter your string : ").split(" ")
            print()
            
            if (i==1):
                encryptMorse(str)
                print()
            elif(i==2):
                decryptMorse(str)
                print()
            else:
                print("Wrong choice")
                break
        
        elif(n==3):
            
            print("1.Encrypt\n2.Decrypt")
            i=int(input("Your choice: "))
            
            str=input("Enter the string : ")
            key=int(input("Enter the key : "))
            print()
            
            if (i==1):
                encryptRailFence(str,key)
                print()
            elif(i==2):
                decryptRailFence(str,key)
                print()
            else:
                print("Wrong choice")
                break
        
        elif(n==4):
            
            print("1.Encrypt\n2.Decrypt")
            i=int(input("Your choice: "))
            print("Note: The string must be continuous without any space and all capital letters.")
            str=input("Enter your string : ")
            key=input("Enter your keyword : ")
            print()
            
            if (i==1):
                encrypt_text_vignere(str,generateKey(str, key))
                print()
            elif(i==2):
                decrpyt_text_vignere(str, generateKey(str, key))
                print()
            else:
                print("Wrong choice")
                break
        
        elif(n==5):
            sys.exit("Exiting program")
        
        else:
            print("Wrong choice")
            sys.exit("Exiting program")
        
        print("Do you want to continue : ")
        ch=input("Enter your choice y/n : ")
        
#Main function of the program.       
if __name__ == "__main__": 
    menu()
    