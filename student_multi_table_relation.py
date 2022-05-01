import sqlite3
#creating connection between python and database
connection = sqlite3.connect("C:\\Users\\DINAKAR RAJA\\Desktop\\sqldatabase\\student_multi_table1.db")
cursor = connection.cursor()
#deleting the existing file
cursor.execute("drop table student;")
#creating a table 
sql_command = """create table student
(
 id integer auto_increment primary key,
 name varchar(20),
 age int default '18',
 gender varchar(1) default'M',
 cid int not null,
 place varchar(20)
);
"""
#executinng the command
cursor.execute(sql_command)

sql_command = """insert into student values(1,"vijay",18,'M',1,"apk"),
(2,"naethra",28,'F',2,"chennai"),(3,"vishwa",18,'M',3,"madurai"),
(4,"Ajay",20,'M',2,"Theni"),(5,"sasi",18,'F',1,"apk"),
(6,"surya",21,'M',3,"madurai");"""
#executing the command
cursor.execute(sql_command)
#saving the files
connection.commit()
cursor.execute("drop table course;")
sql_command = """create table  course
(
 sno int not null,
 cid int not null,
 course varchar(10)
);
"""
cursor.execute(sql_command)
sql_command = """insert into course values(1,1,'IT'),(2,2,'CSC'),(3,3,'ECE');"""
cursor.execute(sql_command)
connection.commit()
#deleting the existing file
cursor.execute("drop table mark;")
#creating mark table
sql_command = """create table mark
(
 id int,
 m1 int not null,
 m2 int not null,
 m3 int not null
);
"""
cursor.execute(sql_command)
#inserting the data into mark table
sql_command = """insert into mark values(1,80,82,85),
(2,78,92,85),(3,90,42,65),(4,70,92,65),(5,30,42,35),(6,70,92,65);"""
cursor.execute(sql_command)
#saving file
connection.commit()

cursor.execute("drop view report;")
#storing the select query data to report view table
sql_command = """create view report as
select student.id,student.name,course.course,mark.m1,mark.m2,mark.m3,
(mark.m1 + mark.m2 + mark.m3) as Total,round((mark.m1 + mark.m2 + mark.m3)/3,2)as Average, 
(
  case
    when mark.m1>= 35 and mark.m2>=35 and mark.m3>=35 then "pass"
    else "Fail"
  end
)as result,
(case
  when mark.m1>= 35 and mark.m2>=35 and mark.m3>=35  then
    case
     when round((mark.m1 + mark.m2 + mark.m3)/3,2)>= 90 and round((mark.m1 + mark.m2 + mark.m3)/3,2)<=100 then "A"
     when round((mark.m1 + mark.m2 + mark.m3)/3,2)>= 80 and round((mark.m1 + mark.m2 + mark.m3)/3,2)<=90 then  "B"
     else "C"
    end 
  else "NO grade"
 end) as grade from student inner join course on student.cid = course.cid
inner join mark on student.id = mark.id;"""
cursor.execute(sql_command)
#saving file
connection.commit()

#display the student details
cursor.execute("select * from report;")
desc = [i[0] for i in cursor.description]
print(desc)
print(*cursor,sep='\n')
print("done")

