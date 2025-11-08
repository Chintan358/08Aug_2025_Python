import mysql.connector as sql

con = sql.connect(
    host='localhost',
    user = 'root',
    password='root',
    port=3306,
    database ='pythonsql'
)

cursor  = con.cursor()

# cursor.execute("create database pythonsql")

# cursor.execute("create table emp(id int primary key,name varchar(20),email varchar(50))")


# cursor.execute("insert into emp values(3,'Jenil','jenil@gmail.com')")

# cursor.execute("update emp set email='abc@gmail.com' where id = 3")

# cursor.execute("delete from emp where id=3")

# con.commit()

cursor.execute("select * from emp")

data = cursor.fetchall()  

print(data)

