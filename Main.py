import tkinter
import customtkinter    
from CTkMessagebox import CTkMessagebox
from Sub_Functions import *
from PIL import Image, ImageTk
import qrcode
import os 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

### Check if file exist and add first lign in it
if os.path.exists(r"C:\test\enregistrement") :
    pass
else : 
    file = open('enregistrement','w')
    lignedata = '{0:<30}{1:<10}\n'.format('Email','Password')       
    if os.path.getsize('enregistrement') == 0:
        file.write(lignedata)
        file.close()   


### All btns that Swap frames ##      
def gotoregister() :
    welcome.place_forget()
    registerframe.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
def gotologin() :
    welcome.place_forget()
    login.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)  
def caesartoalpha () :
    menucaesarfunction.place_forget()
    caesar_alpha.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
def caesartoascii () :
    menucaesarfunction.place_forget()
    caesar_ascii.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
def datatodict() :
    with open("fromagenew.txt", "r") as f:
        lines = f.readlines()
    data = []
    for line in lines:
        line = line.split()
        data.append(line)    
    dataset = {}
    for value in data:
        key = value[0]
        value = value[1:]
        dataset[key] = value
    CTkMessagebox(title="Dataset To Dict", message=dataset)
    
def datatofigure () :
    menudatasetfunction.place_forget()
    menudatasetfigure.place(relx= 0.5 ,rely=0.5 , anchor=tkinter.CENTER)
def back8() :
    menuhashfunction.place_forget()
    home.place(relx=0.5 , rely=0.5 , anchor = tkinter.CENTER)
def back3() :
    ABDfunction.place_forget()
    menuhashfunction.place(relx=0.5 , rely=0.5 , anchor = tkinter.CENTER)
def back4() :
    hashfunction.place_forget()
    menuhashfunction.place(relx=0.5 , rely=0.5 , anchor = tkinter.CENTER)
def back5() :
    menucaesarfunction.place_forget()
    home.place(relx=0.5 , rely=0.5 , anchor = tkinter.CENTER)
def back6() :
    caesar_alpha.place_forget()
    menucaesarfunction.place(relx=0.5 , rely=0.5 , anchor = tkinter.CENTER)
def back7() :
    caesar_ascii.place_forget()
    menucaesarfunction.place(relx=0.5 , rely=0.5 , anchor = tkinter.CENTER)
def back13() :
    menudatasetfunction.place_forget()
    home.place(relx=0.5 , rely=0.5 , anchor = tkinter.CENTER)
def back14() :
    menudatasetfigure.place_forget()
    menudatasetfunction.place(relx=0.5 , rely=0.5 , anchor = tkinter.CENTER)    
def btnfhere() :
    login.place_forget()
    registerframe.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER) 
def backwelcome() :
    login.place_forget()
    welcome.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
def backwelcome2() :
    registerframe.place_forget()
    welcome.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)    
def hashtohash256 () :
    menuhashfunction.place_forget()
    hashfunction.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
def hashtoABD () :
    menuhashfunction.place_forget()
    ABDfunction.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
def back11 () :
    update.place_forget()
    home.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
def hometomenuhash () :
    home.place_forget()
    menuhashfunction.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
def hometoABD () :
    home.place_forget()
    ABDfunction.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
def hometoupdate () :
    home.place_forget()
    update.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
def hometocaesarmenu () :
    home.place_forget()
    menucaesarfunction.place(relx=0.5 , rely=0.5 , anchor = tkinter.CENTER)
def qrframetohome() :
    qrframe.place_forget()
    home.place(relx=0.5 , rely=0.5 , anchor = tkinter.CENTER)
def hometodataset () :
    home.place_forget()
    menudatasetfunction.place(relx=0.5 , rely=0.5 , anchor = tkinter.CENTER)


# System settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")
# The application
app = customtkinter.CTk()
app.geometry("600x440")
app.title("Project Python")
### making the background image blend in every frame
my_image = ImageTk.PhotoImage(Image.open('bgp2.jpg'))
button = customtkinter.CTkLabel(app, image=my_image ,)
button.pack()

### Attack by dictionnaire btn
def submitABD () :
    file = open('dictexemple.txt',"r")
    dictlines = file.readlines()
    file.close()
    print(msgABD.get())
    for i in dictlines :
        print(hashlib.sha256(i.encode()).hexdigest())
        if msgABD.get() == hashlib.sha256(i.encode()).hexdigest() : 
            CTkMessagebox(title="ABD", message="The attack by dictionnaire is coming") 
        else :
            CTkMessagebox(title="ABD", message="not included in dict") 

