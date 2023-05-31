from tkinter import *
from tkinter import messagebox
from socket import *
from threading import *

host = '127.0.0.1'
port = 7004


window = Tk()
window.title("RPS Client")
window.geometry("600x150")

label = Label( window, text="Rock-Paper-Scissors Game ")
label.grid(row=1,column=2)

choose = None
received = None
def rock():
    global choose , received
    choose = "r"
    #handle2(choose)
    s.send(choose.encode('utf-8'))
    while(received == None):
        continue
    if(received == "s"):
        label2['text']="You win"
    elif(received == "p"):
        label2['text']= "you lose"
    elif(received == "r"):
        label2['text']= "Draw!"
    
    

def paper():
    global choose, received 
    choose = "p"
    #handle2(choose)
    s.send(choose.encode('utf-8'))
    while(received == None):
        continue
    if(received == "r"):
        label2['text']="You win"
    elif(received == "s"):
        label2['text']= "you lose"
    elif(received == "p"):
        label2['text']= "Draw!"

def scissors():
    global choose , received
    choose = "s"
    #handle2(choose)
    s.send(choose.encode('utf-8'))
    while(received == None):
        continue
    if(received == "p"):
        label2['text']="You win"
    elif(received == "r"):
        label2['text']= "you lose"
    elif(received == "s"):
        label2['text']= "Draw!"

def replay():
    global choose ,received,label2
    choose = None
    received = None 
    label2.destroy()
    label = Label( window, text="Rock-Paper-Scissors Game ")
    label.grid(row=1,column=2)
    R= Button(window, text="Rock", width=25, command= rock,padx=5)
    R.grid(row=3, column=1)
    P= Button(window, text="Paper", width=25, command= paper,padx=5)
    P.grid(row=3, column=2)
    S= Button(window, text="Scissors ", width=25, command= scissors,padx=5)
    S.grid(row=3, column=3)
    label2 = Label( window, text="Result ")
    label2.grid(row=5,column=2)
    button= Button(window, text="Replay", width=15, command= replay)
    button.grid(row=7, column=2)

def handle():
    global received
    while True:
        x = s.recv (2048)
        x = x.decode ('UTF-8')
        received = x
        
#def handle2(choose):
 #   s.send(choose.encode('utf-8'))
       
        
R= Button(window, text="Rock", width=25, command= rock,padx=5)
R.grid(row=3, column=1)
P= Button(window, text="Paper", width=25, command= paper,padx=5)
P.grid(row=3, column=2)
S= Button(window, text="Scissors ", width=25, command= scissors,padx=5)
S.grid(row=3, column=3)
label2 = Label( window, text="Result ")
label2.grid(row=5,column=2)
button= Button(window, text="Replay", width=15, command= replay)
button.grid(row=7, column=2)





s = socket(AF_INET,SOCK_STREAM)
print("The socket is created!")
s.connect((host,port))

t=Thread(target=handle)
t.start()
#t2=Thread(target=handle2)
#t2.start()

window.mainloop()