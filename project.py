import pandas as pd
import mysql.connector as c
db=c.connect(host='localhost',database='school',user='root',password='school123')
if db.is_connected():
    print('connection done')
def menu():
    print()
    print("****************************************")
    print(         " School Management Project  ")
    print()
    print()
    print("MENU")
    print("1.About")
    print("2.Show TAbles")
    print("3.Create Table student_detail")
    print("4.Describe Table student_detail")
    print("5.Show All the Records of Records from student_detail ")
    print("6.Show any no.of Records from top from student_detail")
    print("7.Show any no. of Records from bottom from student_detail")
    print("8.Show 5 records from Top from student_detail")
    print("9.Show any 5 records from Bottom from student_detail")
    print("10.Add Student Detail")
    print("11.delete from student detail")
    print("12.Update student detail table")
    print("13.Create table marks")
    print("14.Add in marks table")
    print("15.Show marks in marks table")
    print("16.Delete from Marks")
    print("17.Update marks table")
    print("18.Search by roll no.")
    print("19.Marks less than")
    print("20.Highest marks in English")
    print("21.Order by any Subject marks")
    print("22.Total marks of every student")
    print("23.Average marks of every student")
    print("********************************************************")  
    
menu()
def about():
    print("In this School Management System Project there are 2 Tables and 23 Options")
    
def show_tables():
    print("Show names of Tables in the current database school")
    mc=db.cursor()
    mc.execute("show tables")
    for x in mc:
        print(x)
            
def create_student_detail():
    mc=db.cursor()
    mc.execute("create table if not exists student_detail(admno varchar(10) primary key,name varchar(30),father_name varchar(30),mobile int(12),Address varchar(25)")
    print('table created')
    
def desc_student_detail():
    print('All records of student_detail table')
    df=pd.read_sql("desc student_detail",db)
    print(df)
    
def show_recordsstudent_detail():
    print('All records of student_detail')
    df=pd.real_sql("select * from student_detail",db)
    print(df)
    
def anynofromtop():
    print("All Records")
    df=pd.read_sql("select * from student_detail",db)
    print(df)
    df=pd.read_sql("select* from student_detail",db)
    r=int(input("Enter the number of row from the top you want to see:  "))
    print(df.head(r))
    
def anynofrombottom():
     print("All Records")
     df=pd.read_sql("select * from student_detail",db)
     print(df)
     df=pd.read_sql("select * from student_detail",df)
     r=int(input("Enter the number of rows from the bottom you want to see:  "))
     print(df.tail(r))

def fivefromtop():
    print("Top 5 records")
    df=pd.read_sql("select * from student_detail",db)
    print(df.head())
    
def fivefrombottom():
    print("Last 5 Records")
    df=pd.read_sql("select * from student_detail",db)
    print(df.tail())
     
def add_student_detail():
    print( 'Before any changes in table')
    df=pd.read_sql( "select * from student_detail",db)
    print(df)
    print('insert into student_detail new admission')
    mc=db.cursor()
    sql="insert into student_detail(admno,name,father_name,mobile,Address)"
    val=(110,'Rahul Dwivedi','Prem Dwivedi',81981215,'230,Darya Nagar')
    mc.execute(sql,val)
    print("done")
    db.commit()
    df=pd.read_sql("select * from student_details",db)
    print(df)
    print("record inserted")
     
def del_student_detail():
    print('Before any changes in table')
    df=pd.read_sql("select * from student_detail",db)
    print(df)
    print()
    print()
    mc=db.cursor()
    mc.execute("delete from student_detail where admno='123'")
    print("Record Deleted")
    db.commit()
    df=pd.read_sql("select * from student_detail",db)
    print(df)
    
def create_marks():
        mc=db.cursor()
        mc.execute("create table if not exists marks(amdno varchar(10)")    
        print('table created')
    
def add_marks():
    print('Before any changes in table')
    df=pd.read_sql("select * from marks",db)
    print(df)
    print('insert marks into new test marks')
    mc=db.cursor()
    sql="insert into marks(admno,roll,name,English,Hindi,Maths,Computer)"
    val=('107','7','Ankit Chawla','50','43','61','88')
    mc.execute(sql,val)
    print("done")
    db.commit()
    df=pd.read_sql("select * from marks",db)
    print(df)
    print("record inserted")    
    
def delete_record():
    print('Before any changes in table')
    df=pd.read_sql("select * from marks",db)
    print(db)
    print()
    print()
    mc=db.cursor()
    mc.execute("delete from marks where roll='1'")
    print("Record Deleted")
    df=pd.read_sql(" select * from marks",db)
    print(df)
    db.commit()
def update_marks():
        print('Before any changes in table')
        df=pd.read_sql("select * from marks",db)
        print(df)
        print()
        print()
        mc=db.cursor()
        mc.execute("update marks set computer=83 where roll=4")
        print("Record Updated")
        db.commit()
        df=pd.read_sql("select * from marks",db)
        print(df)
def search_byrollno():
    print('Search Student Record by entering Roll no.')
    a=float(input(" Enter Roll number       :     "))
    qry="select * from marks where Roll No=%s;"%(a,)
    df=pd.read_sql(qry,db)
    print(df)
def marks_less_than():
    print('to show details of those students who scored less than')
    ml=float(input("Enter marks to find less than that marks in English"))
    qry="select * from where English<%s;"%(ml,)
    df=pd.read_sql(qry,db)
    print(df)
def orderby_subject():
    df=pd.read_sql("select roll,name,English,Hindi,maths,Computer from marks")
    print(df)
    print("Ascending Order Marks order by English")
    mc=db.cursor()
    mc.execute("select English from marks order by English")
    print("Done")
    for x in mc:
        print(x)
def totalmarks():
    print('Total Marks of each student')
    df=pd.read_sql("select roll,name,English,Hindi,maths, Computer from marks")
    print(df)
    print()
    df[ ' total']=df['English']+df['hindi']+df['maths']+df['Computer']
    df['avg']=df['total']/4
    print(df)
    
    
    
    
    
    
       
    
opt=""
opt=int(input("enter your choice :  "))
if opt==1:
    about()  
if opt==2:
    show_tables()
elif opt==3:
     create_student_detail()  
 
elif opt==4:
     desc_student_detail()   

elif opt==5:
     show_recordsstudent_detail()
elif opt==6:
     anynofromtop()
elif opt==7:
     anynofrombottom()     
elif opt==8:
     fivefromtop()
elif opt==9:
     fivefrombottom()
elif opt==10:
     add_student_detail()
elif opt==11:
     del_student_detail()        
elif opt==12:
     create_marks()
elif opt==13:
     add_marks()
elif opt==14:
     delete_record()    
elif opt==15:
     update_marks()
elif opt==16:
     search_byrollno()
elif opt==17:
     marks_less_than()
elif opt==18:
     orderby_subject()
elif opt==19:
     totalmarks()
else:
     print('invalid option')