def caloriesbycheese () :
    with open("fromagenew.txt", "r") as f:
        lines = f.readlines()
    data = []
    for line in lines:
        line = line.split()
        data.append(line)    
    dataset = {}
    for value in data:
        key = value[0]
        value = value[1:]
        dataset[key] = value
    df = pd.DataFrame(dataset)
    fig1, ax1 = plt.subplots()
    canvas1 = FigureCanvasTkAgg(fig1,master=menudatasetfigure)
    ax1.barh(df["Fromage"], df["Calories"])
    ax1.set_title("Calories by Cheese")
    ax1.set_xlabel("Cheese")
    ax1.set_ylabel("Calories")
    canvas1.draw()
    canvas1.get_tk_widget().place(relx=0.5, rely=0.20 , width=600 ,height=400)   
    

def caloriesbycheese1():
    
    with open("fromagenew.txt", "r") as f:
        lines = f.readlines()
    data = []
    for line in lines:
        line = line.split()
        data.append(line)    
    dataset = {}
    for value in data:
        key = value[0]
        value = value[1:]
        dataset[key] = value
    df = pd.DataFrame(dataset)
    fig2, ax2 = plt.subplots()
    canvas2 = FigureCanvasTkAgg(fig2,master=menudatasetfigure)
    ax2.barh(df["Fromage"], df["Sodium"])
    ax2.set_title("Sodium by Cheese")
    ax2.set_xlabel("Cheese")
    ax2.set_ylabel("Sodium")
    canvas2.draw()
    canvas2.get_tk_widget().place(relx=0.05, rely=0.2 , width=600 , height=400 )  
    
    
    
def submithash256 () :
    if not msg.get()== "" :
        CTkMessagebox(title="Your hash", message=hashlib.sha256(msg.get().encode()).hexdigest()) 

#### The update function
def updateaccount() :
    global emailglobal     
    file = open('enregistrement','r')
    lines = file.readlines()
    file.close()
    refreshfile = 1
    if update_email.get() == "" or update_pwd.get() == "" :
        CTkMessagebox(title="Error", message="Fill the form Please ..")
    else :
        tempemail = existemail (lines , update_email.get())
        print(tempemail)
        print(isValid(update_email.get()))
        if tempemail != 0 or isValid(update_email.get())==False  :
            CTkMessagebox(title="Error", message="This email isnt valid ..")
        else :
            if isValidpass(update_pwd.get()) == 1 :
                with open('Email2','w') as tempfichier :
                    if os.path.getsize('Email2') == 0:       
                        tempfichier.write('{0:<30}{1:<10}\n'.format('Email','Password'))
                        for line in lines :    
                            num = 1
                            if (line != lines[0]) :     
                                test = re.split('([a-zA-Z0-9]+[.-_]*[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[A-Z|a-z]{2,}))',line)
                                if ( emailglobal != test[1]): 
                                    data = '{0:<30}{1:<10}\n'.format(test[1], test[3].strip())         
                                    tempfichier.write(data)  
                                    num += 1  
                        data = '{0:<30}{1:<10}\n'.format( update_email.get(), update_pwd.get())
                        tempfichier.write(data)   
                        refreshfile = 0
                        emailglobal = update_email
                        CTkMessagebox(title="Update", message="The account got updated with success")

            else:
                CTkMessagebox(title="Error", message="This Pass isnt valid ..")
    if (refreshfile == 0) :
        with open('Email2','r') as sssread : 
            copylines = sssread.readlines()
        with open('enregistrement','w') as ss :
            lignedata = '{0:<30}{1:<10}\n'.format('Email','Password') 
            ss.write(lignedata)
            n = 1
            for copyline in copylines :
                if (copyline != copylines[0]) : 
                    test = re.split('([a-zA-Z0-9]+[.-_]*[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[A-Z|a-z]{2,}))',copyline)
                    data = '{0:<30}{1:<10}\n'.format(test[1], hashlib.sha256(test[3].strip().encode()).hexdigest())  
                    ss.write(data)
                    n+=1           
            os.remove('Email2')
            refreshfile = 1

