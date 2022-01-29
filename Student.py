from tkinter import*
from PIL import ImageTk
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Login:

	def __init__(self,root):
		self.root=root

		self.root.title("Login System")
		self.root.geometry("1350x700+0+0")
		self.root.resizable(False,False)

		self.bg=ImageTk.PhotoImage(file="Register_image/Hustel1.jpg")
		self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0)

		Frame_login=Frame(self.root,bg="White").place(x=150,y=50,height=340,width=525)
		title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=300,y=50)
		desc=Label(Frame_login,text="College/Institute Staff Login",font=("times new roman",15,"bold"),fg="green",bg="white").place(x=280,y=110)
		lbl_user=Label(Frame_login,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=170,y=150)
		self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
		self.txt_user.place(x=280,y=155,width=300,height=30)
		lbl_pswd=Label(Frame_login,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=170,y=210)
		self.txt_pswd=Entry(Frame_login,font=("times new roman",15),bg="lightgray",show="*")
		self.txt_pswd.place(x=280,y=215,width=300,height=30)
		btn_forgotpswd=Button(Frame_login,text="Forgot Password?",font=("times new roman",12,"bold"),bd=0,fg="#d77337",bg="white").place(x=350,y=250)
		btn_login=Button(Frame_login,command=self.login_function,cursor="hand2",text="Login",font=("times new roman",15,"bold"),fg="white",bg="#d77337").place(x=355,y=300,width=100,height=30)



	def login_function(self):

		if self.txt_pswd.get() == "" or self.txt_user.get() == "":
			messagebox.showerror("Error", "All fields are required", parent=self.root)
		# elif self.txt_user.get()!="sunilk" or self.txt_pswd.get()!="sunil@123":
		# 	messagebox.showerror("Error","Please enter valid Username or Password...",parent=self.root)
		elif self.txt_user.get() == "sunilk" or self.txt_pswd.get() == "sunil@123":
			self.Roll_No_var = StringVar()
			self.name_var = StringVar()
			self.email_var = StringVar()
			self.gender_var = StringVar()
			self.contact_var = StringVar()
			self.dob_var = StringVar()
			self.search_by = StringVar()
			self.search_txt = StringVar()
			self.fdate_var=StringVar()
			self.ldate_var=StringVar()
			self.status = StringVar()
			self.search_by_attendance=StringVar()

			newWindow = Toplevel(root)
			newWindow.title("Registration")
			newWindow.geometry("1350x700+0+0")
			m_title = Label(newWindow, text="Manage Students", bg="#F11C79", fg="white",font=("times new roman", 30, "bold"))
			m_title.grid(row=0, columnspan=2, pady=10)
			newWindow.resizable(False,False)

			lbl_roll = Label(newWindow, text="Roll No.", bg="#F11C79", fg="white", font=("times new roman", 20, "bold"))
			lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")
			self.txt_Roll = Entry(newWindow, textvariable=self.Roll_No_var, font=("times new roman", 10, "bold"), bd=5,relief=GROOVE)
			self.txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

			lbl_Name = Label(newWindow, text="Name", bg="#F11C79", fg="white", font=("times new roman", 20, "bold"))
			lbl_Name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
			txt_Name = Entry(newWindow, textvariable=self.name_var, font=("times new roman", 10, "bold"), bd=5,relief=GROOVE)
			txt_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

			lbl_Email = Label(newWindow, text="Email", bg="#F11C79", fg="white", font=("times new roman", 20, "bold"))
			lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
			txt_Email = Entry(newWindow, textvariable=self.email_var, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
			txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

			lbl_Gender = Label(newWindow, text="Gender", bg="#F11C79", fg="white", font=("times new roman", 20, "bold"))
			lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
			combo_Gender = ttk.Combobox(newWindow, textvariable=self.gender_var, font=("times new roman", 10, "bold"))
			combo_Gender['values']=("Male", "Female")
			combo_Gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

			lbl_Contact = Label(newWindow, text="Contact", bg="#F11C79", fg="white",font=("times new roman", 20, "bold"))
			lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
			txt_Contact = Entry(newWindow, textvariable=self.contact_var, font=("times new roman", 10, "bold"), bd=5,relief=GROOVE)
			txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

			lbl_Dob = Label(newWindow, text="D.O.B", bg="#F11C79",fg="white",font=("times new roman", 20, "bold"))
			lbl_Dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
			txt_Dob = Entry(newWindow, textvariable=self.dob_var, font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
			txt_Dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

			lbl_Address = Label(newWindow, text="Address", bg="#F11C79", fg="white",font=("times new roman", 20, "bold"))
			lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
			self.txt_Address = Text(newWindow, width=20, height=2, font=("times new roman", 10, "bold"), bd=5,relief=GROOVE)
			self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

			btn_Frame = Frame(newWindow, bd=4, relief=RIDGE, bg="#F11C79")
			btn_Frame.place(x=10, y=520, width=420)

			Addbtn = Button(btn_Frame, text="Add", width=9, command=self.add_student).grid(row=0, column=0, padx=10, pady=10)
			updatebtn = Button(btn_Frame, text="Update", width=9, command=self.update_data).grid(row=0, column=1,padx=10, pady=10)
			deletebtn = Button(btn_Frame, text="Delete", width=9, command=self.delete_data).grid(row=0, column=2,padx=10, pady=10)
			Clearbtn = Button(btn_Frame, text="Clear", width=9, command=self.clear).grid(row=0, column=3, padx=10,pady=10)
			attendancebtn = Button(btn_Frame,text="For Attendence Click Here",bg="black",relief=RIDGE,fg="white",command=self.attendance_function).grid(row=1,column=1)

			Detail_Frame = Frame(newWindow, bd=4, relief=RIDGE, bg="#F11C79")
			Detail_Frame.place(x=500,y=0,width=830,height=600)

			lbl_search = Label(Detail_Frame, text="Search By", bg="#F11C79", fg="white",font=("times new roman", 20, "bold"))
			lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

			combo_search =ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
			combo_search['values']=("Roll_no","Name","Contact","Date")
			combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")

			txt_Search = Entry(Detail_Frame, textvariable=self.search_txt, font=("times new roman", 13, "bold"), bd=5,relief=GROOVE)
			txt_Search.grid(row=0, column=2, pady=10, padx=10, sticky="w")

			txt_Search = Entry(Detail_Frame, textvariable=self.fdate_var, font=("times new roman", 13, "bold"), bd=5,relief=GROOVE)
			txt_Search.grid(row=1, column=1, pady=10, padx=10, sticky="w")

			txt_Search = Entry(Detail_Frame, textvariable=self.ldate_var, font=("times new roman", 13, "bold"), bd=5,relief=GROOVE)
			txt_Search.grid(row=1, column=2, pady=10, padx=20, sticky="w")

			searchbtn = Button(Detail_Frame, text="Search", width=8, command=self.search_data).grid(row=0, column=3,padx=10, pady=10)
			showallbtn = Button(Detail_Frame, text="Show All", width=8, command=self.fetch_data).grid(row=0, column=4,padx=10, pady=10)

			Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="#F11C79")
			Table_Frame.place(x=10,y=95, width=760, height=500)

			scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
			scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

			self.Student_table = ttk.Treeview(Table_Frame,columns=("Roll", "Name", "Email", "Gender", "Contact", "DOB", "Address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
			scroll_x.pack(side=BOTTOM, fill=X)
			scroll_y.pack(side=RIGHT, fill=Y)
			scroll_x.config(command=self.Student_table.xview)
			scroll_y.config(command=self.Student_table.yview)

			self.Student_table.heading("Roll", text="Roll No.")
			self.Student_table.heading("Name", text="Name")
			self.Student_table.heading("Email", text="Email")
			self.Student_table.heading("Gender", text="Gender")
			self.Student_table.heading("Contact", text="Contact")
			self.Student_table.heading("DOB", text="DOB")
			self.Student_table.heading("Address", text="Address")
			self.Student_table['show'] = "headings"
			self.Student_table.column("Roll", width=100)
			self.Student_table.column("Name", width=100)
			self.Student_table.column("Email", width=100)
			self.Student_table.column("Gender", width=100)
			self.Student_table.column("Contact", width=100)
			self.Student_table.column("DOB", width=100)
			self.Student_table.column("Address", width=100)
			self.Student_table.pack(fill=BOTH, expand=1)
			self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
			self.fetch_data()






	def attendance_function(self):
		newWindow1 = Toplevel(root)
		newWindow1.title("Attendance System")
		newWindow1.geometry("1350x700+0+0")
		m_title = Label(newWindow1, text="Attendence Management", bg="#F11C79", fg="white",font=("times new roman", 30, "bold"))
		m_title.grid(row=1,column=2,pady=10,padx=0)
		newWindow1.resizable(False,False)

		Detail_Frame1 = Frame(newWindow1, bd=4, relief=RIDGE, bg="#F11C79")
		Detail_Frame1.place(x=500, y=0, width=830, height=600)

		lbl_search = Label(Detail_Frame1, text="Search By", bg="#F11C79", fg="white",font=("times new roman", 20, "bold"))
		lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

		combo_search = ttk.Combobox(Detail_Frame1, textvariable=self.search_by_attendance, width=10,font=("times new roman", 13, "bold"), state='readonly')
		combo_search['values'] = ("Roll_no", "Name")
		combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

		txt_Search = Entry(Detail_Frame1, textvariable=self.search_txt, font=("times new roman", 13, "bold"), bd=5,relief=GROOVE)
		txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

		searchbtn = Button(Detail_Frame1, text="Search", width=8, command=self.search_attendance_data).grid(row=0, column=3,padx=10, pady=10)
		showallbtn = Button(Detail_Frame1, text="Show All", width=8, command=self.fetch_attendance_data).grid(row=0, column=4,padx=10, pady=10)

		Table_Frame1 = Frame(Detail_Frame1, bd=4, relief=RIDGE, bg="#F11C79")
		Table_Frame1.place(x=10, y=70, width=760, height=500)

		scroll_x = Scrollbar(Table_Frame1, orient=HORIZONTAL)
		scroll_y = Scrollbar(Table_Frame1, orient=VERTICAL)




		self.Student_table1 = ttk.Treeview(Table_Frame1,columns=("Roll", "Name","Present","Absent"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
		scroll_x.place(x=1000,y=15,width=50,height=50)
		scroll_y.place(x=10,y=200,width=50,height=50)
		scroll_x.config(command=self.Student_table1.xview)
		scroll_y.config(command=self.Student_table1.yview)

		r1 = ttk.Radiobutton(Table_Frame1,text="Present", variable=self.status, value='Present')
		r1.grid(row=10,column=6)
		r2 = ttk.Radiobutton(Table_Frame1,text="Absent", variable=self.status, value='Absent')
		r2.grid(row=10,column=4)

		self.Student_table1.heading("Roll", text="Roll No.")
		self.Student_table1.heading("Name", text="Name")
		self.Student_table1.heading("Present",text="Present")
		self.Student_table1.heading("Absent",text="Absent")

		self.Student_table1['show'] = "headings"
		self.Student_table1.column("Roll", width=5)
		self.Student_table1.column("Name", width=5)
		self.Student_table1.column("Present",width=5)
		self.Student_table1.column("Absent",width=10)

		self.Student_table1.place(x=11,y=72,width=750,height=490)
		self.fetch_attendance_data()




	def fetch_attendance_data(self):
		# print(" fetch data methode call")
		con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
		cur = con.cursor()
		cur.execute("select roll_no,name from students")
		rows = cur.fetchall()
		# print("rows=",rows)
		if len(rows) != 0:

			self.Student_table1.delete(*self.Student_table1.get_children())
			for row in rows:
				self.Student_table1.insert('', END, values=row)
		con.commit()
		con.close()
	def search_attendance_data(self):
		# print("search_data called")
		con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
		cur = con.cursor()
		cur.execute("select * from students where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
		rows = cur.fetchall()
		if len(rows) != 0:
			self.Student_table1.delete(*self.Student_table1.get_children())
			for row in rows:
				self.Student_table1.insert('', END, values=row)
		con.commit()
		con.close()
	def add_student(self):
		# print("add_student called")
		con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
		cur = con.cursor()
		cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (
			self.Roll_No_var.get(), self.name_var.get(), self.email_var.get(), self.gender_var.get(),
			self.contact_var.get(), self.dob_var.get(), self.txt_Address.get('1.0', END)))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()

	def fetch_data(self):
		# print(" fetch data methode call")
		con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
		cur = con.cursor()
		cur.execute("select * from students")
		rows = cur.fetchall()
		# print("rows=",rows)
		if len(rows) != 0:

			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('', END, values=row)
		con.commit()
		con.close()

	def get_cursor(self,ev):
		# print("get cursor methode call")

		cursor_row = self.Student_table.focus()
		# print("cursor row=",cursor_row)
		contents = self.Student_table.item(cursor_row)
		# print("Content=",contents)
		row = contents['values']
		self.Roll_No_var.set(row[0])
		self.name_var.set(row[1])
		self.email_var.set(row[2])
		self.gender_var.set(row[3])
		self.contact_var.set(row[4])
		self.dob_var.set(row[5])
		self.txt_Address.delete("1.0", END)
		self.txt_Address.insert(END, row[6])

	def update_data(self):
		# print("update_data called")
		con = pymysql.connect(host="localhost",user="root",password="sunil@123",database="stmgmtpython")
		cur = con.cursor()
		cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_Address.get('1.0',END),self.Roll_No_var.get()))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()


	def delete_data(self):
		# print("delete_data called")
		con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
		cur = con.cursor()
		cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
		con.commit()
		con.close()
		self.fetch_data()
		self.clear()
	def search_data(self):
		# print((self.fdate_var.get()))
		# print((self.ldate_var.get()))
		if (self.search_by.get()=="Roll_no") or (self.search_by.get()=="Name") or (self.search_by.get()=="Contact"):
			con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
			cur = con.cursor()

			cur.execute("select * from students where " + str(self.search_by.get()) + " LIKE '%" + str(
				self.search_txt.get()) + "%'")
			rows = cur.fetchall()
			if len(rows) != 0:
				self.Student_table.delete(*self.Student_table.get_children())
				for row in rows:
					self.Student_table.insert('', END, values=row)
			con.commit()
			con.close()
		elif self.search_by.get()=="Date":
			con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
			cur = con.cursor()
			cur.execute("select * from students where DOB between'"+str(self.fdate_var.get())+"'and'"+str(self.ldate_var.get())+"%'")
			rows = cur.fetchall()
			if len(rows) != 0:
				self.Student_table.delete(*self.Student_table.get_children())
				for row in rows:
					self.Student_table.insert('', END, values=row)
			con.commit()
			con.close()



	def clear(self):
		# print("clear function called")
		self.Roll_No_var.set("")
		self.name_var.set("")
		self.email_var.set("")
		self.gender_var.set("")
		self.contact_var.set("")
		self.dob_var.set("")
		self.txt_Address.delete("1.0", END)


root=Tk()
obj=Login(root)
root.mainloop()