# -*- coding: utf-8 -*-
from lib_common import read_csv_file, write_csv_file

"""def gradesManagement() :
 
    This function performs
    IN :
    OUT :
    """
def displayGradesStudent(ID):
    """
            This function displays all grade info about 1 student
            IN : list of strings like [5,2020/2021,PYTHON,9.6]
            OUT :
            """
    filename = "grades.csv"
    data = read_csv_file(filename)
    a=[]
    for i in range(len(data)):

        if data[i][2] == ID:
            a.append([data[i][1],data[i][3],data[i][4]])

    return a


def addGrade(id_,year,course,grade) :
        """
        This function adds a grade to a student
        IN : list of strings like [5,2020/2021,PYTHON,9.6]
        OUT :
        """


        a = read_csv_file("grades.csv")
        already=False
        print(a)
        gradeData=[len(a)-1,year,id_,course,grade]

        for i in range(len(a)):
            print(a[i][0:-1])
            if a[i][1:-1]==gradeData[1:-1]:
                already=True
                print("grade already exists")

        if already==False:
            a.append(gradeData)
            write_csv_file(a,"grades.csv")

        return
    
def modifyGrade(id_,year,course,grade) :
        """
        This function modifies an already existing grade
        IN :list of strings like [5,2020/2021,PYTHON,9.6]
        OUT :
        """
        a = read_csv_file("grades.csv")
        gradeData=[id_,year,course,grade]
        changed=False
        for i in range(len(a)):
            if a[i][2]==id_ and a[i][1]==year and a[i][3]==course:
                changed=True
                gradeData = [i, year, id_, course, grade]

        if changed==True:
            a[gradeData[0]]=gradeData
            write_csv_file(a, "grades.csv")


        return
    
def deleteGrade(id_,year,course) :
        """
        This function deletes a grade
        IN : [5,2020/2021,PYTHON]
        OUT :
        """
        a = read_csv_file("grades.csv")
        for i in range(len(a)):
            if a[i][2]==id_ and a[i][1]==year and a[i][3]==course:
                a.pop(i)
                break

        write_csv_file(a,"grades.csv")

        return
    
def displayGrades() :
        """
        This method is called to diplay all informations from students grade's file.
        Example : ID, Year, Course, Grade
        IN : no input
        OUT : no output
        """
        ##################################################
        #open and read file contents
        ##################################################
        filename = "grades.csv"
        data = read_csv_file(filename)
        return data

"""
        print("***********************************************************************************************************")
        print("*                                          School Management                                               *")
        print("***********************************************************************************************************")
        print("*   Students ID                        *       Course                           *        Grade             *")
        print("***********************************************************************************************************")

        for i in range(1,len(data)) :
            print("* {:<40}  * {:<40}  * {:>3} *" . format(data[i][2], data[i][3], data[i][4]))

        print("***********************************************************************************************************\n")

        
    ##################################################
    #
    ##################################################
    while True:
        choice = int(input("Choose from menu ( value in 1-5): \n 1- Add grade \n 2- Modify grade\n 3- Delete grade\n 4- Display grades\n 5- Exit\n\n Response:\n"))

        if choice == 1 :
            id_ = input("Enter the student's ID\n->")
            year = input("Enter the school year\n->")
            course = input("Enter the course\n->")
            grade = input("Enter the grade\n->")
            addGrade(id_,year,course,grade)

        if choice == 2 :
            id_ = input("Enter the student's ID\n->")
            year = input("Enter the school year\n->")
            course = input("Enter the course\n->")
            grade = input("Enter the grade\n->")
            modifyGrade(id_,year,course,grade)

        if choice == 3 :
            id_ = input("Enter the student's ID\n->")
            year = input("Enter the school year\n->")
            course = input("Enter the course\n->")
            deleteGrade(id_,year,course)

        if choice == 4 :
            displayGrades() 


        if choice == 5 :
            return 

"""