from tkinter import *
from tkinter import ttk
a=['A','A','A','A']
class Register:
    def __init__(self,root):
         self.root=root
         self.root.title("Login Page")
         self.root.geometry("1050x550+170+70")
         frame1=Frame(self.root,bg="white")
         frame1.place(x=30,y=20,width=1000,height=500)
         title=Label(frame1,text="Welcome",font=("times new roman",30),bg="white",fg="Blue").place(x=350,y=20)
         
         title=Label(frame1,text="Login As Faculty",font=("times new roman",20),bg="white",fg="Blue").place(x=50,y=100)
         tb=Button(frame1,text="Click to proceed",width=20,font=8,bg="pink",fg="blue",command=self.facw)
         tb.place(x=400,y=100)
         title=Label(frame1,text="Login As Student",font=("times new roman",20),bg="white",fg="Blue").place(x=50,y=140)
         studentbutton=Button(frame1,text="Click to proceed",width=20,font=8,bg="pink",fg="blue",command=self.std)
         studentbutton.place(x=400,y=140)


    def std(self):
          root3=Toplevel(root)
          self.root3=root3
          self.root3.title("Hi Student")
          self.root3.geometry("1050x550+170+70")
          frame75=Frame(self.root3,bg="white")
          frame75.place(x=30,y=20,width=1000,height=500)
          title=Label(frame75,text="Welcome Student",font=("times new roman",20),bg="white",fg="Blue").place(x=350,y=20)
                   
          title1=Label(frame75,text="Subject.",font=("times new roman",18),bg="white",fg="Blue").place(x=50,y=100)
          t_us=Entry(frame75,font=("times new roman",16),bg="white",fg="Blue",).place(x=170,y=102)                  
         #  title2=Label(frame75,text="Password",font=("times new roman",18),bg="white",fg="Blue").place(x=47,y=140)
         #  t_ps=Entry(frame75,font=("times new roman",16),bg="white",fg="Blue").place(x=170,y=142)        
          title3=Label(frame75,text="Month",font=("times new roman",18),bg="white",fg="Blue").place(x=47,y=140)         
          
          self.mon=ttk.Combobox(frame75)
          self.mon['values']=("Select","Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec")
          self.mon.place(x=173,y=142)
          self.mon.current(0)
          login_btn=Button(frame75,font=("calibri",12) ,text='Login',command=self.login1)
          login_btn.place(x=170,y=250)    

    def facw(self):
          root1=Toplevel(root)
          self.root1=root1
          self.root1.title("Hi Faculty")
          self.root1.geometry("1050x550+170+70")
          frame2=Frame(self.root1,bg="white")
          frame2.place(x=30,y=20,width=1000,height=500)
          title=Label(frame2,text="Welcome Faculty Member",font=("times new roman",20),bg="white",fg="Blue").place(x=340,y=20)
                   
          title1=Label(frame2,text="Username",font=("times new roman",18),bg="white",fg="Blue").place(x=50,y=100)
          t_us=Entry(frame2,font=("times new roman",16),bg="white",fg="Blue").place(x=170,y=102)                  
          title2=Label(frame2,text="Password",font=("times new roman",18),bg="white",fg="Blue").place(x=47,y=140)
          t_ps=Entry(frame2,font=("times new roman",16),bg="white",fg="Blue").place(x=170,y=142)        
          title3=Label(frame2,text="Month",font=("times new roman",18),bg="white",fg="Blue").place(x=52,y=180)         
          
          self.mon=ttk.Combobox(frame2)
          self.mon['values']=("Select","Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec")
          self.mon.place(x=173,y=188)
          self.mon.current(0)
          login_btn=Button(frame2,font=("calibri",13),text='Login',command=self.login)
          login_btn.place(x=170,y=250)    

    def login1(self):
          root2=Toplevel(root)
          self.root2=root2
          self.root2.title("Hi Faculty")
          self.root2.geometry("1050x550+170+70")
          frame4=Frame(self.root2,bg="white")
          frame4.place(x=30,y=20,width=1000,height=500)

          Table_frame=Frame(frame4,bg="grey",width=790,height=550)
          Table_frame.place(x=5,y=20)

          
          scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
          scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
          Student_Table=ttk.Treeview(frame4,columns=("a","b","c","d"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
          scroll_x.place(x=3,y=534,width=780)
          scroll_y.place(x=775,y=3,height=538)
          scroll_x.config(command=Student_Table.xview)
          scroll_y.config(command=Student_Table.yview)
          Student_Table.heading("a",text="Date")
          Student_Table.heading("b",text="1")
          Student_Table.heading("c",text="2")
          Student_Table.heading("d",text="3")
          Student_Table['show']='headings'
          Student_Table.column("a",width=100)
          Student_Table.column("b",width=100)
          Student_Table.column("c",width=100)
          Student_Table.column("d",width=100)
          Student_Table.place(x=10,y=85,width=770,height=400)
          
          
   

          def fetch():
           import mysql.connector
           mydb=mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="attendance"
           )
           mycursor=mydb.cursor()
           mycursor.execute("select * from Feb")
           rows=mycursor.fetchall()
           if len(rows)!=0:
            Student_Table.delete(*Student_Table.get_children())
            for row in rows:
                Student_Table.insert('',END,values=row)
                mydb.commit
            mydb.close
          fetch()
         
    def login(self):
          root2=Toplevel(root)
          self.root2=root2
          self.root2.title("Hi Faculty")
          self.root2.geometry("1400x1500+60+3")
          print(self.mon.get())
          def clear():
             date_input.delete(0,'end')
             Checkbutton1.set(0)
             Checkbutton2.set(0)
             Checkbutton3.set(0)
          def fetch():
            import mysql.connector
            mydb=mysql.connector.connect(
                host="localhost",
                username="root",
                password="",
                database="attendance"
             )
            mycursor=mydb.cursor()
            mycursor.execute("select * from attd")
            rows=mycursor.fetchall()
            if len(rows)!=0:
                 Student_Table.delete(*Student_Table.get_children())
                 for row in rows:
                      Student_Table.insert('',END,values=row)
                      mydb.commit
            mydb.close


          def submit():
                import mysql.connector
                mydb=mysql.connector.connect(
                     host="localhost",
                     username="root",
                      password="",
                     database="attendance"
                     )
                mycursor=mydb.cursor()
                if (self.mon.get()=="Jan"):
                    mycursor.execute("insert into Jan values(%s,%s,%s,%s)",(date_input.get(),
                                                           a[1],
                                                           a[2],
                                                           a[3]))

                if (self.mon.get()=="Feb"):
                    mycursor.execute("insert into Feb values(%s,%s,%s,%s)",(date_input.get(),
                                                           a[1],
                                                           a[2],
                                                           a[3]))
                                                         
                 
                if (self.mon.get()=="March"):
                    mycursor.execute("insert into March values(%s,%s,%s,%s)",(date_input.get(),
                                                           a[1],
                                                           a[2],
                                                           a[3]))                                        
                mydb.commit()
                fetch()
                clear()
                mydb.close()

          frame3=Frame(self.root2,bg="white")
          frame3.place(x=20,y=100,width=400,height=600)
          frame4=Frame(self.root2,bg="white")
          frame4.place(x=480,y=100,width=800,height=700)
          m_title=Label(frame3,text="Mark Attendance")
          m_title.place(x=90,y=20)
          m_title=Label(frame4,text="Attendance Record")
          m_title.place(x=100,y=10)
          date_label=Label(frame3,text='Enter Date')
          date_label.place(x=20,y=60)
          date_input=Entry(frame3)
          date_input.place(x=80,y=60)
          def display_unit1():
             x=Checkbutton1.get()
             if(x==1):
                a[1]='P'
             if(x!=1):
                a[1]='A'

          def display_unit2():
             x=Checkbutton2.get()
             if(x==1):
                a[2]='P'
             if(x==0):
                a[2]='A'

          def display_unit3():
             x=Checkbutton3.get()
             if(x==1):
                a[3]='P'
             if(x==0):
                a[3]='A'  

          w= Label(frame4, text ='Attendance Manager', font = "50") 
          w.pack() 

          Checkbutton1 = IntVar()  
          Checkbutton2 = IntVar()  
          Checkbutton3 = IntVar()

          Button1 = Checkbutton(frame3, text = "1", 
                      variable = Checkbutton1,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                     command=display_unit1)

          Button2 = Checkbutton(frame3, text = "2",
                      variable = Checkbutton2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                      command=display_unit2)

          Button3 = Checkbutton(frame3, text = "3", 
                      variable = Checkbutton3,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10,
                     command=display_unit3) 

          Button1.place(x=50,y=100) 
          Button2.place(x=50,y=150) 
          Button3.place(x=50,y=200)

          clean=Button(frame3,text="Clear",width=10,command=clear)
          clean.place(x=260,y=500)

          submit=Button(frame3,text="Submit",width=10,command=submit)
          submit.place(x=50,y=500) 

          Table_frame=Frame(frame4,bg="grey",width=790,height=550)
          Table_frame.place(x=5,y=70)

          scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
          scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
          Student_Table=ttk.Treeview(frame4,columns=("a","b","c","d"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
          scroll_x.place(x=3,y=534,width=780)
          scroll_y.place(x=775,y=3,height=538)
          scroll_x.config(command=Student_Table.xview)
          scroll_y.config(command=Student_Table.yview)
          Student_Table.heading("a",text="Date")
          Student_Table.heading("b",text="1")
          Student_Table.heading("c",text="2")
          Student_Table.heading("d",text="3")
          Student_Table['show']='headings'
          Student_Table.column("a",width=100)
          Student_Table.column("b",width=100)
          Student_Table.column("c",width=100)
          Student_Table.column("d",width=100)
          Student_Table.place(x=10,y=85,width=770,height=400)
          #fetch()
   

          def fetch():
           import mysql.connector
           mydb=mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="attendance"
           )
           mycursor=mydb.cursor()
           mycursor.execute("select * from Feb")
           rows=mycursor.fetchall()
           if len(rows)!=0:
            Student_Table.delete(*Student_Table.get_children())
            for row in rows:
                Student_Table.insert('',END,values=row)
                mydb.commit
            mydb.close
           print(self.mon.get())

root=Tk()
obj=Register(root)
root.mainloop()        


        
    
