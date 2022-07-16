import tkinter as tk
import socket,os
list1=os.listdir()
ser=socket.gethostname()
ser=socket.gethostbyname(ser)
#tk.Label(text=ser).pack()
def slc(w):
      filename.delete(0,'end')
      filename.insert(0,lis9.get('anchor'))
lis9=tk.Listbox()
lis9.pack()    
lis9.bind('<ButtonRelease-1>',slc)
for DJ in list1:
      lis9.config(lis9.insert('end',DJ))

      
root=tk.Tk()
root.update()      
def server():
      s= socket.socket()
      try:
          a=open(but2.get()+filename.get(),"rb")
          a=a.read()
      except:
          tk.Label(text='no such file exist',fg='red').pack()
          return
      tk.Label(text=str(len(str(len(a)))),fg='green').pack()
      root.update()
      
      try:
          s.bind((but.get(),int(but1.get())))
          tk.Label(text='Server created').pack()
      except:
          tk.Label(text='Unable To Create server Server',fg='red').pack()
          if but1.get()=='61987':
              return
          but1.delete(0,"end")
          but1.insert(0,'61987')
          server()
          return
    
      s.listen(2)
      root.update()
      while True:
            c,addr=s.accept()
            print(addr)
            tk.Label(text=f'connected to {addr}').pack()
            root.update()
            c.send(bytes(filename.get(),'utf-8'))
            c.send(bytes(str(len(a)),'utf-8'))
            c.send(a)
            c.close()

but=tk.Entry()
but.pack()
but.insert(0,'192.168.43.64')

but1=tk.Entry()
but1.pack()
but1.insert(0,"9999")

but2=tk.Entry()
but2.pack()
but2.insert(0,"")

filename=tk.Entry()
filename.pack()
#filename.insert(0,"file")



send=tk.Button(text="Send file",activebackground='red',command = server).pack()
fram=tk.Frame(height=400,width=500,bg='white')
#fram.pack()

root.mainloop()
