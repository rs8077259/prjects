print('importing modules')
import time,os,sys
def hfgui(u=12):
    for b in range(u):
        time.sleep(.0000000001)
        print('█',end='')
def gui(a=13,s=0,c='Done',t=0):
    for b in range(a):
        time.sleep(s)
        print('█',end='')
    print('\t',c)
    time.sleep(t)
def library_chk():
    library={'numpy':'numpy','pandas':'pandas','PIL':'Pillow','plyer':'plyer','matplotlib':'matplotlib'}
    lis=str(os.path)
    lis=((lis.replace('<module \'ntpath\' from \'','')).replace('\\\\','\\')).replace('ntpath.py\'>','site-packages')
    lis=os.listdir(lis)
    for a,b in library.items():
        if a in lis:
            pass
        else:
            os.system('pip install '+b)
library_chk()
hfgui(5)
import pandas as pd,matplotlib.pyplot as plt,plyer,numpy as np
from PIL import Image,ImageTk
hfgui(10)
import random,tkinter as tk,random,datetime
from tkinter import ttk,messagebox as msg
from datetime import timedelta
gui(a=10,c='Modules (✔)')

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   FUNCTIONS   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
def identyfy(j):
    try:
        b_no=int(book_no.get())
        n=list((book["Book no"]))
        if b_no in n:
            for kl in book[book["Book no"]==b_no]["Book_title"]:
                pass
            msg.showwarning(message=f'Book number alredy exist for book \n-->({kl})',title='####')
    except:
        pass
'==========================================================================================================================================================='    
def decode(csv):    
    pa=pd.read_csv(csv)
    lis=[*pa]
    for item in lis:
        zx=0
    
        for item1 in pa[item]:
            try:
                str(item1)
            except:
                pass
            add=0
            add1=0
            word=''
            while len(item1)>add:
            
                add+=4
                broken_element=item1[add1:add] #this will break individual element of encription in a single
                filtered_dataframe=hashcode[hashcode.code==broken_element]# serch hashcode of broken element in csv file

                add1+=4
                for _index in filtered_dataframe.index:
                    pass
                word+=filtered_dataframe.loc[_index,'Letter']
            pa.loc[zx,item]=word
            zx+=1
    return pa
'==========================================================================================================================================================='
def delete_(u):
    if entry.get()=='Serch Any Book':
        entry.delete(0,'end')
        entry.config(fg='black')
'==========================================================================================================================================================='
def encrift3(datafram):
    dataframe=pd.DataFrame(datafram,copy=True)
    for a in dataframe.columns:
        l=0
        for b in dataframe[a]:
            b=str(b)
            word=''
            for j in b:
                x=np.array(hashcode[hashcode['Letter']==j].code)
                word+=x[0] 
            dataframe.loc[l,a]=word
            l+=1

    return dataframe

def encript(sequence):
    c=0
    for a in sequence:
        a=str(a)
        word=""
        for b in a:
            x=np.array(hashcode[hashcode['Letter']==b].code)
            word+=x[0]
        sequence[c]=word
        c+=1    
    return sequence
'==========================================================================================================================================================='
def upgrade_book():
    j=book_table.selection()
    tup=book_table.item(j,'values')

    for do in j:
        pass
    lisd=[book_no.get(),book_name.get(),pages.get(),type_.get(),price.get(),book_d.get(),tup[-1]]
    book.loc[int(do)]=lisd
    book.to_csv('prog_book.csv',index=False)
    book_table.item(j,values=tuple(lisd))
    msg.showinfo(message=' Successfully upgraded Book',title='All Done')
'==========================================================================================================================================================='    
def exceptio_handel(a,b):
    if b==1:
        c='word_type,matched,letter_in_main_word,word_wanted'
    elif b==2:
        c='Letter,code'    
    elif b==3:
        c='Book no,Book_title,Number_Of_Pages,Type,Price,Book Detail,Status'
    elif b==4:
        c='name,id,password,ip_add'
    elif b==6:
        c='user,date,Time,Spent'
    if b!=5:
        f=open(a,"w")
        f.write(c)
        f.close()
    else:
        rot=tk.Tk()
        rot.geometry('1x1')
        a=sys.path
        msg.showwarning(title="data currupted error",message=f"we detected some encription error in your issue data.\n in process of back up your last time work will not be backuped so we are sving currupted data in file=\
{a[0]}\\curruteddata.csv")
        rot.destroy()
        location=pd.read_csv("backup\\backup.csv")
        try:
            issue_dat.to_csv("currupteddata.csv",index=False)
        except:
            pass
        location.to_csv("issue details.csv",index=False)
'==========================================================================================================================================================='
def photo(path):
    p=Image.open(path)
    p=ImageTk.PhotoImage(p)
    return p
'==========================================================================================================================================================='    
def add_book():
    global book,item,lis2
    l=(book_no.get(),book_name.get().capitalize(),pages.get(),type_.get(),price.get(),book_d.get(),'available')
    lis=[]
    
    if l[1] in book.Book_title:
        return
    elif '' in l:
        msg.showinfo(message=' not entered book or details',title='Requirments not entered')
    else:
        item+=1
        book_table.insert('',index='end',iid=item,values=l)
        book=book.append(pd.DataFrame({'Book no':[l[0]],'Book_title':[l[1]],'Number_Of_Pages':[l[2]],'Type':[l[3]],'Price':[l[4]],'Book Detail':[l[5]],'Status':[l[6]]},index=[item,]))
        book.to_csv('prog_book.csv',index=False)
        msg.showinfo(message=' Successfully added Book',title='All Done')