def registerrandompass () :
    file1=open('enregistrement','r')
    lines = file1.readlines()
    file1.close()
    if wel_email.get()=="" or wel_pwd.get()!="" or wel_pwd2.get()!="" :
        CTkMessagebox(title="Error", message="To register using this feature you need just to fill email and leave the other textboxes empty")
    else:
        if existemail(lines , wel_email.get()) == 0 :
                if isValid(wel_email.get()) :
                    File1=open('enregistrement','a')
                    lignedata = '{0:<30}{1:<10}\n'.format('Email','Password')       
                    if os.path.getsize('enregistrement') == 0:
                        File1.write(lignedata)
                        File1.close()
                    password = genererpass()
                    global emailglobal 
                    global passglobal
                    passglobal = password
                    emailglobal = wel_email.get()
                    data = '{0:<30}{1:<10}\n'.format(wel_email.get(), hashlib.sha256(password.strip().encode()).hexdigest())
                    with open('enregistrement','a') as sss :
                        sss.write(data)
                    qrcode.make(password).save("mypass.png")     
                    CTkMessagebox(title="Info", message="valid registration " ) 
                    registerframe.place_forget() 
                    qrframe.place(relx=0.5 , rely=0.5 ,anchor =tkinter.CENTER )
                    my_imageqr = ImageTk.PhotoImage(Image.open('mypass.png').resize((200,200)))
                    btnbackqr = customtkinter.CTkLabel(qrframe, image=my_imageqr , text="" ,)
                    btnbackqr.place(x=55 , y=100)
                else :
                    CTkMessagebox(title="Info", message="Enter a valid email " )
        else :
            CTkMessagebox(title="Info", message="This email is already used in our database")

def register () : 
    file1=open('enregistrement','r')
    lines = file1.readlines()
    file1.close()

    if wel_email.get()=="" or wel_pwd.get()=="" or wel_pwd2.get()=="" :
        CTkMessagebox(title="Error", message="To register you need to fill the form")
    else:
        if existemail(lines , wel_email.get()) == 0 :
            if wel_pwd2.get() == wel_pwd.get() :    
                if isValid(wel_email.get()) and isValidpass(wel_pwd.get()):
                    File1=open('enregistrement','a')
                    lignedata = '{0:<30}{1:<10}\n'.format('Email','Password')       
                    if os.path.getsize('enregistrement') == 0:
                        File1.write(lignedata)
                        File1.close()
                    password = hashlib.sha256(wel_pwd.get().encode()).hexdigest()
                    data = '{0:<30}{1:<10}\n'.format(wel_email.get(), password)
                    with open('enregistrement','a') as sss :
                        sss.write(data)
                    CTkMessagebox(title="Info", message="valid registration") 
                    registerframe.place_forget() 
                    login.place(relx=0.5 , rely=0.5 ,anchor =tkinter.CENTER )
                else :
                    CTkMessagebox(title="Info", message="Your password must have 1 sym , 1min , 1 majus ,8length")
            else :
                CTkMessagebox(title="Info", message="Your password must match your confirmation")
        else :
            CTkMessagebox(title="Info", message="This email is already used in our database")
    
#This function reads from files the existing email and pass to verify and grant access
def log() :
    global emailglobal
    global passglobal
    file = open('enregistrement',"r")
    lines = file.readlines()
    file.close()
    password = hashlib.sha256(log_pwd.get().encode()).hexdigest()
    if not existemail(lines , log_email.get())==0 :
        hashacomparer = existemail(lines , log_email.get())
        print(hashacomparer[3].strip())
        if hashacomparer[3].strip() == password :
            CTkMessagebox(title="Info", message="Access granted ") 
            emailglobal = log_email.get() 
            passglobal = log_pwd.get()   
            login.place_forget()
            home.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER) 
        else :
            CTkMessagebox(title="Info", message="Invalid Pass")    
    else : 
        CTkMessagebox(title="Info", message="Invalid Email")

def cryptcaesaralpha () :
    if msgalpha.get() == "" and msgalpha2.get() == "" :
        CTkMessagebox(title="Cryptalpha", message="You must fill the form !!")
    else :    
        x=ciphercaesar(msgalpha.get(),msgalpha2.get())
        CTkMessagebox(title="Cryptalpha", message=x)

def cryptcaesaralpha2 () :
    if msgalpha.get() == "" and msgalpha2.get() == "" :
        CTkMessagebox(title="Cryptalpha", message="You must fill the form !!")
    else :    
        x=ciphercaesar2(msgalpha.get(),msgalpha2.get())
        CTkMessagebox(title="Cryptalpha", message=x)        

def cryptcaesarascii () : 
    if msgascii2.get() == "" and msgascii.get() == "" :
        CTkMessagebox(title="Cryptascii", message="You must fill the form !!")
    else :   
        c=ciphercaesarASCII( msgascii.get() ,msgascii2.get()) 
        CTkMessagebox(title="Cryptascii", message=c )

