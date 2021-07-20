import sys
print("\033[1;31;40m "+"NOTE :")
print("        WE ARE CALUCLATING GPA AND CGPA OUT OF 10")
print("        CGPA : CUMULATIVE GRADE POINT AVERAGE (caluclated for each semester)")
print("        GPA  : GRADE POINT AVERAGE (caluclated for all semesters)")
print("        MARKS SHOULD BE UPLOADED OUT OFF 100 (if you have any subjects marks out of 50 please double the value as 50*2=100 and double the credits too) :)"+"\033[0;37;40m")
sem=int(input("\033[1;35;40m"+"Enter No.of Semesters: "+"\033[0;37;40m"))
finalcgpa=[]
flag=0
for a in range(0,sem):
    print("\033[1;36;40m" +"Entering into details of Semester :",(a+1),"\033[0;37;40m")
    n=int(input("\033[1;32;40m"+"Enter no.of Subjects: "+"\033[0;37;40m"))
    marks=[]
    credit=[]
    for i in range(n):
        print("Enter the ",(i+1),end=" th subject marks: ")
        x=int(input())
        marks.append(x)
    for i in range(n):
        print("Enter the ",(i+1),end=" th subject credits: ")
        x=int(input())
        credit.append(x)
    GPA=[]
    Grade=[]
    for i in range(len(marks)):
        if(marks[i]<=100 and marks[i]>=90):
            GPA.append(10)
            Grade.append("A++")
        elif(marks[i]<90 and marks[i]>=80):
            GPA.append(9)
            Grade.append("A+")
        elif(marks[i]<80 and marks[i]>=70):
            GPA.append(8)
            Grade.append("B++")
        elif(marks[i]<70 and marks[i]>=60):
            GPA.append(7)
            Grade.append("B+")
        elif(marks[i]<60 and marks[i]>=50):
            GPA.append(6)
            Grade.append("C")
        else:
            GPA.append(0)
            Grade.append("RA")
    print("\033[1;34;40m"+"Your Grade in Respective Subjects are...."+"\033[0;37;40m")       
    for i in range(n):
        print("Grade in ",(i+1),"th Subject is :",Grade[i])
    cgpa=0
    for i in range(n):
        if(marks[i]<50):
            print("\033[1;31;40m" + "Since You have a Marks Less than 50 / Grade='RA' you are not eligible to caluclate the GPA"+"\033[0;37;40m")
            sys.exit()              
    for i in range(n):
        cgpa=cgpa+(GPA[i]*credit[i])
    finalcgpa.append(cgpa)
    print("\033[1;35;40m"+"Your CGPA is :"+"{:.2f}".format(finalcgpa[a]/sum(credit),"\033[0;37;40m"))
    flag=flag+sum(credit)
print("\033[1;32;40m"+"Your GPA is : "+("{:.2f}".format(sum(finalcgpa)/flag)+"\033[0;37;40m"))
