import tkinter as tk

def_user = 'User'
def_pswd = '12345'

window = tk.Tk()
window.title("LOGIN SYSTEM")
window.geometry("300x300")

Msg1 = tk.Label(text="Username")
Msg1.place(x=20,y=20)
plabel1 = tk.Label(text="Password")
plabel1.place(x=20,y=50)

e1 = tk.Entry(window)
e2 = tk.Entry(window,show='*')

e1.place(x=90,y=20)
e2.place(x=90,y=50)


def button1():
    
        usr=(e1.get())
        psd=(e2.get())
        if usr==def_user and psd == def_pswd:

           plabel2 = tk.Label(text="Login Success")
           plabel2.place(x=60,y=140)
        
        else:

            plabel3 = tk.Label(text="Login Failed")
            plabel3.place(x=60,y=140)

   # print("Login success")


b1= tk.Button(window,text='Log in',command=button1)
b1.place(x=60,y=100)




window.mainloop()