def Dryptcaesarascii () :
    if msgascii2.get() == "" and msgascii.get() == "" :
        CTkMessagebox(title="Drypt", message="You must fill the form !!")
    else :   
        c2=ciphercaesarASCII2( msgascii.get() ,msgascii2.get()) 
        CTkMessagebox(title="Drypt", message=c2 )        

### First Frame to show up(welcome) ##
welcome = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
log_label = customtkinter.CTkLabel(master=welcome , text="Welcome" , font=('century gothic', 36))
log_label.place(x=50 , y=50)
btnlogin = customtkinter.CTkButton(welcome , text="Login" , command=gotologin)
btnlogin.place(x=75 , y=200)
btnregister = customtkinter.CTkButton(welcome , text="Register" , command=gotoregister)
btnregister.place(x=75 , y=150)
welcome.place(relx=0.5,rely=0.5 , anchor=tkinter.CENTER)

######Login page###########
login = customtkinter.CTkFrame(master=button , width=280 ,height=330 , corner_radius=16 ,)
log_label = customtkinter.CTkLabel(master=login , text="Log into your account" , font=('century gothic', 20))
log_label.place(x=30 , y=50)
log_email = customtkinter.CTkEntry(master=login , width=220 , placeholder_text="Email")
log_email.place(x=30 , y=105)
log_pwd = customtkinter.CTkEntry(master=login , width=220 , placeholder_text="Password" ,show="*")
log_pwd.place(x=30 , y= 150)
log_label = customtkinter.CTkLabel(master=login , text="Forget Password" , font=('century gothic', 12))
log_label.place(x=150 , y=180)
btn_login = customtkinter.CTkButton(master=login , width=220 , text="Login" , corner_radius=8 , command=log)
btn_login.place(x=30 , y=210)
log_label = customtkinter.CTkLabel(master=login , text="Create Account Here" , font=('century gothic', 12))
log_label.place(x=70 , y=240)


#######register page#############
registerframe = customtkinter.CTkFrame(master=button , width=280 ,height=330 , corner_radius=16 ,)
wel_label = customtkinter.CTkLabel(master=registerframe , text="Register an account" , font=('century gothic', 20))
wel_label.place(x=40 , y=50)
wel_email = customtkinter.CTkEntry(master=registerframe , width=220 , placeholder_text="Email")
wel_email.place(x=30 , y=105)
wel_pwd = customtkinter.CTkEntry(master=registerframe, width=220 , placeholder_text="Password" ,show="*")
wel_pwd.place(x=30 , y= 150)
wel_pwd2 = customtkinter.CTkEntry(master=registerframe , width=220 , placeholder_text="Confirm Password",show="*")
wel_pwd2.place(x=30 , y= 195)
btn_login = customtkinter.CTkButton(master=registerframe , width=220 , text="Register" , corner_radius=8 ,command=register)
btn_login.place(x=30 , y=240)
btn_login2 = customtkinter.CTkButton(master=registerframe , width=220 , text="Register (Using Pass Generator)" , corner_radius=8 ,command=registerrandompass)
btn_login2.place(x=30 , y=285)


###home
home = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
btnfuncthash1 = customtkinter.CTkButton(master=home,   text="     Hash Menu    ", width=130 ,height=40 ,hover_color="#4158D0",command=hometomenuhash)
btnfuncthash1.place(x=70, y=40,)
btnfunctcesar2 = customtkinter.CTkButton(master=home,  text="   Caesar Cipher  ",  width=130 ,height=40 ,hover_color="#4158D0",command=hometocaesarmenu)
btnfunctcesar2.place(x=70, y=115,)
btnfunctdataset3 = customtkinter.CTkButton(master=home,text="DataSet Collection",  width=100 ,height=40 ,hover_color="#4158D0",command=hometodataset)
btnfunctdataset3.place(x=70, y=190,)
btnfunctupdate4 = customtkinter.CTkButton(master=home, text="Update Your account",  width=120 ,height=40 ,hover_color="#4158D0",command=hometoupdate)
btnfunctupdate4.place(x=70, y=265,)


##############################
## Menu du (hash256 , attack by dict , return)
##############################
menuhashfunction = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
btnmenuhash1 = customtkinter.CTkButton(master=menuhashfunction,width=100 , height=50 ,text="Hash the word using sha256" , command=hashtohash256)
btnmenuhash1.place(x=60, y=115,)
btnmenuhash2 = customtkinter.CTkButton(master=menuhashfunction,width=100 , height=50 ,text="     Attacking by Dict    ",command=hashtoABD)
btnmenuhash2.place(x=60, y=210,)


