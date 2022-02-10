from tkinter import*
from PIL import ImageTk
from tkinter import ttk
import pymysql
from tkinter import messagebox
# from tkinter.messagebox import showinfo
from tkcalendar import DateEntry
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
		btn_login=Button(Frame_login,command=self.login_function,cursor="hand2",text="Login",font=("times new roman",15,"bold"),fg="white",
						 bg="#d77337").place(x=355,y=300,width=100,height=30)



	def login_function(self):

		if self.txt_pswd.get() == "" or self.txt_user.get() == "":
			messagebox.showerror("Error", "All fields are required", parent=self.root)
		elif self.txt_user.get()!="sunilk" or self.txt_pswd.get()!="sunil@123":
			messagebox.showerror("Error","Please enter valid Username or Password...",parent=self.root)
		elif self.txt_user.get() == "sunilk" or self.txt_pswd.get() == "sunil@123":
			self.Roll_No_var = StringVar()
			self.name_var = StringVar()
			self.email_var = StringVar()
			self.gender_var = StringVar()
			self.contact_var = StringVar()
			self.dob_var = StringVar()
			self.search_by = StringVar()
			self.search_txt = StringVar()
			self.search_txt_attendance=StringVar()
			self.fdate_var=StringVar()
			self.ldate_var=StringVar()
			self.status = StringVar()
			self.search_by_attendance=StringVar()
			self.status_var=StringVar()
			self.firstdate_var=StringVar()
			self.lastdate_var=StringVar()
			self.attendance_date_var=StringVar()
			self.attendance_roll_no_var=StringVar()
			self.attendance_name_var=StringVar()
			self.attendance_status_var=StringVar()
			self.add_attendance_date_var=StringVar()
			self.add_attendance_roll_no_var=StringVar()
			self.add_attendance_name_var=StringVar()
			self.add_attendance_status_var=StringVar()
			self.month=StringVar()
			self.name_with_roll = ""
			self.display_roll=""



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

			lbl_Date = Label(newWindow, text="D.O.B", bg="#F11C79",fg="white",font=("times new roman", 20, "bold"))
			lbl_Date.grid(row=6, column=0, pady=10, padx=20, sticky="w")
			txt_Date = DateEntry(newWindow,date_pattern="yyyy-mm-dd",textvariable=self.dob_var, font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
			txt_Date.grid(row=6, column=1, pady=10, padx=20, sticky="w")

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
			attendancebtn = Button(btn_Frame,text="For Attendence Click Here",width=20,command=self.attendance_function).grid(row=1,column=1,padx=10,pady=10)

			self.Detail_Frame = Frame(newWindow, bd=4, relief=RIDGE, bg="#F11C79")
			self.Detail_Frame.place(x=500,y=0,width=830,height=600)

			lbl_search = Label(self.Detail_Frame, text="Search By", bg="#F11C79", fg="white",font=("times new roman", 20, "bold"))
			lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

			combo_search =ttk.Combobox(self.Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
			combo_search['values']=("Roll_no","Name","Contact","Date")
			combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")

			def status_changed(event):
				# print(self.search_by.get())
				if self.search_by.get()=="Date":
					# print("True Block of Date")
					txt_Search.grid_forget()
					fdate_field.grid(row=1, column=1, pady=10, padx=10, sticky="w")
					ldate_field.grid(row=1, column=2, pady=10, padx=20, sticky="w")
				elif self.search_by.get()=="Roll_no" or self.search_by.get()=="Name" or self.search_by.get()=="Contact":
					fdate_field.grid_forget()
					ldate_field.grid_forget()
					txt_Search.grid(row=0, column=2, pady=10, padx=10, sticky="w")


			combo_search.bind('<<ComboboxSelected>>', status_changed)



			txt_Search = Entry(self.Detail_Frame, textvariable=self.search_txt, font=("times new roman", 13, "bold"), bd=5,relief=GROOVE)
			txt_Search.grid(row=0, column=2, pady=10, padx=10, sticky="w")

			fdate_field = DateEntry(self.Detail_Frame, selectmode='day', date_pattern="yyyy-mm-dd",textvariable=self.fdate_var, font=
			("times new roman", 13, "bold"), bd=5,relief=GROOVE)
			fdate_field.grid(row=1, column=1, pady=10, padx=10, sticky="w")

			ldate_field = DateEntry(self.Detail_Frame, selectmode='day', date_pattern="yyyy-mm-dd",textvariable=self.ldate_var, font=
			("times new roman", 13, "bold"), bd=5,relief=GROOVE)
			ldate_field.grid(row=1, column=2, pady=10, padx=20, sticky="w")

			searchbtn = Button(self.Detail_Frame, text="Search", width=8, command=self.search_data).grid(row=0, column=3,padx=10, pady=10)
			showallbtn = Button(self.Detail_Frame, text="Show All", width=8, command=self.fetch_data).grid(row=0, column=4,padx=10, pady=10)

			Table_Frame = Frame(self.Detail_Frame, bd=4, relief=RIDGE, bg="#F11C79")
			Table_Frame.place(x=10,y=95, width=760, height=500)

			scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
			scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

			self.Student_table = ttk.Treeview(Table_Frame,columns=("Roll", "Name", "Email", "Gender", "Contact", "DOB", "Address"),
											  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
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
		self.newWindow1 = Toplevel(root)
		self.newWindow1.title("Attendance System")
		self.newWindow1.geometry("1350x700+0+0")
		m_title = Label(self.newWindow1, text="Attendence Management", bg="#F11C79", fg="white",font=("times new roman", 30, "bold"))
		m_title.grid(row=0,columnspan=2,pady=10)
		self.newWindow1.resizable(False,False)

		lbl_roll = Label(self.newWindow1, text="Roll No.", bg="#F11C79", fg="white", font=("times new roman", 20, "bold"))
		lbl_roll.grid(row=2, column=0, pady=10, padx=20, sticky="w")
		self.txt_Roll = Entry(self.newWindow1,textvariable=self.attendance_roll_no_var, font=("times new roman", 10, "bold"), bd=5,relief=GROOVE)
		self.txt_Roll.grid(row=2, column=1, pady=10, padx=20, sticky="w")
		self.txt_Roll.configure(state='disabled')

		lbl_Name = Label(self.newWindow1, text="Name", bg="#F11C79", fg="white", font=("times new roman", 20, "bold"))
		lbl_Name.grid(row=1, column=0, pady=10, padx=20, sticky="w")
		txt_Name = Entry(self.newWindow1, textvariable=self.attendance_name_var,font=("times new roman", 10, "bold"), bd=5,relief=GROOVE)
		txt_Name.grid(row=1, column=1, pady=10, padx=20, sticky="w")
		txt_Name.configure(state='disabled')

		lbl_status = Label(self.newWindow1, text="Status", bg="#F11C79", fg="white", font=("times new roman", 20, "bold"))
		lbl_status.grid(row=3, column=0, pady=10, padx=20, sticky="w")
		combo_status = ttk.Combobox(self.newWindow1,textvariable=self.attendance_status_var ,font=("times new roman", 10, "bold"))
		combo_status['values'] = ("Present", "Absent")
		combo_status.grid(row=3, column=1, pady=10, padx=20, sticky="w")

		lbl_Date = Label(self.newWindow1, text="Date", bg="#F11C79", fg="white", font=("times new roman", 20, "bold"))
		lbl_Date.grid(row=4, column=0, pady=10, padx=20, sticky="w")
		txt_Date = DateEntry(self.newWindow1,textvariable=self.attendance_date_var, date_pattern="yyyy-mm-dd",font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
		txt_Date.grid(row=4, column=1, pady=10, padx=20, sticky="w")
		txt_Date.configure(state='disabled')

		btn_Frame1 = Frame(self.newWindow1, bd=4, relief=RIDGE, bg="#F11C79")
		btn_Frame1.place(x=10, y=520, width=420)

		Addbtn = Button(btn_Frame1, text="Add", width=9, command=self.attendance_add_function).grid(row=0, column=0, padx=10, pady=10)
		updatebtn = Button(btn_Frame1, text="Update", width=9, command=self.update_attendance).grid(row=0, column=1, padx=10, pady=10)
		deletebtn = Button(btn_Frame1, text="Delete", width=9, command=self.delete_attendance_data).grid(row=0, column=2, padx=10,pady=10)
		Clearbtn = Button(btn_Frame1, text="Clear", width=9, command=self.clear_attendance).grid(row=0, column=3, padx=10, pady=10)

		self.Detail_Frame1 = Frame(self.newWindow1, bd=4, relief=RIDGE, bg="#F11C79")
		self.Detail_Frame1.place(x=500, y=0, width=830, height=600)

		lbl_search = Label(self.Detail_Frame1, text="Search By", bg="#F11C79", fg="white",font=("times new roman", 20, "bold"))
		lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

		combo_search = ttk.Combobox(self.Detail_Frame1, textvariable=self.search_by_attendance, width=10,font=("times new roman", 13, "bold"), state='readonly')
		combo_search['values'] = ("Roll_no", "Name","Date")
		combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

		txt_Search = Entry(self.Detail_Frame1, textvariable=self.search_txt_attendance, font=("times new roman", 13, "bold"), bd=5,relief=GROOVE)
		txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

		fdate_field = DateEntry(self.Detail_Frame1, selectmode='day', date_pattern="yyyy-mm-dd",textvariable=self.firstdate_var, font=("times new roman",
																																	   13, "bold"), bd=5, relief=GROOVE)
		fdate_field.grid(row=1, column=1, pady=10, padx=10, sticky="w")

		ldate_field = DateEntry(self.Detail_Frame1, selectmode='day', date_pattern="yyyy-mm-dd",textvariable=self.lastdate_var, font=("times new roman",
																																	  13, "bold"), bd=5, relief=GROOVE)
		ldate_field.grid(row=1, column=2, pady=10, padx=20, sticky="w")

		searchbtn = Button(self.Detail_Frame1, text="Search", width=8, command=self.search_attendance_data).grid(row=0, column=3,padx=10, pady=10)
		showallbtn = Button(self.Detail_Frame1, text="Show All", width=8, command=self.fetch_attendance_data).grid(row=0, column=4,padx=10, pady=10)

		Table_Frame1 = Frame(self.Detail_Frame1, bd=4, relief=RIDGE, bg="#F11C79")
		Table_Frame1.place(x=10, y=95, width=760, height=500)

		scroll_x = Scrollbar(Table_Frame1, orient=HORIZONTAL)
		scroll_y = Scrollbar(Table_Frame1, orient=VERTICAL)


		self.Student_table1 = ttk.Treeview(Table_Frame1,columns=("Roll", "Name","Present/Absent","Date"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

		scroll_x.pack(side=BOTTOM, fill=X)
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_x.config(command=self.Student_table1.xview)
		scroll_y.config(command=self.Student_table1.yview)
		self.Student_table1.pack(fill=BOTH, expand=1)
		txt_Search2 = Entry(self.Student_table1, font=("times new roman",10, "bold"), bd=2)
		# txt_Search2.pack()

		self.Student_table1.heading("Roll", text="Roll No.")
		self.Student_table1.heading("Name", text="Name")
		self.Student_table1.heading("Present/Absent",text="Present/Absent")
		self.Student_table1.heading("Date",text="Date")

		self.Student_table1['show'] = "headings"
		self.Student_table1.column("Roll", width=100)
		self.Student_table1.column("Name", width=100)
		self.Student_table1.column("Present/Absent",width=100)
		self.Student_table1.column("Date",width=100)
		self.Student_table1.bind("<ButtonRelease-1>", self.get_attendance_cursor)


		self.fetch_attendance_data()

	def attendance_add_function(self):
		self.newWindow2 = Toplevel(root)
		self.newWindow2.title("Attendance Add System")
		self.newWindow2.geometry("1350x700+0+0")
		m_title = Label(self.newWindow2, text="Attendence Management", bg="#F11C79", fg="white",font=("times new roman", 30, "bold"))
		m_title.grid(row=0,columnspan=2,pady=10)
		self.newWindow2.resizable(False,False)

		lbl_name = Label(self.newWindow2, text="Name", bg="#F11C79", fg="white", font=("times new roman", 20, "bold"))
		lbl_name.grid(row=1, column=0, pady=10, padx=20, sticky="w")
		self.combo_name = ttk.Combobox(self.newWindow2, textvariable=self.month, font=("times new roman", 10, "bold"))
		self.combo_name.grid(row=1, column=1, pady=10, padx=20, sticky="w")

		lbl_roll = Label(self.newWindow2, text="Roll No.", bg="#F11C79", fg="white", font=("times new roman", 20, "bold"))
		lbl_roll.grid(row=2, column=0, pady=10, padx=20, sticky="w")
		self.txt_Roll = Entry(self.newWindow2,textvariable=self.add_attendance_roll_no_var, font=("times new roman", 10, "bold"), bd=5,relief=GROOVE)
		self.txt_Roll.grid(row=2, column=1, pady=10, padx=20, sticky="w")
		self.txt_Roll.configure(state='disabled')

		lbl_status = Label(self.newWindow2, text="Status", bg="#F11C79", fg="white", font=("times new roman", 20, "bold"))
		lbl_status.grid(row=4, column=0, pady=10, padx=20, sticky="w")
		combo_status = ttk.Combobox(self.newWindow2,textvariable=self.add_attendance_status_var ,font=("times new roman", 10, "bold"))
		combo_status['values'] = ("Present", "Absent")
		combo_status.grid(row=4, column=1, pady=10, padx=20, sticky="w")

		lbl_Date = Label(self.newWindow2, text="Date", bg="#F11C79", fg="white", font=("times new roman", 20, "bold"))
		lbl_Date.grid(row=3, column=0, pady=10, padx=20, sticky="w")
		txt_Date = DateEntry(self.newWindow2,textvariable=self.add_attendance_date_var, date_pattern="yyyy-mm-dd",font=("times new roman", 10,
																														"bold"), bd=5, relief=GROOVE)
		txt_Date.grid(row=3, column=1, pady=10, padx=20, sticky="w")



		def status_month(event):
			self.display_roll = self.month.get().split("_")
			# showinfo(
			# 	title='Result',
			# 	message=f'You selected {self.month.get()}! at index {self.combo_name.current()}', parent=self.newWindow2)
			print("get=", self.month.get())
			print("Display_roll=", self.display_roll[0])
			self.add_attendance_roll_no_var.set(self.display_roll[0])


		self.combo_name.bind('<<ComboboxSelected>>', status_month)


		btn_Frame2 = Frame(self.newWindow2, bd=4, relief=RIDGE, bg="#F11C79")
		btn_Frame2.place(x=10, y=520, width=420)


		Addbtn = Button(btn_Frame2, text="Add", width=9, command=self.add_attendance_student).grid(row=0, column=0, padx=10, pady=10)
		self.rana()
		name_list=self.name_with_roll.split(",")
		self.combo_name['values'] = (name_list)




	def rana(self):
		con=pymysql.connect(host="localhost",user="root",password="sunil@123",database="stmgmtpython")
		cur=con.cursor()
		cur.execute("select roll_no,name from students")
		rows=cur.fetchall()
		counter = 1

		# print("Rows value=",rows)
		for row in rows:
			# print("row value=",row)
			if counter==1:
				self.name_with_roll=str(row[0])+"_"+row[1]
			elif counter!=1:
				self.name_with_roll=self.name_with_roll+","+str(row[0])+"_"+row[1]
			counter=counter+1
		print("Name_with_roll=",self.name_with_roll)
		return self.name_with_roll





	def fetch_attendance_data(self):
		# print(" fetch data methode call")
		con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
		cur = con.cursor()
		cur.execute("select s.roll_no,s.name,a.status,a.date from students s left outer join attendance a on s.roll_no=a.roll_no")
		rows = cur.fetchall()
		# print("rows=",rows)
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

	def add_attendance_student(self):
		try:
			con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
			cur = con.cursor()
			cur.execute("insert into attendance values(%s,%s,%s,%s)", (
			self.add_attendance_roll_no_var.get(), self.add_attendance_name_var.get(),
			self.add_attendance_date_var.get(), self.add_attendance_status_var.get()))
			con.commit()
			self.fetch_data()
			self.clear()
			con.close()
			self.fetch_attendance_data()
			self.clear_add_attendance()
		except pymysql.err.IntegrityError:
			messagebox.showerror("Failed", "This Student have already data on this date", parent=self.Detail_Frame1)
		else:
			messagebox.showinfo("Success", "Attendance Added Successfully", parent=self.Detail_Frame1)
		finally:
			self.clear_add_attendance()
			self.newWindow2.destroy()


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
	def get_attendance_cursor(self,ev):
		cursor_row = self.Student_table1.focus()
		contents = self.Student_table1.item(cursor_row)
		row = contents['values']
		# print(cursor_row)
		# print(row)
		self.attendance_roll_no_var.set(row[0])
		self.attendance_name_var.set(row[1])
		self.attendance_status_var.set(row[2])
		self.attendance_date_var.set(row[3])
		print("Hello")


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
		cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(self.name_var.get(),self.email_var.get(),
																													self.gender_var.get(),self.contact_var.get(),
																													self.dob_var.get(),self.txt_Address.get('1.0',END),
																													self.Roll_No_var.get()))


		con.commit()
		self.fetch_data()
		self.clear()
		con.close()
	def update_attendance(self):
		print("update starting")
		con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
		cur = con.cursor()
		cur.execute("update attendance set status=%s where roll_no=%s and date=%s", (
		self.attendance_status_var.get(), self.attendance_roll_no_var.get(),self.attendance_date_var.get()))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()
		messagebox.showinfo("Success", "Attendance Updated Successfully", parent=self.Detail_Frame1)
		self.fetch_attendance_data()
		self.clear_attendance()


		# print("Update attendance run")



	def delete_data(self):
		# print("delete_data called")
		con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
		cur = con.cursor()
		cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
		con.commit()
		con.close()
		self.fetch_data()
		self.clear()
	def delete_attendance_data(self):
		# print("delete_attendance_data called")
		print(self.attendance_roll_no_var.get())
		print(self.attendance_date_var.get())
		con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
		cur = con.cursor()
		cur.execute("delete from attendance where roll_no=%s and date=%s",(self.attendance_roll_no_var.get(),self.attendance_date_var.get()))
		con.commit()
		con.close()
		self.fetch_attendance_data()
		self.clear_attendance()

	def search_data(self):
		# print((self.fdate_var.get()))
		# print((self.ldate_var.get()))
		if (self.search_by.get()=="Roll_no") or (self.search_by.get()=="Name") or (self.search_by.get()=="Contact"):
			con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
			cur = con.cursor()

			cur.execute("select * from students where " + str(self.search_by.get()) + " LIKE '%" + str(
				self.search_txt.get()) + "%'")
			rows = cur.fetchall()
			# print(len(rows))
			if len(rows) != 0:
				self.Student_table.delete(*self.Student_table.get_children())
				for row in rows:
					print(row)
					self.Student_table.insert('', END, values=row)
			elif len(rows)==0:
				messagebox.showinfo("Information", "No Results Founds", parent=self.Detail_Frame)

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
			elif len(rows)==0:
				messagebox.showinfo("Information", "No Results Founds", parent=self.Detail_Frame)
			con.commit()
			con.close()

	def search_attendance_data(self):
		# print("search_data called")
		if (self.search_by_attendance.get() == "Roll_no") or (self.search_by_attendance.get() == "Name"):
			con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
			cur = con.cursor()

			cur.execute("select s.roll_no,s.name,a.status from students s left outer join attendance a on s.roll_no=a.roll_no where s." + str(
				self.search_by_attendance.get()) + " LIKE '%" + str(
				self.search_txt_attendance.get()) + "%'")
			rows = cur.fetchall()
			# print(len(rows))
			if len(rows) != 0:
				self.Student_table1.delete(*self.Student_table1.get_children())
				for row in rows:
					print(row)
					self.Student_table1.insert('', END, values=row)
			elif len(rows) == 0:
				messagebox.showinfo("Information", "No Results Founds", parent=self.Detail_Frame1)

			con.commit()
			con.close()
		elif self.search_by_attendance.get() == "Date":
			con = pymysql.connect(host="localhost", user="root", password="sunil@123", database="stmgmtpython")
			cur = con.cursor()
			cur.execute("select s.roll_no,s.name,a.status from students s left outer join attendance a on s.roll_no=a.roll_no where a.date between '" + str(
				self.firstdate_var.get()) + "'and'" + str(self.lastdate_var.get()) + "%'")
			rows = cur.fetchall()
			if len(rows) != 0:
				self.Student_table1.delete(*self.Student_table1.get_children())
				for row in rows:
					self.Student_table1.insert('', END, values=row)
			elif len(rows) == 0:
				messagebox.showinfo("Information", "No Results Founds", parent=self.Detail_Frame1)
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
		self.status_var.set("")
	def clear_attendance(self):
		self.attendance_roll_no_var.set("")
		self.attendance_name_var.set("")
		self.attendance_status_var.set("")
		self.attendance_date_var.set("")
	def clear_add_attendance(self):
		self.add_attendance_roll_no_var.set("")
		self.add_attendance_name_var.set("")
		self.add_attendance_status_var.set("")
		self.add_attendance_date_var.set("")
		self.month.set("")


root=Tk()
obj=Login(root)
root.mainloop()
