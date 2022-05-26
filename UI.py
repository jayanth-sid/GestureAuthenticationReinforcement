import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import tkinter.ttk as ttk
import tkinter.font as font
import Predictor
import tracker
import Authentication
model = Predictor.load_model()
window=tk.Tk()
window.title("Gesture Based Authentication Reinforcement")
window.geometry('800x600')
window.configure(bg='#5ce1e6')

login_label= tk.Label(window, text="Login Here" ,bg="#5ce1e6"  ,fg='black'  ,width=10 ,height=1,font=('open sans extra bold', 20, 'bold'))
login_label.place(x=70, y=150)

reg_label= tk.Label(window, text="Register Here" ,bg="#5ce1e6"  ,fg='black'  ,width=10 ,height=1,font=('open sans extra bold', 20, 'bold'))
reg_label.place(x=530, y=150)

#Notification
message = tk.Label(window,text="",bg="#83f7b2" ,fg="white", width=30, height=2, font=('Helvetica',20,'bold'))
message.place(x=150,y=500)



#Login FIEDLS
lbl = tk.Label(window, text="Enter ID :",width=10,height=1,bg = '#5ce1e6'  ,fg="black"  ,font=('Helvetica', 10, ' bold '), justify = 'left'  )
lbl.place(x=70, y=210)

txt = tk.Entry(window,width=25  ,bg="#CAEBF2" ,fg="black",font=('Helvetica', 10, ' bold '), justify = 'left')
txt.place(x=70, y=230)

lbl2= tk.Label(window, text="Enter Password :",width=15  ,height=1  ,fg="black"  ,bg='#5ce1e6' ,font=('Helvetica', 10, ' bold '), justify = 'left' )
lbl2.place(x=70, y=260)

txt2 = tk.Entry(window,width=25  ,bg="#CAEBF2" ,show='*',fg="black",font=('Helvetica', 10, ' bold '), justify = 'left')
txt2.place(x=70, y=280)




#Register Fields

lbl3 = tk.Label(window, text="Enter ID :",width=10,height=1,bg = '#5ce1e6'  ,fg="black"  ,font=('Helvetica', 10, ' bold '), justify = 'left' )
lbl3.place(x=530, y=210)

txt3 = tk.Entry(window,width=25  ,bg="#CAEBF2" ,fg="black",font=('Helvetica', 10, ' bold '), justify = 'left')
txt3.place(x=530, y=230)

lbl4= tk.Label(window, text="Enter Password :",width=15  ,height=1  ,fg="black"  ,bg='#5ce1e6' ,font=('Helvetica', 10, ' bold '), justify = 'left')
lbl4.place(x=530, y=260)

txt4 = tk.Entry(window,width=25  ,bg="#CAEBF2" ,show='*',fg="black",font=('Helvetica', 10, ' bold '), justify = 'left')
txt4.place(x=530, y=280)

def login_clear():
    txt.delete(0,'end')
    txt2.delete(0,'end')
    #res = ""
    #txt.configure(text= res)
    #txt2.configure(text=res)
def reg_clear():
    txt3.delete(0,'end')
    txt4.delete(0,'end')
    #res = ""
    #txt3.configure(text= res)
    #txt4.configure(text=res)

def message_clear():
    pass

def login_submit():
    a = txt.get()
    b = txt2.get()
    if a == '' or b == '':
        message.configure(text='Enter ID and password',fg = 'red')
    else:
        message.configure(text="Capturing" , fg = 'green')
        path_extracted = tracker.run()
        message.configure(text = 'Predicting , Authenticating')
        prediction = Predictor.predict(model , path_extracted)

        msg = Authentication.login_user(a,b,prediction)
        if msg == 1:
            message.configure(text="User Not Found" , fg = "red")
        elif msg == 3:
            message.configure(text="Authentication Failed", fg="red")
        else:
            message.configure(text="Authentication Successful", fg="green")
        cv2.imshow("img",path_extracted)
        cv2.waitKey(0)
        print(prediction)
    login_clear()
    reg_clear()

def reg_submit():
    Userid = txt3.get()
    passcode = txt4.get()
    if Userid == '' or passcode =='':
        message.configure(text = 'Enter ID and password' ,fg = 'red')
    else:
        path_extracted = tracker.run()
        prediction = Predictor.predict(model, path_extracted)
        print(list(prediction.keys())[0],passcode)
        r = Authentication.create_user(Userid,passcode,list(prediction.keys())[0])
        if r == 1:
            message.configure(text="User registered" , fg="green")
        else:
            message.configure(text="Failed", fg="red")
    login_clear()
    reg_clear()


#Login Actions
submit = tk.Button(window, text="Submit",fg="red",command= login_submit, bg="#CAEBF2"  ,width=7 ,height=1 ,activebackground = "#7ed957" ,font=('Helvetica', 10, ' bold '))
submit.place(x=70, y=320)

clearButton = tk.Button(window, text="Clear",fg="red", command=login_clear,bg="#CAEBF2"  ,width=7  ,height=1, activebackground = "#eb4d77" ,font=('Helvetica', 10, ' bold '))
clearButton.place(x=170, y=320)

#Register Actions
submit2 = tk.Button(window, text="Submit",fg="red", command=reg_submit, bg="#CAEBF2"  ,width=7  ,height=1 ,activebackground = "#7ed957" ,font=('Helvetica', 10, ' bold '))
submit2.place(x=530, y=320)

clearButton2 = tk.Button(window, text="Clear",command=reg_clear, fg="red"  ,bg="#CAEBF2"  ,width=7  ,height=1, activebackground = "#eb4d77" ,font=('Helvetica', 10, ' bold '))
clearButton2.place(x=630, y=320)






#final Actions
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="white"  ,bg="red"  ,width=20  ,height=2, activebackground = "Red" ,font=('Helvetica', 15, ' bold '))
quitWindow.place(x=1000, y=550)
window.mainloop()