##############################
##hash word with sha256 Frame
##############################
hashfunction = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
#text dans hash
hashtext = customtkinter.CTkLabel(hashfunction,width=210 , font=('century gothic', 13)  , text="This is where you will hash your")
hashtext.place(x=35, y=50) 
hashtext2 = customtkinter.CTkLabel(hashfunction,width=210 , font=('century gothic', 13)  , text="message with the method sha256")
hashtext2.place(x=35, y=70) 
msg = customtkinter.CTkEntry(hashfunction, width=200, height=50, placeholder_text="Message ....", show="*")
msg.place(x=40 ,y=130)
btnsubmithash256 = customtkinter.CTkButton(master=hashfunction, text="Hash", command=submithash256)
btnsubmithash256.place(x=60, y=230,)

##############################
## Attack by Dict
##############################
ABDfunction = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
ABDtext = customtkinter.CTkLabel(ABDfunction,width=210 , font=('century gothic', 13) ,text="Hash your message using")
ABDtext.place(x=35, y=50) 
ABDtext2 = customtkinter.CTkLabel(ABDfunction,width=210 , font=('century gothic', 13) ,text="the method Attack by Dict ..")
ABDtext2.place(x=35, y=70) 
msgABD = customtkinter.CTkEntry(ABDfunction, width=200, height=60, placeholder_text="Message ...", show="*")
msgABD.place(x=40 ,y=130)
btnsubmitABD = customtkinter.CTkButton(master=ABDfunction, text="Attack by Dict",command=submitABD)
btnsubmitABD.place(x=60, y=230,)

##############################
## ceasar ascii
##############################
caesar_ascii = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
asciitext = customtkinter.CTkLabel(caesar_ascii,width=210 , font=('century gothic', 13) ,text="Crypt your message using")
asciitext.place(x=35, y=50) 
asciitext2 = customtkinter.CTkLabel(caesar_ascii,width=210 , font=('century gothic', 13) ,text="the Caesar ascii method ..")
asciitext2.place(x=35, y=70) 
msgascii = customtkinter.CTkEntry(caesar_ascii, width=200, height=60, placeholder_text="Message ...", )
msgascii.place(x=40 ,y=130)
msgascii2 = customtkinter.CTkEntry(caesar_ascii, width=200, height=20, placeholder_text="key ...", )
msgascii2.place(x=40 ,y=190)
btnascii = customtkinter.CTkButton(master=caesar_ascii, text="Crypt",command=cryptcaesarascii)
btnascii.place(x=60, y=230,)
btnascii2 = customtkinter.CTkButton(master=caesar_ascii, text="Derypt",command=Dryptcaesarascii)
btnascii2.place(x=60, y=260,)

##############################
## Caesar Alpha
##############################
caesar_alpha = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
alphatext = customtkinter.CTkLabel(caesar_alpha,width=210 , font=('century gothic', 13) ,text="Crypt your message using")
alphatext.place(x=35, y=50) 
alphatext2 = customtkinter.CTkLabel(caesar_alpha,width=210 , font=('century gothic', 13) ,text="the Caesar Alpha method ..")
alphatext2.place(x=35, y=70) 
msgalpha = customtkinter.CTkEntry(caesar_alpha, width=200, height=60, placeholder_text="Message ...", )
msgalpha.place(x=40 ,y=130)
msgalpha2 = customtkinter.CTkEntry(caesar_alpha, width=200, height=20, placeholder_text="key ...", )
msgalpha2.place(x=40 ,y=190)
btncryptcaesar = customtkinter.CTkButton(master=caesar_alpha, text="Crypt",command=cryptcaesaralpha)
btncryptcaesar.place(x=60, y=230,)
btncryptcaesar2 = customtkinter.CTkButton(master=caesar_alpha, text="Decrypt",command=cryptcaesaralpha2)
btncryptcaesar2.place(x=60, y=260,)
   
##############################
## Menu du (alpha , Ascii , return)
##############################
menucaesarfunction = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
# Btn menu 
btnmenucaesar1 = customtkinter.CTkButton(master=menucaesarfunction,width=100 , height=50 ,text="Crypt the word using Alpha" , command=caesartoalpha)
btnmenucaesar1.place(x=60, y=100,)
btnmenucaesar2 = customtkinter.CTkButton(master=menucaesarfunction,width=100 , height=50 ,text="Crypt the word using ASCII ",command=caesartoascii)
btnmenucaesar2.place(x=60, y=210,)

