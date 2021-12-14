from tkinter import *
from tkinter import ttk
import lib_grades as libg
reportwindow = Tk()
reportwindow.geometry('900x400')
n = ttk.Notebook(reportwindow)

reportframe = Frame(reportwindow,width=700, height=800, borderwidth=2, relief=GROOVE)
reportframe.pack(side=LEFT, padx=5, pady=5)

modifyframe = Frame(reportwindow, borderwidth=2, relief=GROOVE)
modifyframe.pack(side=RIGHT, padx=0, pady=0)

Label(reportframe, text="School Report").grid(row=0, column=1)
Label(modifyframe,text='New informations :').grid(row=0, column=1)


IDLabel = Label(modifyframe, bg ='white', fg ='black', text = 'Student ID').grid(row = 1, column = 0)
ID = StringVar()
IDEntry = Entry(modifyframe, textvariable = ID).grid(row = 1, column = 1)


def insertin(ID):

    data=libg.displayGradesStudent(ID)
    #print(data)
    data.pop(0)
    x=tv.get_children()
    for item in x:
        tv.delete(item)
    for i in range(len(data)):

        tv.insert(parent='', index=i, iid=i, text='', values=(data[i]))


def display():
    ID1=ID.get()
    insertin(ID1)



displayButton = Button(modifyframe, text = 'Display', bg = 'white', fg = 'black',command=display).grid(row = 5, column = 1)


tv = ttk.Treeview(reportframe)
tv.column('#0', width=0, stretch=NO)
tv['columns']=('Year','Course','Grade')

tv.column('Year', anchor=CENTER, width=100)
tv.column('Course', anchor=CENTER, width=150)
tv.column('Grade', anchor=CENTER, width=150)


tv.heading('Year',text='Year', anchor=CENTER)
tv.heading('Course', text='Course', anchor=CENTER)
tv.heading('Grade', text='Grade', anchor=CENTER)

vsb = ttk.Scrollbar(reportwindow, orient="vertical", command=tv.yview)
vsb.place(x=412, y=75, height=200+10)
tv.configure(yscrollcommand=vsb.set)
tv.grid(row=1,column=1)


def start3():

    reportwindow.mainloop()