import sqlite3
#creating a connection between python  and database
connection = sqlite3.connect("C:\\Users\\DINAKAR RAJA\\Desktop\\sqldatabase\\student.db")
cursor = connection.cursor()
#deleting the existing table
cursor.execute("drop table student;")
#creating a table
sql_command = """create  table student(
                 roll_no int primary key,
                 name varchar(20),
                 age int default "18",
                 gender varchar(1) default "M",
                 place varchar(20));"""
cursor.execute(sql_command)
std_count = int(input("Enter how many student:"))
#storing details in details variable
details = []
for i in range(std_count):
    #getting inputs from user
    roll_no = int(input("Enter your roll number:"))
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    gender = input("Enter gender male for ('M') or female (F):").upper()
    place = input("Enter your native place (or) which place you are coming from:").capitalize()
    #appending the details in the tuple in list data type
    details.append((roll_no,name,age,gender,place))

#inserting the student details in the student database
for i in details:
    form_str = """insert into student values('{roll_no}','{name}','{age}',
               '{gender}','{place}');"""
    sql_command = form_str.format(roll_no = i[0],name=i[1],age=i[2],gender=i[3],place=i[4])
    cursor.execute(sql_command)
cursor.execute("select * from student;")
#retrieving the field name from student table
desc = [i[0] for i in cursor.description]
print(desc)
#printing the details 
result = cursor.fetchall()
print(*result,sep='\n')
