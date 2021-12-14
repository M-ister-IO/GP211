# -*- coding: utf-8 -*-
from lib_common import read_csv_file, write_csv_file

"""
def studentsManagement() :
    This function performs
    IN :
    OUT :
    """


def addStudent(sex,lastname,firstname,email,group) :
        """
        This function adds a student to the csv students file
        IN : list of list of strings: [["1","M","BALZAN","Thomas","thomas.balzan@ipsa.fr","ANG2"],..]
        OUT :
        """

        studentData=[sex,lastname,firstname,email,group]
        a=read_csv_file("students.csv")
        already=False
        print(a)
        for i in range(len(a)):
            if a[i][2]==studentData[1] and a[i][3]==studentData[2]:
                already=True

                print("this student already exists")

        if already==False:
            studentData=([len(a)]+studentData)
            a.append(studentData)
            write_csv_file(a,"students.csv")

        return
    
def modifyStudent(id_,sex,lastname,firstname,email,group) :
        """
        This function modifies the information of a student that is already in the csv file
        IN :list of list of strings: [["1","M","BALZAN","Thomas","thomas.balzan@ipsa.fr","ANG2"],..]
        OUT :
        """
        studentData = [id_, sex, lastname, firstname, email, group]
        a = read_csv_file("students.csv")


        for i in range(len(a)):
            print(a[i][0],studentData[0][0])
            if a[i][0]==studentData[0]:
                a[i]=studentData


        #print(a)
        write_csv_file(a,"students.csv")

        print("modificationEtudiant")
        return
    
def deleteStudent(id_) :
        """
        This function deletes a student
        IN : the id od a student
        OUT :
        """
        a = read_csv_file("students.csv")
        for i in range(len(a)):

            if a[i][0]==id_:
                a.pop(i)
                break

        write_csv_file(a, "students.csv")
        return
    
def displayStudents() :
        """
        This method is called to diplay all informations from student's file.
        Example : ID,SEX,LAST NAME,FIRST NAME,EMAIL,GROUP
        IN : no input
        OUT : no output
        """
        ##################################################
        #open and read file contents
        ##################################################
        filename = "students.csv"
        data = read_csv_file(filename)
        return data


"""
        print("****************************************************************************************************************")
        print("*                                            School Management                                                 *")
        print("****************************************************************************************************************")
        print("*   ID   *   Sex    *     Lastname    *        Firstname        *        Email adresse       *        Group    *")
        print("****************************************************************************************************************")

        for i in range(1,len(data)) :
            print("* {:<8}  * {:<8}  * {:<15}  *  {:<15}  *  {:<30} * {:>3} *" . format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))

        print("***********************************************************************************************************\n")
        
    
    ##################################################
    #
    ##################################################
    while True:
        choice = int(input("Choose from menu ( value in 1-5): \n 1- Add student \n 2- Modify student\n 3- Delete student\n 4- Display students\n 5- Exit\n\n Reply :\n"))

        if choice == 1 :
            #id_ = input("Enter student's ID\n->")
            sex = input("Enter student's sex\n->")
            lastname = input("Enter student's last name\n->")
            firstname = input("Enter student's first name\n->")
            email = input("Enter student's email\n->")
            group = input("Enter student's group\n->")
            addStudent(sex,lastname,firstname,email,group)

        if choice == 2 :
            id_ = input("Enter student's ID\n->")
            sex = input("Enter student's sex\n->")
            lastname = input("Enter student's last name\n->")
            firstname = input("Enter student's first name\n->")
            email = input("Enter student's email\n->")
            group = input("Enter student's group\n->")
            modifyStudent(id_,sex,lastname,firstname,email,group)

        if choice == 3 :
            id_ = input("Enter student's ID\n->")
            deleteStudent(id_)

        if choice == 4 :
            displayStudents()


        if choice == 5 :
            return

"""
