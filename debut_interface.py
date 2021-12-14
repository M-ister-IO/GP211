from tkinter import *
from tkinter import ttk
import lib_students as libs

import lib_grades as libg


tkWindow = Tk()
tkWindow.geometry('1000x350')
n = ttk.Notebook(tkWindow) 

#frame 1

Frame1 = Frame(tkWindow,bg="white", borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=2, pady=2)

# frame 2 in frame 1

Frame2 = Frame(Frame1, bg="white", borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=5, pady=5)

# labelling frame 2

Label(Frame2,bg='white', text="Student").grid(row=1, column=1)
Label(Frame1,bg='white').pack(padx=250, pady=0)

#Student's first name

firstnameLabel = Label(Frame2, bg ='white', fg = 'black', text = 'First Name').grid(row = 2, column = 0)
firstname = StringVar()
firstnameEntry = Entry(Frame2, textvariable = firstname).grid (row = 2, column = 1)


#Student's last name

lastnameLabel = Label(Frame2, bg ='white', fg ='black', text = 'Last Name').grid(row = 3, column = 0)
lastname = StringVar()
lastnameEntry = Entry(Frame2, textvariable = lastname).grid(row = 3, column = 1)


#Student's ID

IDLabel = Label(Frame2, bg ='white', fg ='black', text = 'ID').grid(row = 4, column = 0)
ID = StringVar()
IDEntry = Entry(Frame2, textvariable = ID).grid(row = 4, column = 1)

#Student' sex

sexLabel = Label(Frame2, bg ='white', fg ='black', text = 'Sex').grid(row = 5, column = 0)
sex = StringVar()

button1 = Radiobutton(Frame2, bg = 'white', text="Female", variable = sex, value="F",tristatevalue=0).grid(row = 5, column = 1)
button2 = Radiobutton(Frame2, bg = 'white', text="Male", variable = sex, value="M",tristatevalue=0).grid(row = 5, column = 2)


#Student's group

groupLabel = Label(Frame2, bg ='white', fg ='black', text = 'Group').grid(row = 6, column = 0)
group = StringVar()

button3 = Radiobutton(Frame2,bg = 'white',  text="Group 1", variable = group, value="ANG1",tristatevalue=0).grid(row = 6, column = 1)
button4 = Radiobutton(Frame2, bg = 'white', text="Group 2", variable = group, value="ANG2",tristatevalue=0).grid(row = 6, column = 2)


#Student's email 

emailLabel = Label(Frame2, bg ='white', fg = 'black', text = 'Email').grid(row = 7, column = 0)
email = StringVar()
emailEntry = Entry(Frame2, textvariable = email).grid (row = 7, column = 1)


#Space between both:
Label(Frame2, bg = 'white', text="").grid(row=8, column=0)





#tableau

tv = ttk.Treeview(Frame1)
tv.column('#0', width=0, stretch=NO)
tv['columns']=('ID', 'Sex','Last Name','First Name','Email','Group')
tv.column('ID', anchor=CENTER, width=50)
tv.column('Sex', anchor=CENTER, width=40)

tv.column('Last Name', anchor=CENTER, width=130)
tv.column('First Name', anchor=CENTER, width=130)
tv.column('Email', anchor=CENTER, width=225)
tv.column('Group', anchor=CENTER, width=60)


tv.heading('ID', text='ID', anchor=CENTER)
tv.heading('Sex', text='Sex', anchor=CENTER)

tv.heading('Last Name', text='Last Name', anchor=CENTER)
tv.heading('First Name', text='First Name', anchor=CENTER)
tv.heading('Email', text='Email', anchor=CENTER)
tv.heading('Group', text='Group', anchor=CENTER)


def insertin():

    data=libs.displayStudents()
    data.pop(0)
    x=tv.get_children()
    for item in x:
        tv.delete(item)
    for i in range(len(data)):
        tv.insert(parent='', index=i, iid=i, text='', values=(data[i]))



def change():
    global sex, group, lastname, firstname, email, ID
    sex1 = sex.get()  #if i use the same name i will not be able to call them later
    lastname1 = lastname.get()
    firstname1 = firstname.get()
    email1 = email.get()
    group1 = group.get()
    ID1 = ID.get()

    libs.modifyStudent(ID1, sex1, lastname1, firstname1, email1, group1)
    insertin()



#ScrollBar

vsb = ttk.Scrollbar(tkWindow, orient="vertical", command=tv.yview)
vsb.place(x=915, y=55, height=200+10)
tv.configure(yscrollcommand=vsb.set)
tv.pack()

#Add New Button
def addNew():
    global sex,group,lastname,firstname,email
    sex1 = sex.get()

    lastname1=lastname.get()
    firstname1=firstname.get()
    email1=email.get()
    group1=group.get()

    libs.addStudent(sex1, lastname1, firstname1, email1, group1)
    insertin()


def deleting():
    global ID
    ID1=ID.get()
    libs.deleteStudent(ID1)
    insertin()

def addgrade():
    tkWindow.destroy()
    import modify_info

def report():
    tkWindow.destroy()
    import report

addnewButton = Button(Frame2, text = 'Add New', bg = 'white', fg = 'black',command=addNew).grid(row = 9, column = 0)


#Delete Button

deleteButton = Button(Frame2, text = 'Delete', bg = 'white', fg = 'black',command=deleting).grid(row = 9, column = 2)


#Update Button

updateButton = Button(Frame2, text = 'Modify', bg = 'white', fg = 'black',command=change).grid(row = 10, column = 1)


#Add Grade Button

addgradeButton = Button(Frame1, text = 'Add Grade', bg = 'white', fg = 'black',command=addgrade).pack(side=LEFT,padx = 120, pady = 3)


#School Report Button

schoolreportButton = Button(Frame1, text = 'School Report', bg = 'white', fg = 'black',command=report).pack(side=LEFT,padx = 3, pady = 3)

insertin()
def start():

    tkWindow.mainloop()


