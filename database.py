from tkinter import *
import sqlite3
en1,en2,root1,win1=0,0,0,0
#conn = sqlite3.connect('kiran.db')
#print 'open database successfull'
#conn.execute('''CREATE TABLE COMPANY(ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, EMAIL CHAR(30) NOT NULL, PWD CHAR(50) NOT NULL, SALARY INT NOT NULL);''')
#print 'Hey Table Created successfullyyyy.'
#conn.close()

def db():
    conn = sqlite3.connect('kiran.db')  
    conn.execute('''INSERT INTO COMPANY (ID ,NAME,EMAIL,PWD,SALARY) VALUES(?,?,?,?,?)''',(e1.get(),e2.get(),e3.get(),e4.get(),e5.get()))
    conn.commit()
    print 'Dear Rohith, your insertion in kiran Database created successfully'
    conn.close()
    label=Label(win,text='Created Successfully',font=('times',16,'bold'),width=16)
    label.grid(columnspan=5)
    clear()
    
def clear():
    e1.delete(0,'end')
    e2.delete(0,'end')
    e3.delete(0,'end')
    e4.delete(0,'end')
    e5.delete(0,'end')

def verify():
    global root
    global root1,en1,en2,win1
    a=en1.get()
    #print('verify')
    conn=sqlite3.connect('kiran.db')
    try:
        c=conn.execute('''SELECT id,name,email,pwd,salary from COMPANY WHERE id = '''+a)
        for row in c:
            if en2.get()==row[3]:
                e1.insert(0,row[0])
                e2.insert(0,row[1])
                e3.insert(0,row[2])
                e4.insert(0,row[3])
                e5.insert(0,row[4])
                root1.destroy()
    except:
        Label(win1,text='Enter correct Details').grid(columnspan=5)
        conn.close()
        clear()
    
def verification():
    #global root
    #root.destroy()
    global en1,en2,root1,win1
    root1=Tk()
    root1.title('Verification')
    root1.geometry('300x300+420+200')
    win1=Frame(root1)
    la1=Label(win1,text='ID')
    la1.grid(column=0,row=0)
    la2=Label(win1,text='Password')
    la2.grid(column=0,row=1)
    en1=Entry(win1)
    en1.grid(column=1,row=0)
    en2=Entry(win1)
    en2.grid(column=1,row=1)
    bt=Button(win1,text='VERIFY',width=7,command=verify)
    bt.grid(columnspan=3)
    win1.pack()
    root1.mainloop()
    
root=Tk()
root.title('Login Portal')
root.geometry('300x300+420+200')
win=Frame(root)
l1=Label(win,text='ID')
l1.grid(column=0,row=0)
l2=Label(win,text='Name')
l2.grid(column=0,row=1)
l3=Label(win,text='Email ID')
l3.grid(column=0,row=2)
l4=Label(win,text='Password')
l4.grid(column=0,row=3)
l5=Label(win,text='Salary')
l5.grid(column=0,row=4)
e1=Entry(win)
e1.grid(column=1,row=0)
e2=Entry(win)
e2.grid(column=1,row=1)
e3=Entry(win)
e3.grid(column=1,row=2)
e4=Entry(win)
e4.grid(column=1,row=3)
e5=Entry(win)
e5.grid(column=1,row=4)
btn=Button(win,text='SUBMIT',width=7,command=db)
btn.grid(columnspan=3)
ver=Button(win,text='VERIFICATION',width=10,command=verification)
ver.grid(columnspan=3)
q=Button(win,text='Quit',width=7,command=root.destroy)
q.grid(columnspan=3)


win.pack()
root.mainloop()
