import re
import random
import string
import maskpass
import os
import hashlib

emailtest = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

#retourne le length du fichier
def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    f.closed    
    return i + 1

#check if fichier is empty
def file_is_empty(path):
    return os.stat(path).st_size==0


# the existance of email in the file
def existemail(x , email1) :
    i = 0
    for line in x :               
            if (i != 0):            
                    testupdate = re.split('([a-zA-Z0-9]+[.-_]*[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[A-Z|a-z]{2,}))',line)
                    if (email1 == testupdate[1]):
                        return testupdate
            i+=1        
    return 0        

# the existance of password in the file
def existpass(x , pass1) :
    i = 0
    print(pass1)
    for line in x :               
            if (i != 0):            
                    testupdate = re.split('([a-zA-Z0-9]+[.-_]*[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[A-Z|a-z]{2,}))',line)
                    print(testupdate[3])
                    if (pass1 == testupdate[3]):
                        return testupdate
            i+=1        
    return 0   

def isValid(email):
    if re.fullmatch(emailtest, email):
      return True
    else:
      return False

def isValidpass(pwd):
    lowercount=0
    majuscount=0
    numbercounter=0
    symbolcounter=0
    if (len(pwd)>=8):
        for c in pwd :
            if (c.islower()):
                lowercount+=1
            if (c.isupper()):
                majuscount+=1
            if (c.isdigit()):
                numbercounter+=1        
            if re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\]', pwd):
                symbolcounter+=1 
    else :
        print("entrer un password de longuer 8 au minimum") 
        return 0           
    if(lowercount==0):
        print("utiliser au minimum un caractere miniscule")
    if(majuscount==0):
        print("utiliser au minimum un caractere majuscule")
    if(numbercounter==0):
        print("utiliser au minimum un chiffre")
    if(symbolcounter==0):
        print("utiliser au minimum un symbol")            
    if (lowercount != 0 and majuscount != 0 and numbercounter != 0 and symbolcounter!= 0):
       return 1
    return 0                        


def genererpass():
    while True :
        test='1'
        pwd=""
        x=random.randint(6,8)
        for i in range(x) :
            p=random.randint(1,4)
            if(p==1):
                pwd+=random.choice(string.ascii_lowercase)
            elif(p==2):
                pwd+=random.choice(string.ascii_uppercase)
            elif(p==3):
                pwd+=random.choice(string.digits)
            elif(p==4):
                pwd+=random.choice(string.punctuation)
        lowercount=0
        majuscount=0
        numbercounter=0
        symbolcounter=0
        for c in pwd :
            if (c.islower()):
                lowercount+=1
            if (c.isupper()):
                majuscount+=1
            if (c.isdigit()):
                numbercounter+=1        
            if (not c.isalnum()):
                symbolcounter+=1                      
        if (lowercount != 0 and majuscount != 0 and numbercounter != 0 and symbolcounter!= 0):
            test ='0'
        if (test =='0'):
            return(pwd)
        
def ciphercaesar(a , b) :
    Alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    a=a.upper()                        
    for i in a :
        if i.isalpha() :
            result+=Alph[(Alph.index(i)+int(b))%26] 
        else :
            result+=i    
    return result  
def ciphercaesar2(a , b) :
    Alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    a=a.upper()                        
    for i in a :
        if i.isalpha() :
            result+=Alph[(Alph.index(i)-int(b))%26] 
        else :
            result+=i    
    return result  

def ciphercaesarASCII(a, b):
    result = ''
    a = a.upper()
    for i in a:
        if i.isalpha():
            result+=chr((ord(i) + int(b) - ord('A')) % 26 + ord('A'))
        else:
            result+=i
    return result

def ciphercaesarASCII2(a, b):
    result = ''
    a = a.upper()
    for i in a:
        if i.isalpha():
            result+=chr((ord(i) - int(b) - ord('A')) % 26 + ord('A'))      
        else:
            result+=i
    return result


