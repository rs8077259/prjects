import socket as sk
import tkinter as tk
import os
root=tk.Tk()
def receive():
    ip1=i.get()
    port1=int(en.get())
    c=sk.socket()
    try:
        c.connect((ip1,port1))
    except:
        la=tk.Label(text='connection failed',fg='red')
        la.pack()
        
        return
    la=tk.Label(text='connection Successful',fg='green')
    la.pack()   
    en1.delete(0,'end')
    en1.insert(0,c.recv(1024))
    if en1.get() in os.listdir():
    	os.remove(en1.get())
    a=open(en1.get(),"ab")
    la.destroy()
    lab=tk.Label(text='0')
    lab.pack()
    lenth=int(c.recv(int(en2.get())))
    
    rec=0
    while True:
        h=c.recv(2048)
        rec+=len(h)
        re=(rec/lenth)*100
        if re<33:
        	lab.config(fg='red')
        if re>33 and re<80:
        	lab.config(fg='yellow')
        if re>80:
        	lab.config(fg='green')
        lab.config(text=str(re))
        root.update()  
        
        if h==b'':
            break
        a.write(h)
    a.close()
    lab.config(lab.config(text='Done...'))
but=tk.Button(text='receive',command=receive,activebackground='green')
i=tk.Entry()
i.pack()
i.insert(0,'192.168.43.64')
en=tk.Entry()
en.pack()
en.insert(0,'9999')
en1=tk.Entry()
en1.pack()

en2=tk.Entry()
en2.pack()
but.pack(side='bottom')
root.mainloop()