'==========================================================================================================================================================='
def retur_book_():
    
    selected=issue_table.selection()
    val=issue_table.item(selected,'values')
    if val=='':
        msg.askretrycancel(message='Sorry cannot find any issue to be returned please select entry',title='@')
        return
    val=list(val)
    
    val[-1]='Returned'
    val=tuple(val)
    issue_table.item(selected,values=val)
    got=issue_table.item(selected,'values')
    bkno=got[1]
    adm=got[4]
    is_da=got[6]
    lo=issue_data[issue_data['Student adm_no']==adm]
    lo=lo[lo['Book No']==bkno]
    lo=lo[lo['Issue Date']==is_da]
    lo=lo.index
    ifound=lo
    for h in ifound:
        pass
    if issue_data.loc[h,'Returned on']=='Not Returned':
        issue_data.loc[h,'Returned on']='Returned'
        lk=encript(list(issue_data.loc[h]))
        issue_dat.loc[h]=lk
        
        issue_dat.to_csv('issue details.csv',index=False)
        indek=book[book['Book no']==int(bkno)]
        for k in indek.index:
            pass
        book.loc[k,'Status']='available'
        book.to_csv('prog_book.csv',index=False)
        msg.showinfo(message='Book returned',title='@')
    else:
        msg.askretrycancel(message='Book alredy received from this student',title='@')

'==========================================================================================================================================================='    
def bok_serch(p):
    try:
        n=book[book['Book no']==int(book_n.get())]['Book_title']
        for j in n:
            pass
        book_name2.delete(0,'end')
        book_name2.insert(0,j)
        issue_chk()

    except:
        pass
'==========================================================================================================================================================='
def mdb():
    global d_book
    m_d_b=list(issue_data['Book Name'].unique())
    d_book=pd.DataFrame(columns=[0,1])
    bak=pd.DataFrame(columns=[0,1])
    for fb in m_d_b:
        number=len(issue_data[issue_data['Book Name']==fb])
        bak.loc[len(bak)]=[fb,number]
    for x in range(3):
        lo=bak.loc[:,1].max(0)
        lo=bak[bak.loc[:,1]==lo]
        bak=bak.drop(lo.index)
        d_book=d_book.append(lo)
        
    plt.figure(figsize=(8,7))
    plt.title('most Demanded book')
    expl=[]
    for h in range(len(d_book)):
        expl.append(random.choice(np.arange(0,0.3,0.051)))
    plt.pie(d_book[1],labels=d_book[0],shadow=True,explode=expl)
    chart_view()
'==========================================================================================================================================================='    
def clibm():
    namesofstd=list(issue_data['Student Name'].unique())
    sfil=pd.DataFrame(columns=[0,1])
    sfil1=pd.DataFrame(columns=[0,1])
    for nam in namesofstd:
        b=len(issue_data[issue_data['Student Name']==nam])
        sfil.loc[len(sfil)]=[nam,b]
    for ran in range(4):
        max1=sfil[1].max(0)
        sfil1=sfil1.append(sfil[sfil[1]==max1],)
        sfil=sfil.drop(sfil[sfil[1]==max1].index)
    for sam in sfil[1].cumsum(0):
        pass
    sfil1.loc[len(sfil1)]=['Others',sam]
    explo=[]
    for y in range(len(sfil1)):
        explo.append(random.choice(np.arange(0,0.3,0.1)))
    plt.figure(figsize=(8,7))
    plt.title('Student issued Book most')
    plt.pie(sfil1[1],labels=sfil1[0],shadow=True,explode=explo)
    chart_view()
'==========================================================================================================================================================='
def color():
    global colour
    colour='r k m b g y c'
    colour=random.choice(colour.split(' '))
'==========================================================================================================================================================='
def surchacutest():
    data=pd.read_csv('dataforml.csv')
    matc=np.array(data.matched)
    word=np.array(data.letter_in_main_word)
    plt.figure(figsize=(8,6))
    color()
    plt.title('Serch Engin accuracy')
    plt.scatter(word,matc,marker='*',color=colour)
    chart_view()
'==========================================================================================================================================================='        
def chart_view():
    plt.savefig('chart\\chart.png')
    global pictue
    try:
        pictue
        pictue=photo('chart\\chart.png')
        sho.config(image=pictue,)
        
    except:
        pictue=photo('chart\\chart.png')
        sho=tk.Label(charts,image=pictue,bg='white')
        sho.place(x=500,y=50,)
