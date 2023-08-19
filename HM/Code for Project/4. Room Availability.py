from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class DetailsRoom:
        def __init__(self,root):
                self.root=root
                self.root.title("Hotel Management System")
                self.root.geometry("1050x550+230+220")
                
                
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
                labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",18,"bold"),padx=2,)
                labelframeleft.place(x=5,y=50,width=450,height=300)
                
                # ------------label and entry------------
                
                # Floor
                lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_floor.grid(row=0,column=0,sticky=W)
                
                self.var_floor=StringVar()
                entry_floor=Entry(labelframeleft,textvariable=self.var_floor,font=("arial",13,"bold"),width=16)
                entry_floor.grid(row=0,column=1,sticky=W)
                
                # Room Number
                lbl_room_no=Label(labelframeleft,text="Room Number",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_room_no.grid(row=1,column=0,sticky=W)
                
                self.var_room_no=StringVar()
                entry_floor=Entry(labelframeleft,font=("arial",13,"bold"),textvariable=self.var_room_no,width=16)
                entry_floor.grid(row=1,column=1,sticky=W)
        
                # Room type
                lbl_room_type=Label(labelframeleft,text="Room_type",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_room_type.grid(row=2,column=0,sticky=W)
                
                self.var_room_type=StringVar()
                entry_floor=Entry(labelframeleft,font=("arial",13,"bold"),textvariable=self.var_room_type,width=16)
                entry_floor.grid(row=2,column=1,sticky=W)
                
                
                # ------------- button ------------
                
                btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
                btn_frame.place(x=5,y=150,width=405,height=34)
                
                btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
                btnadd.grid(row=0,column=0,padx=1)
                
                btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
                btnupdate.grid(row=0,column=1,padx=1)
        
                btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
                btnDelete.grid(row=0,column=2,padx=1)
                
                btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
                btnReset.grid(row=0,column=3,padx=1)
                
                # --------------TABLE FRAME search ------------ 
                
                table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",13,"bold"),fg="blue")
                table_frame.place(x=480,y=52,width=550,height=300)
                
                
                
                scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=Scrollbar(table_frame,orient=VERTICAL)
                
                self.room_table=ttk.Treeview(table_frame,columns=("floor","room_no","room_type"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
                
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                
                scroll_x.config(command=self.room_table.xview)
                scroll_y.config(command=self.room_table.yview)
                
                
                self.room_table.heading("floor",text="Floor")
                self.room_table.heading("room_no",text="Room No")
                self.room_table.heading("room_type",text="Room Type")
                  
                self.room_table["show"]="headings"
        
                self.room_table.pack(fill=BOTH,expand=1)
                self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
                self.fetch_data()
                
        def add_data(self):
            if self.var_floor.get()=="" or self.var_room_type.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else: 
                try:
                    conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into details values(%s,%s,%s)",(     
                                                                                            self.var_floor.get(),
                                                                                            self.var_room_no.get(),
                                                                                            self.var_room_type.get(),
                                                                                )) 
                    conn.commit()
                    self.fetch_data()
                    conn.close()                   
                    messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
        
        
        # fetch data
        def fetch_data(self):
            conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from details")
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
            
            self.var_floor.set(row[0]),
            self.var_room_no.set(row[1]),
            self.var_room_type.set(row[2]),
           
        
        # Update  
        def update(self):
            if self.var_floor.get()=="":
               messagebox.showerror("Error","Please enter floor number",parent =self.root)
            else:
                conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("update details set floor=%s,room_type=%s where room_no=%s",(
                                                                                            self.var_floor.get(),
                                                                                            self.var_room_type.get(),
                                                                                            self.var_room_no.get(),
                                                                                                                       
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","New room deatils has been updated successfully",parent=self.root)    
    
        
        # Delete    
        def mDelete(self):
            mDelete=messagebox.askyesno("Hotel Management System","Do you want to remove this room ? ",parent=self.root)     
            if mDelete>0:
                conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                my_cursor=conn.cursor()
                query="delete from details where room_no=%s"
                value=(self.var_room_no.get(),) #var_cust_ref
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
            self.var_floor.set("")
            self.var_room_no.set("")
            self.var_room_type.set("")         
                                        
                
if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()
