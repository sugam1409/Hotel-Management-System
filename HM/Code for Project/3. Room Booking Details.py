from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class Roombooking:
        def __init__(self,root):
                self.root=root
                self.root.title("Hotel Management System")
                self.root.geometry("1050x550+230+220")
                
                # Variables 
                self.var_contact=StringVar()
                self.var_check_in=StringVar()
                self.var_check_out=StringVar()
                self.var_room_type=StringVar()
                self.var_room_available=StringVar()
                self.var_meal=StringVar()
                self.var_no_of_days=StringVar()
                self.var_paid_tax=StringVar()
                self.var_actual_total=StringVar()
                self.var_total=StringVar()
                
                
                #-------------Title---------------
                lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
                lbl_title.place(x=0,y=0,width=1100,height=50)
                
                # ---------- Logo -----------------
                img2=Image.open(r"D:\project\HM\Hotel logo.jpg")
                img2=img2.resize((80,50),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)
                    
                lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
                lblimg.place(x=0,y=0,width=80,height=50)
                
                # ------------- label frame-------------
                labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room-Booking Details",font=("times new roman",18,"bold"),padx=2,)
                labelframeleft.place(x=5,y=50,width=425,height=500)
                
                
                # ------------label and entry------------
                
                # Customer contact
                lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_cust_contact.grid(row=0,column=0,sticky=W)
                entry_contact=Entry(labelframeleft,textvariable=self.var_contact,font=("arial",13,"bold"),width=16)
                entry_contact.grid(row=0,column=1,sticky=W)
                
                # Fetch data button
                
                btn_fetch_data=Button(labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
                btn_fetch_data.place(x=300,y=2.5)
                            
                # Check_in_Date
                check_in_date=Label(labelframeleft,text="Check-in Date",font=("arial",12,"bold"),padx=2,pady=6)
                check_in_date.grid(row=1,column=0,sticky=W)
                txtcheck_in_date=Entry(labelframeleft,textvariable=self.var_check_in,font=("arial",13,"bold"),width=22)
                txtcheck_in_date.grid(row=1,column=1)
                    
                # Check_out_Data
                check_out_date=Label(labelframeleft,text="Check-out Date",font=("arial",12,"bold"),padx=2,pady=6)
                check_out_date.grid(row=2,column=0,sticky=W)
                txtcheck_out_date=Entry(labelframeleft,textvariable=self.var_check_out,font=("arial",13,"bold"),width=22)
                txtcheck_out_date.grid(row=2,column=1)
                
                # Room Type
                lbl_roomType=Label(labelframeleft,text="Room-Type",font=("arial",12,"bold"),padx=5,pady=6)
                lbl_roomType.grid(row=3,column=0,sticky=W)
                
                conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("select room_type from details")
                types=my_cursor.fetchall()
                
                txt_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_room_type,width=20,font=("arial",13,"bold"),state="readonly")
                txt_roomtype["value"]=types
                txt_roomtype.current(0)
                txt_roomtype.grid(row=3,column=1)
                
                # Available Room 
                
                lbl_room_available=Label(labelframeleft,text="Available Room",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_room_available.grid(row=4,column=0,sticky=W)
                # txt_room_available=Entry(labelframeleft,textvariable=self.var_room_available,font=("arial",13,"bold"),width=22)
                # txt_room_available.grid(row=4,column=1)
                
                conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("select room_no from details")
                rows=my_cursor.fetchall()
                
                txt_room_no=ttk.Combobox(labelframeleft,textvariable=self.var_room_available,width=20,font=("arial",13,"bold"),state="readonly")
                txt_room_no["value"]=rows
                txt_room_no.current(0)
                txt_room_no.grid(row=4,column=1)
                
                # Meal
                
                lbl_meal=Label(labelframeleft,text="Meal",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_meal.grid(row=5,column=0,sticky=W)
                txt_meal=Entry(labelframeleft,textvariable=self.var_meal,font=("arial",13,"bold"),width=22)
                txt_meal.grid(row=5,column=1)
                
                # No of Days
                
                lbl_no_of_days=Label(labelframeleft,text="NO of Days",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_no_of_days.grid(row=6,column=0,sticky=W)
                txt_no_of_days=Entry(labelframeleft,textvariable=self.var_no_of_days,font=("arial",13,"bold"),width=22)
                txt_no_of_days.grid(row=6,column=1)
                
                # Paid Tax
                
                lbl_no_of_days=Label(labelframeleft,text="Paid Tax",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_no_of_days.grid(row=7,column=0,sticky=W)
                txt_no_of_days=Entry(labelframeleft,textvariable=self.var_paid_tax,font=("arial",13,"bold"),width=22)
                txt_no_of_days.grid(row=7,column=1)
                
                # Sub Total
                
                lbl_no_of_days=Label(labelframeleft,text="Sub Total",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_no_of_days.grid(row=8,column=0,sticky=W)
                txt_no_of_days=Entry(labelframeleft,textvariable=self.var_actual_total,font=("arial",13,"bold"),width=22)
                txt_no_of_days.grid(row=8,column=1)
                
                # Total Cost
                lbl_Id_number=Label(labelframeleft,text="Total Cost",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_Id_number.grid(row=9,column=0,sticky=W)
                txt_Id_number=Entry(labelframeleft,textvariable=self.var_total,font=("arial",13,"bold"),width=16)
                txt_Id_number.grid(row=9 ,column=1,sticky=W)
                
                btn_bill=Button(labelframeleft,command=self.total,text="Bill",font=("arial",11,"bold"),bg="red",fg="black",width=10)
                btn_bill.place(x=300,y=320)

                
                
                # ------------- button ------------
                
                btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
                btn_frame.place(x=5,y=350,width=405,height=34)
                
                btnadd=Button(btn_frame,command=self.add_data,text="Add",font=("arial",13,"bold"),bg="black",fg="gold",width=9)
                btnadd.grid(row=0,column=0,padx=1)
                
                btnupdate=Button(btn_frame,command=self.update,text="Update",font=("arial",13,"bold"),bg="black",fg="gold",width=9)
                btnupdate.grid(row=0,column=1,padx=1)
        
                btnDelete=Button(btn_frame,command=self.mDelete,text="Delete",font=("arial",13,"bold"),bg="black",fg="gold",width=9)
                btnDelete.grid(row=0,column=2,padx=1)
                
                btnReset=Button(btn_frame,command=self.reset,text="Reset",font=("arial",13,"bold"),bg="black",fg="gold",width=9)
                btnReset.grid(row=0,column=3,padx=1)
                
                # Right side image
                
                img3=Image.open(r"D:\project\HM\right side image.jpg")
                img3=img3.resize((300,300),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)
                    
                lblimg = Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
                lblimg.place(x=760,y=55,width=300,height=300)
                
                
            
                # --------------TABLE FRAME search ------------ 
                
                table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",13,"bold"),fg="blue")
                table_frame.place(x=449,y=240,width=660,height=260)
            
                lbl_search_by=Label(table_frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white")
                lbl_search_by.grid(row=0,column=0,sticky=W)
                
                self.search_var=StringVar()
                cust_search_by=ttk.Combobox(table_frame,textvariable=self.search_var,width=15,font=("arial",13,"bold"),state="readonly")
                cust_search_by["value"]=("Room","Contact_No")
                cust_search_by.grid(row=0,column=1,padx=2)
                
                self.txt_search=StringVar()
                cust_search=Entry(table_frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=20)
                cust_search.grid(row=0,column=2,padx=2)
                
                btn_search=Button(table_frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold")
                btn_search.grid(row=0,column=3,padx=1)
                
                btn_show_all=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold")
                btn_show_all.grid(row=0,column=4,padx=1) 
                
                
                # --------------Show Data-table
                
                details_frame=Frame(table_frame,bd=5,relief=RIDGE)
                details_frame.place(x=5,y=50,width=578 ,height=150)
                
                scroll_x=Scrollbar(details_frame,orient=HORIZONTAL)
                scroll_y=Scrollbar(details_frame,orient=VERTICAL)
                
                self.room_table=ttk.Treeview(details_frame,columns=("contact","check_in","check_out","room_type","room_available","meal","no_of_days"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
                
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                
                scroll_x.config(command=self.room_table.xview)
                scroll_y.config(command=self.room_table.yview)
            
                self.room_table.heading("contact",text="Contact No")
                self.room_table.heading("check_in",text="Check-In")
                self.room_table.heading("check_out",text="Check-Out")
                self.room_table.heading("room_type",text="Room Type")
                self.room_table.heading("room_available",text="Room No")
                self.room_table.heading("meal",text="Meal")
                self.room_table.heading("no_of_days",text="No of Days")
              
                self.room_table["show"]="headings"
                
                self.room_table.pack(fill=BOTH,expand=1)
                self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

                self.fetch_data()
                
                
        def add_data(self):
            if self.var_contact.get()=="" or self.var_check_in.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else: 
                try:
                    conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(     
                                                                                            self.var_contact.get(),
                                                                                            self.var_check_in.get(),
                                                                                            self.var_check_out.get(),
                                                                                            self.var_room_type.get(),
                                                                                            self.var_room_available.get(),
                                                                                            self.var_meal.get(),
                                                                                            self.var_no_of_days.get()
                                                                                            
                                                                                )) 
                    conn.commit()
                    self.fetch_data()
                    conn.close()                   
                    messagebox.showinfo("Success","Room Booked",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
        
        # fetch data
        def fetch_data(self):
            conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from room")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("",END,values=i)
                conn.commit()
                conn.close()
         
            
        # Get cursor 
        def get_cursor(self,event=""):
            cursor_row=self.room_table.focus()
            content=self.room_table.item(cursor_row)
            row=content["values"]
            
            self.var_contact.set(row[0]),
            self.var_check_in.set(row[1]),
            self.var_check_out.set(row[2]),
            self.var_room_type.set(row[3]),
            self.var_room_available.set(row[4]),
            self.var_meal.set(row[5]),
            self.var_no_of_days.set(row[6])
         
            
        # Update  
        def update(self):
            if self.var_contact.get()=="":
               messagebox.showerror("Error","Please enter contact number",parent =self.root)
            else:
                conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("update room set check_in=%s,check_out=%s,room_type=%s,room_available=%s,meal=%s,no_of_days=%s where contact=%s",(
                                                                                                                                                        self.var_check_in.get(),
                                                                                                                                                        self.var_check_out.get(),
                                                                                                                                                        self.var_room_type.get(),
                                                                                                                                                        self.var_room_available.get(),
                                                                                                                                                        self.var_meal.get(),
                                                                                                                                                        self.var_no_of_days.get(),
                                                                                                                                                        self.var_contact.get()                             
                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","Room deatils has been updated successfully",parent=self.root)    
    
    
        # Delete    
        def mDelete(self):
            mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer details ? ",parent=self.root)     
            if mDelete>0:
                conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                my_cursor=conn.cursor()
                query="delete from room where contact=%s"
                value=(self.var_contact.get(),) #var_cust_ref
                my_cursor.execute(query,value)
                conn.commit()
                self.fetch_data()
                conn.close()
            else:
                if not mDelete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()
    
        
        # Reset 
        def reset(self):
            self.var_contact.set("")
            self.var_check_in.set("")
            self.var_check_out.set("")
            self.var_room_type.set("")
            self.var_room_available.set("")
            self.var_meal.set("")
            self.var_no_of_days.set("")
            self.var_paid_tax.set("")
            self.var_actual_total.set("")
            self.var_total.set("")


        # search system
        def search(self):
            conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
            my_cursor=conn.cursor()
            
            my_cursor.execute("select * from room where "+str(self.search_var.get())+"="+str(self.txt_search.get()))
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table .insert("",END,values=i)
                conn.commit()
            conn.close()
           
                         
        # Total
        def total(self):
            indate=self.var_check_in.get()
            outdate=self.var_check_out.get()
            indate=datetime.strptime(indate,"%d/%m/%Y")
            outdate=datetime.strptime(outdate,"%d/%m/%Y")
            self.var_no_of_days.set(abs(outdate-indate).days)
            
            if(self.var_meal.get()=="Breakfast" and self.var_room_type.get()=="Single" ):
                q1=float(300)
                q2=float(700)
                q3=float(self.var_no_of_days.get())
                q4=float(q1+q2)
                q5=float(q3+q4)
                tax="Rs. "+str("%.2f"%((q5)*0.1))
                st="Rs. "+str("%.2f"%((q5)))
                TT="Rs. "+str("%.2f"%(q5+((q5)*0.1)))
                self.var_paid_tax.set(tax)
                self.var_actual_total.set(st)
                self.var_total.set(TT)
                
            elif(self.var_meal.get()=="Launch" and self.var_room_type.get()=="Single" ):
                q1=float(500)
                q2=float(700)
                q3=float(self.var_no_of_days.get())
                q4=float(q1+q2)
                q5=float(q3+q4)
                tax="Rs. "+str("%.2f"%((q5)*0.1))
                st="Rs. "+str("%.2f"%((q5)))
                TT="Rs. "+str("%.2f"%(q5+((q5)*0.1)))
                self.var_paid_tax.set(tax)
                self.var_actual_total.set(st)
                self.var_total.set(TT)
                
        
        
        
        
        # ------ Fetching contact
        def fetch_contact(self):
            if self.var_contact.get()=="":
               messagebox.showerror("Error","Please enter contact number",parent =self.root)
            else:
                conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select Customer_Name from customer where Contact_No=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                if row==None:
                    messagebox.showerror("Error","This no is not found",parent=self.root)
                else:
                    conn.commit()
                    conn.close()
                    
                    show_dataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                    show_dataframe.place(x=455,y=55,width=300,height=180)
                    
                    lbl_name=Label(show_dataframe,text="Name:",font=("arial",12,"bold"))
                    lbl_name.grid(row=0,column=0)
                    
                    lbl1=Label(show_dataframe,text=row,font=("arial",12,"bold"))
                    lbl1.grid(row=0,column=1)
                    
                    # gender
                    
                    conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                    my_cursor=conn.cursor()
                    query=("select Gender from customer where Contact_No=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()
                    
                    lbl_gender=Label(show_dataframe,text="Gender:",font=("arial",12,"bold"))
                    lbl_gender.grid(row=1,column=0)
                    
                    lbl2=Label(show_dataframe,text=row,font=("arial",12,"bold"))
                    lbl2.grid(row=1,column=1,sticky=W)
                    
                    # Referal no
                    
                    conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                    my_cursor=conn.cursor()
                    query=("select Customer_Ref from customer where Contact_No=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()
                    
                    lbl_gender=Label(show_dataframe,text="Refer No:",font=("arial",12,"bold"))
                    lbl_gender.grid(row=2,column=0)
                    
                    lbl2=Label(show_dataframe,text=row,font=("arial",12,"bold"))
                    lbl2.grid(row=2,column=1,sticky=W)
                    
                    # ID_Proof_Type
                    
                    conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                    my_cursor=conn.cursor()
                    query=("select ID_Proof_Type from customer where Contact_No=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()
                    
                    lbl_gender=Label(show_dataframe,text="ID_Proof_Type:",font=("arial",12,"bold"))
                    lbl_gender.grid(row=3,column=0)
                    
                    lbl2=Label(show_dataframe,text=row,font=("arial",12,"bold"))
                    lbl2.grid(row=3,column=1,sticky=W)
                    
                    # ID_Number
                    
                    conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                    my_cursor=conn.cursor()
                    query=("select ID_Number from customer where Contact_No=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()
                    
                    lbl_gender=Label(show_dataframe,text="ID_Number:",font=("arial",12,"bold"))
                    lbl_gender.grid(row=4,column=0)
                    
                    lbl2=Label(show_dataframe,text=row,font=("arial",12,"bold"))
                    lbl2.grid(row=4,column=1,sticky=W)
                    
                    # Address
                    
                    conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                    my_cursor=conn.cursor()
                    query=("select Address from customer where Contact_No=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()
                    
                    lbl_gender=Label(show_dataframe,text="Address:",font=("arial",12,"bold"))
                    lbl_gender.grid(row=5,column=0)
                    
                    lbl2=Label(show_dataframe,text=row,font=("arial",12,"bold"))
                    lbl2.grid(row=5,column=1,sticky=W)
                    
                    # Postal_Code
                    
                    conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                    my_cursor=conn.cursor()
                    query=("select Postal_Code from customer where Contact_No=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()
                    
                    lbl_gender=Label(show_dataframe,text="Postal_Code:",font=("arial",12,"bold"))
                    lbl_gender.grid(row=6,column=0)
                    
                    lbl2=Label(show_dataframe,text=row,font=("arial",12,"bold"))
                    lbl2.grid(row=6,column=1,sticky=W)
  
if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
