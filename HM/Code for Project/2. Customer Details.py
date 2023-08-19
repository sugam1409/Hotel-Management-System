from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import random
from tkinter import messagebox

class Cust_Win:

    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1050x550+230+220")
             
        # ------------- Variable ---------------
        self.var_cust_ref=StringVar()
        x=random.randint(1000,9999) 
        self.var_cust_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_f_name=StringVar()
        self.var_gender=StringVar()
        self.var_address=StringVar()
        self.var_postal_code=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_contact_no=StringVar()
        self.var_email=StringVar()
            
        #-------------Title---------------
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1100,height=50)
        
        # ---------- Logo -----------------
        img2=Image.open(r"D:\project\HM\Hotel logo.jpg")
        img2=img2.resize((80,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
             
        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=80,height=50)
        
        # ------------- label frame-------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customers Details",font=("times new roman",18,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=500)
        
        # ------------label and entry------------
        # Cust Ref
        
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        
        entry_ref=Entry(labelframeleft,textvariable=self.var_cust_ref ,font=("arial",13,"bold"),width=22,state="readonly")
        entry_ref.grid(row=0,column=1)
        
        # Cust Name
        
        lbl_cust_name=Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)
        
        cust_name=Entry(labelframeleft,textvariable=self.var_cust_name ,width=22,font=("arial",13,"bold"))
        cust_name.grid(row=1,column=1)
        
        # Cust Fathername
        
        lbl_cust_f_name=Label(labelframeleft,text="Father's Name",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_f_name.grid(row=2,column=0,sticky=W)
        
        cust_f_name=Entry(labelframeleft,textvariable=self.var_f_name,width=22,font=("arial",13,"bold"))
        cust_f_name.grid(row=2,column=1)
        
        # Cust gender
        
        lbl_cust_gen=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=5,pady=6)
        lbl_cust_gen.grid(row=3,column=0,sticky=W)
        
        cust_gen=ttk.Combobox(labelframeleft,textvariable=self.var_gender,width=20,font=("arial",13,"bold"),state="readonly")
        cust_gen["value"]=("Male","Female","Other")
        cust_gen.grid(row=3,column=1)
        
        # Cust Address
        
        lbl_cust_add=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_add.grid(row=4,column=0,sticky=W)
        
        cust_add=Entry(labelframeleft,textvariable=self.var_address,width=22,font=("arial",13,"bold"))
        cust_add.grid(row=4,column=1)
        
        # Cust postalcode
        
        lbl_cust_pc=Label(labelframeleft,text="Postal Code",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_pc.grid(row=5,column=0,sticky=W)
        
        cust_pc=Entry(labelframeleft,textvariable=self.var_postal_code,width=22,font=("arial",13,"bold"))
        cust_pc.grid(row=5,column=1)
        
        # Cust ID proof type
        
        lbl_cust_id=Label(labelframeleft,text="ID Proof Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_id.grid(row=6,column=0,sticky=W)
        
        cust_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,width=20,font=("arial",13,"bold"),state="readonly")
        cust_id["value"]=("Aadhaar Card","Pan Card","Driving Licence","Passport")
        cust_id.grid(row=6,column=1)
        
        # Cust ID number
        
        lbl_cust_id_no=Label(labelframeleft,text="ID Number",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_id_no.grid(row=7,column=0,sticky=W)
        
        cust_id_no=Entry(labelframeleft,textvariable=self.var_id_number,width=22,font=("arial",13,"bold"))
        cust_id_no.grid(row=7,column=1)
        
        # Cust Mo number
        
        lbl_cust_mo_no=Label(labelframeleft,text="Conatct No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_mo_no.grid(row=8,column=0,sticky=W)
        
        cust_mo_no=Entry(labelframeleft,textvariable=self.var_contact_no,width=22,font=("arial",13,"bold"))
        cust_mo_no.grid(row=8,column=1)
        
        # Cust E-mail
        
        lbl_cust_email=Label(labelframeleft,text="E-mail",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_email.grid(row=9,column=0,sticky=W)
        
        cust_email=Entry(labelframeleft,textvariable=self.var_email,width=22,font=("arial",13,"bold"))
        cust_email.grid(row=9,column=1)
        
        # --------------button------------------
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=350,width=405,height=34)
        
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
        table_frame.place(x=449,y=50,width=660,height=490)
       
        lbl_search_by=Label(table_frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white")
        lbl_search_by.grid(row=0,column=0,sticky=W)
        
        self.search_var=StringVar()
        cust_search_by=ttk.Combobox(table_frame,textvariable=self.search_var,width=15,font=("arial",13,"bold"),state="readonly")
        cust_search_by["value"]=("Customer_Ref","Customer_Name","Contact_No")
        cust_search_by.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        cust_search=Entry(table_frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=20)
        cust_search.grid(row=0,column=2,padx=2)
        
        btn_search=Button(table_frame,command=self.search,text="Search",font=("arial",11,"bold"),bg="black",fg="gold")
        btn_search.grid(row=0,column=3,padx=1)
        
        btn_show_all=Button(table_frame,command=self.fetch_data,text="Show All",font=("arial",11,"bold"),bg="black",fg="gold")
        btn_show_all.grid(row=0,column=4,padx=1)       
        
        # --------------Show Data-table
        
        details_frame=Frame(table_frame,bd=5,relief=RIDGE)
        details_frame.place(x=5,y=50,width=578 ,height=340)
        
        scroll_x=Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(details_frame,orient=VERTICAL)
        
        self.Cust_details_Table=ttk.Treeview(details_frame,columns=("Customer Ref","Customer Name","Father's Name","Gender","Address","Postal Code","ID Proof Type","ID Number","Contact NO","E-mail"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_details_Table.xview)
        scroll_y.config(command=self.Cust_details_Table.yview)
     
        self.Cust_details_Table.heading("Customer Ref",text="Refer No")
        self.Cust_details_Table.heading("Customer Name",text="Customer Name")
        self.Cust_details_Table.heading("Father's Name",text="Father's Name")
        self.Cust_details_Table.heading("Gender",text="Gender")
        self.Cust_details_Table.heading("Address",text="Address")
        self.Cust_details_Table.heading("Postal Code",text="Postal Code")
        self.Cust_details_Table.heading("ID Proof Type",text="ID Proof Type")
        self.Cust_details_Table.heading("ID Number",text="ID Number")
        self.Cust_details_Table.heading("Contact NO",text="Contact NO")
        self.Cust_details_Table.heading("E-mail",text="E-mail")
        
        self.Cust_details_Table["show"]="headings"
        
        self.Cust_details_Table.pack(fill=BOTH,expand=1)
        self.Cust_details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

       
         
    def add_data(self):
        if self.var_contact_no.get()=="" or self.var_f_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else: 
            try:
                conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )",(
                                                                                        self.var_cust_ref.get(),
                                                                                        self.var_cust_name.get(),
                                                                                        self.var_f_name.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_postal_code.get(),
                                                                                        self.var_id_proof.get(),
                                                                                        self.var_id_number.get(),
                                                                                        self.var_contact_no.get(),
                                                                                        self.var_email.get(),
                                                                                    ))  
                conn.commit()
                self.fetch_data()
                conn.close()                   
                messagebox.showinfo("Success","Customer data added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
     
     
    def fetch_data(self):
        conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())
            for i in rows:
                self.Cust_details_Table.insert("",END,values=i)
            conn.commit()
            conn.close()
            
                 
    def get_cursor(self,event=""):
        cursor_row=self.Cust_details_Table.focus()
        content=self.Cust_details_Table.item(cursor_row)
        row=content["values"]
        
        self.var_cust_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_f_name.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_address.set(row[4]),
        self.var_postal_code.set(row[5]),
        self.var_id_proof.set(row[6]),
        self.var_id_number.set(row[7]),
        self.var_contact_no.set(row[8]),
        self.var_email.set(row[9]),
     
         
    def update(self):
        if self.var_contact_no.get=="":
            messagebox.showerror("Error","Please enter contact number",parent =self.root)
        else:
            conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Customer_Name=%s,Gender=%s,Address=%s,Postal_Code=%s,ID_Number=%s,Contact_NO=%s,Email=%s where Customer_Ref=%s",(
                                                                                                                                                                                        self.var_cust_name.get(),
                                                                                                                                                                                        # self.var_f_name.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_postal_code.get(),
                                                                                                                                                                                        # self.var_id_proof.get(),
                                                                                                                                                                                        self.var_id_number.get(),
                                                                                                                                                                                        self.var_contact_no.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_cust_ref.get()    
                                                                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer deatils has been updated successfully",parent=self.root)    
    
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer details ? ",parent=self.root)     
        if mDelete>0:
            conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from customer where Customer_Ref=%s"
            value=(self.var_cust_ref.get(),) #var_cust_ref
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
    
    def reset(self):
        # self.var_cust_ref.set(""),
        self.var_cust_name.set(""),
        self.var_f_name.set(""),
        # self.var_gender.set(""),
        self.var_address.set(""),
        self.var_postal_code.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_contact_no.set(""),
        self.var_email.set("")
        
        x=random.randint(1000,9999) 
        self.var_cust_ref.set(str(x)) 
    
    def search(self):
        conn= mysql.connector.connect(host="localhost",username="root",password="Sugam0907",database="hotel_management")
        my_cursor=conn.cursor()
        
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+"="+str(self.txt_search.get()))
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())
            for i in rows:
                self.Cust_details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
                            
if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
