import pymysql
db=pymysql.connect("localhost","root","","data_science")
cursor=db.cursor()

print("Hi! Welcome in My Quiz System ")
print("We Provide Following Services : ")
while(1):
    print("****************************************************************************")
    print(1," Insert Question Into Question Table ")
    print(2," Show All The Question From The Question Table ")
    print(3," Show Question By QuestionId ")
    print(4," Update The Question By QuestionId ")
    print(5," Delete The Question By QuestionId ")
    print(6," Attempt To Exam ")
    print(7," Exit ")
    print("****************************************************************************")
    n=int(input("Enter Your Choice  : "))
    if(n==1):
        que=input(" Enter Your Question :")
        opa=input(" Enter Option(A) :")
        opb=input(" Enter Option(B) :")
        opc=input(" Enter Option(C) :")
        opd=input(" Enter Option(D) :")
        cop=input(" Enter Correct Option :")
        mar=int(input("Enter Question Marks :"))
        args=(que,opa,opb,opc,opd,cop,mar)
        r=cursor.callproc("spInsertQuestion",args)
        db.commit()
        if r:
            print("Question Insertion SuccessFully")
        else:
            print("Question Insertion Failed ")
        input("Press Enter To Continue :")
        
    if(n==2):
        cursor.execute("call spShowQuestion()")
        r=cursor.fetchall()
        if(r):
            for i in r:
                    print("(",i[0],end=")")
                    print(" Qestion ",i[1])
                    print("(A) ",i[2],"(B) ",i[3],"\n(C) ",i[4],"(D) ",i[5])
        else:
            print("No Question Persent In Table")
        input("Press Enter To Continue :")
        
    if(n==3):
        qid=int(input("Enter Question Id :"))
        sql="call spShowQuestionById('%i')"%(qid)
        r=cursor.execute(sql)
        if(r>0):
            x=cursor.fetchall()
            print("Question Details : ")
            for i in x:
                print("(",qid,")",i[1])
                print("(A) ",i[2],"(B) ",i[3],"\n(C) ",i[4],"(D) ",i[5])
        else:
            print("Question Does Not Exist")
        input("Press Enter To Continue : ")
        
    if(n==4):
        qid=int(input("Enter Question Id : "))
        sql="call spShowQuestionById(%i)"%(qid)
        r=cursor.execute(sql)
        if(r>0):
            que=input(" Enter Your Question :")
            opa=input(" Enter Option(A) :")
            opb=input(" Enter Option(B) :")
            opc=input(" Enter Option(C) :")
            opd=input(" Enter Option(D) :")
            cop=input(" Enter Correct Option :")
            mar=int(input("Enter Question Marks :"))
            sql="call spUpdateQestionByQid('%i','%s','%s','%s','%s','%s','%s','%i')"%(qid,que,opa,opb,opc,opd,cop,mar)
            r=cursor.execute(sql)
            if(r):
                print("Updation Sucess Fully ")
            else:
                print("Updation Failed")
        else:
            print("Question Does Not Exist For This Qid")
        input("Press Enter To Continue : ")

    if(n==5):
        qid=int(input("Enter Question Id :"))
        sql="call spShowQuestionById('%i')"%(qid)
        r=cursor.execute(sql)
        if(r>0):
            sql="call spDeleteQuestionById('%i')"%(qid)
            r=cursor.execute(sql)
            if(r>0):
                print("Deletion SucessFully")
            else:
                print("Deletion Failed")
        else:
            print("Question Does Not Exist")
        input("Press Enter To Continue : ")
    if(n==6):
        cursor.execute("call spShowQuestion()")
        r=cursor.fetchall()
        if(r):
            point=0
            total=0
            for i in r:
                print(i[1])
                print("(A)",i[2])
                print("(B)",i[3])
                print("(C)",i[4])
                print("(D)",i[5])
                x=input("Enter Your Answere : ")
                if(x=='a'):
                    x='A'
                if(x=='b'):
                    x='B'
                if(x=='c'):
                    x='C'
                if(x=='d'):
                    x='D'
                total=total+i[7]
                if(x==i[6]):
                    print("Your Answere Is Correct ")
                    point=point+i[7]
                else:
                    print("Your Answere Is Wrong ")
                    print("My Answere ",i[6])
                x=int(input("Enter 0 To Stop OtherWise 1 To Continue "))
                if(x==0):
                    print("Your Score Is : ",point)
                    break
                else:
                    continue
        else:
            print("No Question Present in Qestion Table")

        print("Your Final Score Is Follows : ")
        print("Your Score Is : ",point)
        print("Your Percentage :",(point/total)*100)
        input("Press Enter To Continue : ")

    if(n==7):
        break
    if(n<1 or n>7):
        print("You Entered Wrong Number")
        input("Press Enter To Continue : ")
        
print("Thank You For Using My Question System ")
print("See You Again I Hope You Enjoy My Game !!!!")



'''
Delimiter $
 create procedure spInsertQuestion(
     In p_qestion varchar(1000),
     In p_optiona varchar(1000),
     In p_optionb varchar(1000),
     In p_optionc varchar(1000),
     In p_optiond varchar(1000),
     In p_correct varchar(1000),
     In p_marks int)
     begin
     Insert into question(qestion,optiona,optionb,optionc,optiond,correct,marks)
     values(p_qestion,p_optiona,p_optionb,p_optionc,p_optiond,p_correct,p_marks);
     End$
     
create procedure spShowQuestion()
begin
select * from question;
end$

create procedure spShowQuestionById(In p_id int)
Begin
Select * from question where qid=p_id;
End$

create procedure spUpdateQestionByQid(In p_id int,
 In p_qestion varchar(1000),
     In p_optiona varchar(1000),
     In p_optionb varchar(1000),
     In p_optionc varchar(1000),
     In p_optiond varchar(1000),
     In p_correct varchar(1000),
     In p_marks int)
Begin
Update question
set qestion=p_qestion,
optiona=p_optiona,
optionb=p_optionb,
optionc=p_optionc,
optiond=p_optiond,
correct=p_correct,
marks=p_marks
where qid=p_id;
End$

create procedure spDeleteQuestionById(In p_id int)
Begin
Delete from question where qid=p_id;
End$



     
     '''