'==========================================================================================================================================================='
def mostenterd():
    names=list(history.user.unique())
    ent=dict()
    for fb in names:
        hours=pd.DataFrame(columns=[0,1,2])
        detal=history[history['user']==fb]
        detal.iloc[:,-1].replace('0','00:00:00',inplace=True)
        detal.iloc[:,-1].replace(0,'00:00:00',inplace=True)
        for ik in detal.iloc[:,-1]:
            ik=str(ik)
            ik=ik.split(':')
            ik[-1]=ik[-1][0:ik[-1].find('.')]
            hours.loc[len(hours)]=[int(ik[0]),int(ik[1]),int(ik[2])]
        finding=hours.cumsum(0)
        finding.iloc[-1,1]=finding.iloc[-1,-2]+int(finding.iloc[-1,-1]//60) #secounds to min
        finding.iloc[-1,0]=finding.iloc[-1,0]+int(finding.iloc[-1,-2]//60)+finding.iloc[-1,1]%60/60 #min to hour
        ent[fb]=finding.iloc[-1,0]
        col=[]
        for t in range(len(ent)):
            col.append(random.choice(['r','k','m','b','g','y','c']))
        plt.figure(figsize=(8,7))
        plt.title('Id which spent time most')
        plt.bar(ent.keys(),ent.values(),color=col)
        plt.xlabel('ID')
        plt.ylabel('Time Spent in hours')
        chart_view()
'==========================================================================================================================================================='
def booktoissue():
    t_b=len(book)
    i_b=len(issue_data[issue_data['Returned on']=='Not Returned'])
    plt.figure(figsize=(8,7))
    choi=[]
    for a in range(2):
        choi.append(random.choice(np.arange(0,0.4,0.1)))
    plt.title('Total Book to issued Book')
    plt.pie([t_b,i_b],shadow=True,explode=choi,labels=['Abailable book','issued book'])
    plt.legend(loc='upper right')
    chart_view()
'==========================================================================================================================================================='
def chart():
    global charts
    charts=tk.Toplevel(master=windows,bg='white')
    charts.minsize(1300,700)
    charts.maxsize(1300,700)
    title=tk.Label(charts,text='CHARTS',font=('arial black',25),fg='red',bg='white')
    title.place(x=480,y=10)
    char1=tk.Button(charts,text='most demanded books',command=mdb,bg='white',fg='black',font=('arial black',17),borderwidth=0).place(x=90,y=270)
    char2=tk.Button(charts,text='Student issued book most time',command=clibm,bg='white',fg='black',font=('arial black',17),borderwidth=0).place(x=90,y=350)
    char3=tk.Button(charts,text='surch engin accuracy',command=surchacutest,bg='white',fg='black',borderwidth=0,font=('arial black',17)).place(x=90,y=430)
    char3=tk.Button(charts,text='Time spent',command=mostenterd,bg='white',fg='black',borderwidth=0,font=('arial black',17)).place(x=90,y=510)
    char3=tk.Button(charts,text='available/issued',command=booktoissue,bg='white',fg='black',borderwidth=0,font=('arial black',17)).place(x=90,y=590)
    
    charts.mainloop()
'==========================================================================================================================================================='    
def timegiven(destroy):
    timenow=datetime.datetime.now()
    history.iloc[his_index,-1]=timenow-entertime
    history.to_csv('enterhistory.csv',index=False)        
    try:
        destroy
    except:
        pass
    for b in globals().keys():
        del b

'==========================================================================================================================================================='
def add():
    global issue_dat
    lisy=[book_n.get(),book_name2.get(),std_name.get(),std_admno.get(),class_.get(),issue_d.get(),r_date.get()]
    if '' in lisy:
        msg.showinfo(message='details not correctly filled')
        return
    details=[len(issue_data),book_n.get(),book_name2.get(),std_name.get().capitalize(),std_admno.get(),class_.get().upper().replace(' ',''),issue_d.get(),r_date.get(),'Not Returned']  
    issue_data.loc[len(issue_data)]=details
    issue_table.insert('',index='end',iid=len(issue_data),values=details)
    checker=book[book.Book_title==book_name2.get()].index
    try:
        for hjk in checker:
            pass
    except:
        msg.askretrycancel(message="Book not found please chek spellings")
    if book.loc[hjk,'Status']!='available':
        nm=issue_data[issue_data['Book Name']==book_name2.get()]
        nm=nm[nm['Returned on']=='Not Returned']
        for dat in nm["Return Date"]:
            pass 
        msg.showerror(message=f'issue Failed  book alredy issued. wiil be availabe on {dat} ')
        return
    try:
        jk=encript(list(issue_data.iloc[-1]))
        issue_dat.loc[len(issue_dat)]=jk
        issue_dat.to_csv('issue details.csv',index=False)
        boo=book[book.Book_title==book_name2.get()]
        boo=boo.index
        for jj in boo:
            pass
        book.loc[jj,'Status']='Issued'
        book.to_csv('prog_book.csv',index=False)
        msg.showinfo(message=f'successfully issued {book_name2.get()} to {std_name.get()} upto Date {r_date.get()}')

    except:
        msg.showwarning(message=f'an unidentified error had occered in saving the file please recode this data in your register')
'==========================================================================================================================================================='        
def return_datei(key):
    try:
        r_date.delete(0,'end')
        r_date.insert(0,date+datetime.timedelta(int(interval.get())))
    except:
        pass
'==========================================================================================================================================================='
def delete_book():
    book=pd.read_csv('prog_book.csv')
    
    indec=book_table.selection()
    for i in indec:
        book_table.delete(i)
        book = book.drop([int(i)])
    book.to_csv('prog_book.csv',index=False)
    msg.showwarning(message=' Successfully deleted Book',title='All Done')
'==========================================================================================================================================================='
def upgrade(u):
    book_no.delete(0,'end')
    book_name.delete(0,'end')
    pages.delete(0,'end')
    type_.delete(0,'end')
    price.delete(0,'end')
    book_d.delete(0,'end')
    ID=book_table.selection()
    val=book_table.item(ID,'values')
    
    book_no.insert(0,val[0])

    book_name.insert(0,val[1])

    pages.insert(0,val[2])

    type_.insert(0,val[3])

    price.insert(0,val[4])

    book_d.insert(0,val[5])
'==========================================================================================================================================================='
def b_serch(l):

    global listbo2
    
    data = pd.read_csv('prog_book.csv')
    da=list(data.Book_title)
    user1=book_name2.get().lower().capitalize()
    user=book_name2.get().lower().replace(' ','')

    li=[]
    indx=[]

    try:
        listbo2.destroy()
    except:
        pass
    listbo2=tk.Listbox(issue_w,height=10,borderwidth=0)

    try:
        most_app=data[data['Book_title'].str.contains(user1)]
        most_app.append(data[data['Book_title'].str.contains(user1.lower())])
        if not most_app.empty:
            for kp in most_app.Book_title:
                listbo2.config(listbo2.insert('end',kp))
        for bak in most_app['Book_title']:
            da.remove(bak)
    except:
        pass

    for item in da:
        copy=item.lower().replace(' ','')
        mark=0
        lenth=0
        for i in user:
            lenth+=1
            if mark == 0:
                if i in copy:
                    fin=copy.find(i)
                    copy=copy[fin+1:]
                    mark+=1
                else:
                    mark-=1
            elif mark >= 1:
                if i in copy:
                    fnd=copy.find(i)
                    copy=copy[:fnd]+copy[fnd+1:]
                    mark+=1
                else:
                    mark-=1

            if lenth == len(user):
                percen=(mark/len(user))*100
                percent=(mark/len(item.replace(' ','')))*100

                if percen >= 85:
                    li.append(item)
                    indx.append(percent)

                elif percent >= 85:
                    li.append(item)
                    indx.append(percent)
                
                elif percen >= 74:
                    if percent >= 69:
                        li.append(item)
                        indx.append(percent)

                elif percent >= 74:
                    if percen >= 69:
                        li.append(item)
                        indx.append(percen)

    dta=pd.DataFrame(li,columns=['name'],index=indx).sort_index(ascending=False)

    
    for b in dta.loc[:,'name']:
        listbo2.config(listbo2.insert('end',b))
    
    listbo2.place(x=390,y=470,width=303)
    listbo2.yview()
    listbo2.bind('<ButtonRelease-1>',changer)
'==========================================================================================================================================================='
def loop(l):
    global listbo
    
    data = pd.read_csv('prog_book.csv')
    da=list(data.Book_title)
    user1=entry.get().lower().capitalize()
    user=entry.get().lower().replace(' ','')

    li=[]
    indx=[]

    
    try:
        listbo.destroy()
        listbo4.destroy()
    except:
        pass
    if user=='':
        return
    listbo=tk.Listbox(main_w,height=10,borderwidth=0)

    try:
        most_app=data[data['Book_title'].str.contains(user1)]
        most_app.append(data[data['Book_title'].str.contains(user1.lower())])
        if not most_app.empty:
            for kp in most_app.Book_title:
                listbo.config(listbo.insert('end',kp))
        for bak in most_app['Book_title']:
            da.remove(bak)
    except:
        pass

    for item in da:
        copy=item.lower().replace(' ','')
        mark=0
        lenth=0
        for i in user:
            lenth+=1
            if mark == 0:
                if i in copy:
                    fin=copy.find(i)
                    copy=copy[fin+1:]

                    mark+=1
                else:
                    mark-=1
            elif mark >= 1:
                if i in copy:
                    fnd=copy.find(i)
                    copy=copy[:fnd]+copy[fnd+1:]
                    mark+=1
                else:
                    mark-=1


            if lenth == len(user):
                percen=(mark/len(user))*100
                percent=(mark/len(item.replace(' ','')))*100

                if percen >= 78:
                    li.append(item)
                    indx.append(percent)

                elif percent >= 78:
                    li.append(item)
                    indx.append(percent)
                
                elif percen >= 69:
                    if percent >= 54:
                        li.append(item)
                        indx.append(percent)

                elif percent >= 69:
                    if percen >= 54:
                        li.append(item)
                        indx.append(percen)
    if li==[]:
        listbo.destroy()
        return
    dta=pd.DataFrame(li,columns=['name'],index=indx).sort_index(ascending=False)
    
    
    for b in dta.loc[:,'name']:
        listbo.config(listbo.insert('end',b))
    
    listbo.place(x=320,y=230,width=538)
    listbo.yview()
    listbo.bind('<ButtonRelease-1>',se)
'==========================================================================================================================================================='    
def se(i):
    global picture2
    global ML
    global listbo4
    user_entered=entry.get().lower()
    number1=len(user_entered)
    wanted=listbo.get('anchor').lower()
    entry.delete(0,'end')
    entry.insert(0,listbo.get('anchor'))
    listbo.destroy()
    listbo.destroy()
    listbo4=tk.Frame(main_w,height=285,bg='white')
    listbo4.place(x=320,y=230,width=538)
    got=book[book.Book_title==entry.get()]
    x=4
    y=10
    for col in book.columns:
        value=list(got[col])
        if col=='Book no':
            booknum=value[0]
        val=tk.Label(listbo4,text=f"{col}  = {value[0]}",font=('segoe script',13),bg='white').place(x=x,y=y)
        y+=29
 
    matched=0
    try:
        retun=issue_data[issue_data['Book Name']==entry.get()]
        retun=list(retun[retun['Returned on']=='Not Returned']['Return Date'])
        if retun[0]!='':
            val=tk.Label(listbo4,text=f"Return Date = {retun[0]}",font=('segoe script',13),bg='white').place(x=x,y=y)
    except:
        pass
    try:
        pic=list(bphoto[bphoto.BookNo==booknum].filename)
        pic=pic[0]
        background2=Image.open("bphoto\\"+pic)
        back=background2.resize((150,200),Image.ANTIALIAS)
        picture2=ImageTk.PhotoImage(back)
        pic=tk.Label(listbo4,image=picture2)
        pic.place(x=359,y=72)
    except:
        pass
    
    for a in np.array(list(user_entered)):
        if a in wanted:
            matched+=1
    ML.loc[len(ML)+1]=[user_entered,matched,len(wanted),wanted,number1]
    ML.to_csv('dataforml.csv',index=False)
'==========================================================================================================================================================='            
def changer(i):
    global picture3
    global ML
    user_entered=book_name2.get().lower()
    number1=len(user_entered)
    wanted=listbo2.get('anchor').lower()
    
    book_name2.delete(0,'end')
    book_name2.insert(0,listbo2.get('anchor'))
    listbo2.destroy()
    n=book[book.Book_title==book_name2.get()]['Book no']
    for k in n:
        pass
    book_n.delete(0,'end')
    book_n.insert(0,k)
    try:
        pic=list(bphoto[bphoto.BookNo==k].filename)
        pic=pic[0]
        background2=Image.open("bphoto\\"+pic)
        back=background2.resize((140,160),Image.ANTIALIAS)
        picture3=ImageTk.PhotoImage(back)
        pic=tk.Label(issue_w,image=picture3)
        pic.place(x=1219,y=480)
    except Exception as e:
        print(e)
    matched=0
    for a in np.array(list(user_entered)):
        if a in wanted:
            matched+=1
    ML.loc[len(ML)+1]=[user_entered,matched,len(wanted),wanted,number1]
    ML.to_csv('dataforml.csv',index=False)
    
'==========================================================================================================================================================='
def regis():
    print(otp)
    print(id_password.get())
    print(id_password.get()==id_pass_c.get())

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  CSV FILES  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
print('connecting to server...')
hfgui()
while True:
    try:ML=pd.read_csv('dataforml.csv')
    except:
        exceptio_handel('dataforml.csv',1)
        continue
    try:
        hashcode=pd.read_csv('hashcodes.csv')
    except:
        exceptio_handel('hashcodes.csv',2)
        continue
    try:    
        book=pd.read_csv('prog_book.csv')
    except:
        exceptio_handel('prog_book.csv',3)
        continue
    try:    
        userdata=decode('usersdata.csv')
    except:
        exceptio_handel('usersdata.csv',4)
        continue
    try:
        issue_dat=pd.read_csv('issue details.csv')
        issue_data=decode('issue details.csv')
        issue_dat.to_csv("backup\\backup.csv",index=False)
    except:
        exceptio_handel('issue details.csv',5)
        continue
    try:
        history=pd.read_csv('enterhistory.csv')
        break
    except:
        exceptio_handel('enterhistory.csv',6)
        continue
bphoto=pd.read_csv('photod.csv')
gui(c='Data are correct (✔)')

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   SUB WINDOW   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


print('checking functions...')
hfgui()
'''                                                    ------------------------------Defalter window----------------------------'''
    
def defalters():
    global kl,windows
    main_w.destroy()
    windows=tk.Tk()
    
    windows.minsize(1400,700)
    windows.maxsize(1400,700)
    windows.iconbitmap('Itzikgur-My-Seven-Books-2.ico')
    windows.title('Running... library management system')
    heading=tk.Label(windows,text='Defalters',font=('segoe script',30),fg='red',bg='white').pack(fill='both',)
    
    tree_view_frame=tk.Frame(windows,height=600,bg='white',width=1400)
    scroll=tk.Scrollbar(tree_view_frame,)
    scroll.place(x=1380,y=0,height=600)
    def_table=ttk.Treeview(tree_view_frame,show='headings',height=30,yscrollcommand=scroll.set)
    
    def_table['columns']=tuple(issue_data.columns)
    def_table.column('Serial No',width=90)
    def_table.column('Book No',width=90)
    def_table.column('Book Name',anchor='center',width=300)
    def_table.column('Student Name',anchor='center',width=140)
    def_table.column('Student adm_no',width=120)
    def_table.column('class\section',width=100)
    def_table.column('Issue Date',width=150)
    def_table.column('Return Date',width=150)
    for data in tuple(issue_data.columns):
        def_table.heading(data,text=data,)
    datas=issue_data['Return Date']

    
    date_n=datetime.datetime.now()
    extract=pd.DataFrame([])
    date_n=date_n.date()
    en=0
    for k in datas:

        j=k.split('-')
        dt=datetime.date(int(j[0]),int(j[1]),int(j[2]))
        if dt<date_n:
            extract=extract.append(issue_data.iloc[en])
        en+=1
    kl = extract[extract['Returned on']=='Not Returned']
    kl=kl.sort_values('class\section')
    
    for item3 in range(len(kl)):

            def_table.insert('',index='end',iid=item3,values=tuple(kl.iloc[item3]))
                
    def_table.place(x=0,y=0,width=1380)
    tree_view_frame.pack()
    button3=tk.Button(windows,text='Show Charts',font=('arial black',10),borderwidth=2,command=chart,bg='white',activebackground='red',activeforeground='white').place(x=1300,y=600)
    button6=tk.Button(windows,text='<-- Back ',borderwidth=2,font=('arial black',10),activeforeground='white',activebackground='red',command=lambda : main_window(windows.destroy())).place(x=20,y=600)
    windows.protocol('WM_DELETE_WINDOW',lambda : timegiven(windows.destroy()),)
    windows.mainloop()

'''                                                    ------------------------------issue window----------------------------'''
def issue_book():
    main_w.destroy()
    
    global tree_view_frame,issue_w,r_date,date,interval,book_n,book_name2,std_name,issue_d,std_admno,class_,issue_table,item2
    
    issue_w=tk.Tk()
    
    issue_w.title('Running... library management system')
    issue_w.geometry('1400x700')
    issue_w.resizable(False,False)
    issue_w.iconbitmap('Itzikgur-My-Seven-Books-2.ico')
    heading=tk.Label(issue_w,text='Issue',font=('segoe script',30),fg='red').pack(fill='both',)
    
    tree_view_frame=tk.Frame(issue_w,height=349,bg='white',width=1400)
    
    scroll=tk.Scrollbar(tree_view_frame,)
    scroll.place(x=1380,y=0,height=350)

    issue_table=ttk.Treeview(tree_view_frame,show='headings',height=16,yscrollcommand=scroll.set)
    
    issue_table['columns']=tuple(issue_data.columns)
    issue_table.column('Serial No',width=90)
    issue_table.column('Book No',width=120)
    issue_table.column('Book Name',anchor='center',width=450)
    issue_table.column('Student Name',anchor='center',width=150)
    issue_table.column('Student adm_no',width=100)
    issue_table.column('class\section',width=90)
    issue_table.column('Issue Date',width=130)
    issue_table.column('Return Date',width=130)
    for data in tuple(issue_data.columns):
        issue_table.heading(data,text=data,)
    item2=0
    try:
        for item2 in range(len(book)):
            issue_table.insert('',index='end',iid=item2,values=tuple(issue_data.loc[item2]))

    except:
        pass

    date=datetime.datetime.now()
    date=date.date()
    scroll.config(command=issue_table.yview)
#-------------------------------------------------------------------------------------------    
    book_n=tk.Label(issue_w,text='Book No',).place(x=50,y=450)
    book_n=tk.Entry(issue_w,width=20)
    book_n.bind('<KeyRelease>',bok_serch)
    book_n.place(x=110,y=450)
    

    book_name=tk.Label(issue_w,text='Book Name',).place(x=310,y=450)
    book_name2=tk.Entry(issue_w,width=50)
    book_name2.bind('<KeyRelease>',b_serch)
    book_name2.place(x=390,y=450)
    
    student_admno=tk.Label(issue_w,text='Admission No',).place(x=730,y=450)
    std_admno=tk.Entry(issue_w,width=30)
    std_admno.place(x=830,y=450)

    
    std_name=tk.Label(issue_w,text='Student Name',).place(x=1050,y=450)
    std_name=tk.Entry(issue_w,width=38)
    std_name.place(x=1140,y=450)

    class_=tk.Label(issue_w,text='Class & Section',).place(x=180,y=530)
    class_=tk.Entry(issue_w,width=20)
    class_.place(x=280,y=530,)
    
    issue_d=tk.Label(issue_w,text='Date of Issue',).place(x=450,y=530)
    issue_d=tk.Entry(issue_w,width=20)
    issue_d.insert(0,date)
    issue_d.place(x=530,y=530)
    
    interval=tk.Label(issue_w,text='total Days',).place(x=720,y=530)
    interval=tk.Entry(issue_w,width=20)
    interval.insert(0,7)
    interval.place(x=787,y=530)
    interval.bind('<KeyRelease>',return_datei)

    
    r_date=tk.Label(issue_w,text='Return Date',).place(x=950,y=530)
    r_date=tk.Entry(issue_w,width=20)
    r_date.insert(0,date+datetime.timedelta(int(interval.get())))
    r_date.place(x=1025,y=530)


    button3=tk.Button(issue_w,text='ISSUE',font=('arial black',10),borderwidth=2,command=add,bg='white',activebackground='green',activeforeground='white').place(x=1300,y=660)

    button4=tk.Button(issue_w,text='Received',borderwidth=2,font=('arial black',10),activeforeground='white',activebackground='red',command=retur_book_).place(x=1200,y=660)

    button5=tk.Button(issue_w,text='<-- Back ',borderwidth=2,font=('arial black',10),activeforeground='white',activebackground='red',command=lambda : main_window(issue_w.destroy())).place(x=20,y=660)

    issue_w.protocol('WM_DELETE_WINDOW',lambda : timegiven(issue_w.destroy()))


    
        
    issue_table.place(x=0,y=0,width=1380)
    tree_view_frame.pack()
    
    issue_w.mainloop()



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''                                                    ------------------------------Book window----------------------------'''
def book_window():

    main_w.destroy()
    global root,item,book_no,book_name,pages,price,type_,book_d,book_table,add_b
    
    root=tk.Tk()
    
    root.title('Running... library management system')
    root.geometry('1300x700')
    root.iconbitmap('Itzikgur-My-Seven-Books-2.ico')
    
    frame=tk.Label(root,text='Book Details',font=('segoe script',24),fg='red',padx=10)
    frame.pack()



    '                 ----------------------------------------------------------   FRAMES     -------------------------------------------------------------------------------                           '
    root1=tk.Frame(root,height=40,width=500,bg='red')
    add_b=tk.Frame(root,height=400,width=400,bg='green')

    '                 ----------------------------------------------------------  BOOK TABLE --------------------------------------------------------------------------------                           '


    scr=tk.Scrollbar(root)
    scr.pack(side='right',fill='y')

    head=tuple(book.columns)
    book_table=ttk.Treeview(root,column=head,show='headings',height=22,yscrollcommand=scr.set)

    book_table.column('Number_Of_Pages',anchor='center',width=120)
    book_table.column('Book no',anchor='center',)
    book_table.column('Book_title',anchor='center',width=370)
    book_table.column('Type',anchor='center',)
    book_table.column('Price',anchor='center',width=90)
    book_table.column('Book Detail',anchor='center',width=140)
    book_table.column('Status',anchor='center',width=150)
    for item_ in head:
        book_table.heading(item_,text=item_)

    for item in range(len(book)):
        book_table.insert('',index='end',iid=item,values=tuple(book.loc[item]))

    book_table.pack(fill='x')

    scr.config(command=book_table.yview)

    book_table.bind('<ButtonRelease-1>',upgrade)

    #frame _________________________________________________________________________________
    
    add_b=tk.Frame(root,height=330,width=1580,borderwidth=6)

    '                --------------------------------------------------------- add_book FRAME wigids ------------------------------------------------------------------------------'


    
    # Book no________________________________________________________________________________
    book_no=tk.Label(add_b,text='Book No',).place(x=60,y=30)
    book_no=tk.Entry(add_b,)
    book_no.place(x=130,y=30)
    book_no.bind('<KeyRelease>',identyfy)

    # book name _____________________________________________________________________________
    book_name=tk.Label(add_b,text='Book Name',).place(x=300,y=30)
    book_name=tk.Entry(add_b,width=72)
    book_name.place(x=380,y=30)

    #page____________________________________________________________________________________
    pages=tk.Label(add_b,text='Pages',).place(x=900,y=30)
    pages=tk.Entry(add_b,width=30)
    pages.place(x=950,y=30)

    #type __________________________________________________________________________________
    type_=tk.Label(add_b,text='Cover_Type',).place(x=60,y=90)
    type_=tk.Entry(add_b,width=40)
    type_.place(x=150,y=90)
    type_.insert(0,'Paperback')

    #price___________________________________________________________________________________
    price=tk.Label(add_b,text='Price',).place(x=440,y=90)
    price=tk.Entry(add_b,width=40)
    price.place(x=480,y=90)

    # Book Detailtable_______________________________________________________________________
    book_d=tk.Label(add_b,text='Book Type',).place(x=780,y=90)
    book_d=tk.Entry(add_b,width=45)
    book_d.place(x=860,y=90)

    # button of book table___________________________________________________________________
    button=tk.Button(add_b,text='Add',command=add_book,borderwidth=2,font=('arial black',10),activeforeground='white',activebackground='green').place(x=1200,y=130)
    button7=tk.Button(add_b,text='Upgrade',command=upgrade_book,borderwidth=2,font=('arial black',10),activeforeground='white',activebackground='orange').place(x=1100,y=130)

    button2=tk.Button(add_b,text='Delete',command=delete_book,borderwidth=2,font=('arial black',10),activeforeground='white',activebackground='red').place(x=1000,y=130)
    add_b.place(x=0,y=519)
    button6=tk.Button(add_b,text='<-- Back ',borderwidth=2,font=('arial black',10),activeforeground='white',activebackground='red',command=lambda : main_window(root.destroy())).place(x=20,y=130)

    root.protocol('WM_DELETE_WINDOW',lambda : timegiven(root.destroy()))
    #end __________________________________________________________________________________________________________________________________________________________________________________________________
    root.mainloop()

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   MAIN WINDOW   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def main_window(dest):
    global abort
    try:
        dest
        if abort==True:
            abort=False
            os.system('shutdown /a')
    except:
        pass
    global main_w,school_photo,book_photo,book_button,issue_button,entry

    main_w=tk.Tk()
    
    main_w.maxsize(1208,700)
    main_w.minsize(1208,700)
    main_w.iconbitmap('Itzikgur-My-Seven-Books-2.ico')
    main_w.title('Running... library management system')
    images=os.listdir('photo')
    imags=random.choice(images)
    background2=Image.open('photo\\'+imags)
    back=background2.resize((1208,700),Image.ANTIALIAS)
    school_photo=ImageTk.PhotoImage(back)
    main_w_background=tk.Label(main_w,image=school_photo)
    main_w_background.pack()
    
    ' =====================================================================  FRAMES  ======================================================================================= '
    
    entry=tk.Entry(main_w,width=89,fg='gray')
    entry.insert(0,'Serch Any Book',)
    entry.place(x=320,y=205,height=25)
    entry.bind('<ButtonRelease-1>',delete_)
    entry.bind('<KeyRelease>',loop)


    ' =====================================================================  BUTTON  ======================================================================================= '
    book_button = tk.Button(main_w,text = 'BOOK DETAILS',fg='black',width=32,height=7,bg='white',borderwidth=0,activebackground='gray',activeforeground='white',font=('arial black',13),command=book_window)
    book_button.place(x=7,y=520)

    issue_button = tk.Button(main_w,text = 'ISSUE BOOK',fg='black',width=34,height=7,bg='white',borderwidth=0,activebackground='gray',activeforeground='white',font=('arial black',13),command=issue_book)
    issue_button.place(x=403,y=520)

    defalter_button = tk.Button(main_w,text = 'DEFALTERS',fg='black',width=31,height=7,bg='white',borderwidth=0,activebackground='gray',activeforeground='white',font=('arial black',13),command=defalters)
    
    defalter_button.place(x=823,y=520)

    main_w.protocol('WM_DELETE_WINDOW',lambda : timegiven(main_w.destroy()))

    main_w.mainloop()
    

 
gui(c='Done (✔)')



'=============================================================================    STARTING  WINDOW   ====================================================================================================='
print('loading library management system', )
gui(25,0.00001,'All Done (✔)',0.4)
def clear(o):
    i_n.delete(0,'end')
def fp():
    global wi,i_n,otpbu
    win.destroy()
    wi=tk.Tk()
    wi.iconbitmap('Itzikgur-My-Seven-Books-2.ico')
    wi.geometry('350x250')
    wi.minsize(350,250)
    wi.maxsize(350,250)
    k=tk.Label(wi,text='Reset',font=('segoe script',35),bg='black',fg='red').pack(fill='x')
    
    frm=tk.Frame(bg='black',width=300,height=450).pack(fill='both')
    
    i_n=tk.Entry(width=54)
    i_n.insert(0,'Enter a valid id')
    i_n.bind('<ButtonRelease-1>',clear)
    i_n.place(x=7,y=150)
    otpbu=tk.Button(text='Send OTP',command=otp_generator2,activeforeground='white',activebackground='black',bg='black',fg='red')
    otpbu.place(x=144,y=226)
    wi.mainloop()
    
def otp_generator2():
    global ix
    fil=userdata[userdata.id==i_n.get()]
    ix=fil.index
    try:
        for k in fil.iloc[:,-1]:
            pass
    except:
        pass 
    try:
        if k == i_n.get():
            global _otp_
            otp_=range(10)
            _otp_=''
            for j in range(4):
                genrator=random.choice(otp_)
                _otp_+=str(genrator)
            plyer.notification.notify(title="your OTP",message=f"Your OTP to Register is {_otp_}",app_icon='python.ico')
            i_n.delete(0,'end')
            i_n.insert(0,'Enter otp')
            otpbu.config(text='verify',command=verify)
    except:
        msg.askquestion(title='#333',message='ID not found please register')
def verify():
    if _otp_==i_n.get():
        i_n.delete(0,'end')
        i_n.insert(0,'Enter New Password')
        otpbu.config(text='Submit',command=newpass)

def newpass():
    global userdata
    userdata.loc[ix,'password']=i_n.get()
    userdat=encrift3(userdata)
            
    userdat.to_csv('usersdata.csv',index=False)
    msg.showinfo(title='*****',message='Your Password upgraded')
    login(wi.destroy())
     
def otp_generator():
    global _otp
    otp_=range(10)
    _otp=''
    for j in range(4):
        genrator=random.choice(otp_)
        _otp+=str(genrator)
    plyer.notification.notify(title="your OTP",message=f"Your OTP to Register is {_otp}",app_icon='python.ico')
    otp.delete(0,'end')
    otp.insert(0,_otp)
    


def regis():
    global userdata
    try:
        _otp
    except:
        msg.askretrycancel(title='OTP not given',message='Please click on otp button to get OTP',)
        return
    if id_password.get()==id_pass_c.get():
        global lis
        lis=[id_name.get(),_id.get(),id_password.get(),_id.get()]
        if otp.get()!=_otp:
            msg.askyesnocancel(message='OTP not given')
            return
        if '' in lis:
            msg.askyesnocancel(message='Details not given')
            return
        if _id.get() not in list(userdata['id']):
            p=len(userdata)
            userdata.loc[p]=lis
            userdat=encrift3(userdata)
            
            userdat.to_csv('usersdata.csv',index=False)
            msg.showinfo(title='*****',message='Welcome to our Fammily')
            login(rot.destroy())
        else:
            msg.showwarning(message='Id alredy in use',title='####')
def register_now():
    global id_name,_id,id_password,id_pass_c,otp,rot
    win.destroy()
    rot=tk.Tk()
    rot.iconbitmap('Itzikgur-My-Seven-Books-2.ico')
    rot.geometry('500x700')
    rot.minsize(500,700)
    rot.maxsize(500,700)
    k=tk.Label(rot,text='Register Now',font=('arial black',35),bg='black',fg='red').pack(fill='x')
    frm=tk.Frame(rot,height=640,width=500,bg='black').pack(side='bottom')
    
    k=tk.Label(frm,text='Name',font=('arial black',9),bg='black',fg='red').place(x=30,y=210)
    id_name=tk.Entry(frm,width=35)
    id_name.place(x=160,y=210)

    k=tk.Label(frm,text='ID',font=('arial black',9),bg='black',fg='red').place(x=30,y=280)
    _id=tk.Entry(frm,width=50)
    _id.place(x=160,y=280)

    k=tk.Label(frm,text='Password',font=('arial black',9),bg='black',fg='red').place(x=30,y=340)
    id_password=tk.Entry(frm,width=40)
    id_password.place(x=160,y=340)

    k=tk.Label(frm,text='conform Password',font=('arial black',9),bg='black',fg='red').place(x=30,y=400)
    id_pass_c=tk.Entry(frm,width=40)
    id_pass_c.place(x=160,y=400)

    k=tk.Label(frm,text='OTP',font=('arial black',9),bg='black',fg='red').place(x=30,y=460)
    otp=tk.Entry(frm,width=40)
    otp.place(x=160,y=460)

    but=tk.Button(text='Register',command=regis,activeforeground='black',activebackground='red',fg='red',bg='black').place(x=445,y=670)
    otpbut=tk.Button(text='Send OTP',command=otp_generator,activeforeground='white',activebackground='black',bg='black',fg='red').place(x=20,y=670)
    rot.mainloop()
abort =False

shutd=0
def chk():
    global shutd,userdata,entertime,his_index
    if id_n.get() in np.array(userdata.id):
        fil=userdata[userdata.id==id_n.get()]
        if password_n.get() == np.array(fil.password):
            o=list(fil.name)
            entertime=datetime.datetime.now()
            his_index=len(history)
            history.loc[his_index]=[o[0],datetime.datetime.now().date(),datetime.datetime.now().time(),0]
            main_window(win.destroy())
        else:
            msg.askretrycancel(title='#333',message='Password is incorrect')
            shutd+=1
            shutdown()
    else:
        msg.askquestion(title='#333',message='ID not found please register')
        shutd+=1
        shutdown()
def shutdown():
    global abort
    if shutd==1:
        abort =True
        msg.showwarning(message = 'we are giving you 60 secounds to login in with correct password else system will shutdown')
        os.system('shutdown /s /t 60')
def login(des):
    des
    global id_n,password_n,win
    win=tk.Tk()
    win.geometry('300x500')
    win.minsize(300,500)
    win.maxsize(300,500)
    win.iconbitmap('Itzikgur-My-Seven-Books-2.ico')
    k=tk.Label(win,text='Login',font=('segoe script',35),bg='black',fg='red').pack(fill='x')
    
    frm=tk.Frame(bg='black',width=300,height=450).pack(fill='both')
    
    id_=tk.Label(text='Id',font=('arial black',9),fg='red',bg='black').place(x=37,y=200)
    id_n=tk.Entry(width=30,)
    id_n.place(x=90,y=200)
    
    password_=tk.Label(text='Password',font=('arial black',9),fg='red',bg='black').place(x=21,y=290)
    password_n=tk.Entry(width=30,show='*')
    password_n.place(x=89,y=290)

    login=tk.Button(text='Login',font=('arial black',9),activebackground='red',activeforeground='white',command=chk,fg='red',bg='black').place(x=240,y=400)
    register=tk.Button(text='Register now',font=('arial black',9),activebackground='red',activeforeground='white',command=register_now,fg='red',bg='black').place(x=10,y=400)
    f_password=tk.Button(text='Forgot Password',font=('arial black',9),activebackground='gray',command=fp,activeforeground='black',borderwidth=0,fg='red',bg='black',).place(x=102,y=460)
    
    win.mainloop()
login(None)