######update page###########
update = customtkinter.CTkFrame(master=button , width=280 ,height=330 , corner_radius=16 ,)
update_label = customtkinter.CTkLabel(master=update , text="Update your account" , font=('century gothic', 20))
update_label.place(x=30 , y=50)
update_email = customtkinter.CTkEntry(master=update , width=220 , placeholder_text="Email")
update_email.place(x=30 , y=105)
update_pwd = customtkinter.CTkEntry(master=update , width=220 , placeholder_text="Password" ,show="*")
update_pwd.place(x=30 , y= 150)
btn_update = customtkinter.CTkButton(master=update , width=220 , text="Update" , corner_radius=8 , command=updateaccount)
btn_update.place(x=30 , y=210)

######qr page###########
qrframe = customtkinter.CTkFrame(master=button , width=280 ,height=330 , corner_radius=16 ,)
qrframe_label = customtkinter.CTkLabel(master=qrframe , text="Scan this to get your pass" , font=('century gothic', 20))
qrframe_label.place(x=25 , y=50)
btn_qrframe = customtkinter.CTkButton(master=qrframe , width=220 , text="Go to Home" , corner_radius=8 , command=qrframetohome)
btn_qrframe.place(x=30 , y=270)

##############################
## Menu du dataset
##############################

menudatasetfunction = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
btnmenudata1 = customtkinter.CTkButton(master=menudatasetfunction,width=110 , height=50 ,text="Turn Your Dataset into Dict" , command=datatodict)
btnmenudata1.place(x=60, y=80,)
btnmenudata2 = customtkinter.CTkButton(master=menudatasetfunction,width=100 , height=50 ,text="Turn Your Dataset into Chart ",command=datatofigure)
btnmenudata2.place(x=60, y=210,)

##############################
## frame dataset chart
##############################

menudatasetfigure = customtkinter.CTkFrame(master=app , width=1200 ,height=700, corner_radius=16 ,) 
btnmenudata1 = customtkinter.CTkButton(master=menudatasetfigure,width=100 , height=50 ,text="Calories by Cheese" , command=caloriesbycheese)
btnmenudata1.place(x=800, y=60,)
btnmenudata2 = customtkinter.CTkButton(master=menudatasetfigure,width=100 , height=50 ,text="Sodium by Cheese" , command=caloriesbycheese1)
btnmenudata2.place(x=200, y=60,)



#### BACK Arrow BTNS ##
my_image11 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback11 = customtkinter.CTkButton(update, image=my_image11 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=back11)
btnback11.place(x=10 , y=10)
my_image1 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback1 = customtkinter.CTkButton(login, image=my_image1 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=backwelcome)
btnback1.place(x=10 , y=10)
my_image2 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback2 = customtkinter.CTkButton(registerframe, image=my_image2 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=backwelcome2)
btnback2.place(x=10 , y=10)
btnhere = customtkinter.CTkButton(login , text="Here" , text_color="blue" , font=('century gothic', 13) , width=10, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=btnfhere)
btnhere.place(x=166 , y=240)
my_image3 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback3 = customtkinter.CTkButton(ABDfunction, image=my_image3 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=back3)
btnback3.place(x=10 , y=10)
my_image8 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback8 = customtkinter.CTkButton(menuhashfunction, image=my_image8 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=back8)
btnback8.place(x=10 , y=10)
my_image4 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback4 = customtkinter.CTkButton(hashfunction, image=my_image4 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=back4)
btnback4.place(x=10 , y=10)
my_image5 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback5 = customtkinter.CTkButton(menucaesarfunction, image=my_image5 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=back5)
btnback5.place(x=10 , y=10)
my_image6 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback6 = customtkinter.CTkButton(caesar_alpha, image=my_image6 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=back6)
btnback6.place(x=10 , y=10)
my_image7 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback7 = customtkinter.CTkButton(caesar_ascii, image=my_image7 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=back7)
btnback7.place(x=10 , y=10)
my_image13 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback13 = customtkinter.CTkButton(menudatasetfunction, image=my_image13 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=back13)
btnback13.place(x=10 , y=10)
my_image14 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback14 = customtkinter.CTkButton(menudatasetfigure, image=my_image14 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=back14)
btnback14.place(x=10 , y=10)




app.mainloop()


