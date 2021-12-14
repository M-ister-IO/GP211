from tkinter import *
from tkinter import ttk
import lib_grades as libg
gradewindow = Tk()
gradewindow.geometry('900x400')
n = ttk.Notebook(gradewindow) 

gradeframe = Frame(gradewindow,width=700, height=800, borderwidth=2, relief=GROOVE)
gradeframe.pack(side=LEFT, padx=5, pady=5)

modifyframe = Frame(gradewindow, borderwidth=2, relief=GROOVE)
modifyframe.pack(side=RIGHT, padx=0, pady=0)

Label(gradeframe, text="School Report").grid(row=0, column=1)
Label(modifyframe,text='New informations :').grid(row=0, column=1)


IDLabel = Label(modifyframe, bg ='white', fg ='black', text = 'Student ID').grid(row = 1, column = 0)
ID = StringVar()
IDEntry = Entry(modifyframe, textvariable = ID).grid(row = 1, column = 1)

yearLabel = Label(modifyframe, bg ='white', fg ='black', text = 'Year').grid(row = 2, column = 0)
year = StringVar()
yearEntry = Entry(modifyframe, textvariable = year).grid(row = 2, column = 1)

courseLabel = Label(modifyframe, bg ='white', fg ='black', text = 'Course').grid(row = 3, column = 0)
course = StringVar()
courseEntry = Entry(modifyframe, textvariable = course).grid(row = 3, column = 1)

gradeLabel = Label(modifyframe, bg ='white', fg ='black', text = 'Grade').grid(row = 4, column = 0)
grade = StringVar()
gradeEntry = Entry(modifyframe, textvariable = grade).grid(row = 4, column = 1)


def insertin():

    data=libg.displayGrades()
    print(data)
    data.pop(0)
    x=tv.get_children()
    for item in x:
        tv.delete(item)
    for i in range(len(data)):
        print(data[i])
        tv.insert(parent='', index=i, iid=i, text='', values=(data[i][1:]))
        print(len(data[i][1:-1]))





def add():
    global ID,year,grade,course
    ID1=ID.get()
    year1=year.get()
    course1=course.get()
    grade1=grade.get()

    libg.addGrade(ID1,year1,course1,grade1)
    insertin()


def mod():
    global ID,year,grade,course
    ID1=ID.get()
    year1=year.get()
    course1=course.get()
    grade1=grade.get()

    libg.modifyGrade(ID1, year1, course1, grade1)
    insertin()


def delete():
    global ID,year,grade,course
    ID1=ID.get()
    year1=year.get()
    course1=course.get()
    grade1=grade.get()

    libg.deleteGrade(ID1, year1, course1)
    insertin()


addButton = Button(modifyframe, text = 'Add', bg = 'white', fg = 'black',command=add).grid(row = 5, column = 1)
modButton = Button(modifyframe, text = 'Modify', bg = 'white', fg = 'black',command=mod).grid(row = 5, column = 2)
delButton = Button(modifyframe, text = 'Delete', bg = 'white', fg = 'black',command=delete).grid(row = 5, column = 3)

tv = ttk.Treeview(gradeframe)
tv.column('#0', width=0, stretch=NO)
tv['columns']=('Year','Students ID','Course','Grade')

tv.column('Year', anchor=CENTER, width=100)
tv.column('Students ID', anchor=CENTER, width=100)
tv.column('Course', anchor=CENTER, width=150)
tv.column('Grade', anchor=CENTER, width=150)


tv.heading('Year',text='Year', anchor=CENTER)
tv.heading('Students ID', text='Students ID', anchor=CENTER)
tv.heading('Course', text='Course', anchor=CENTER)
tv.heading('Grade', text='Grade', anchor=CENTER)

vsb = ttk.Scrollbar(gradewindow, orient="vertical", command=tv.yview)
vsb.place(x=512, y=75, height=200+10)
tv.configure(yscrollcommand=vsb.set)
tv.grid(row=1,column=1)


def start2():

    gradewindow.mainloop()