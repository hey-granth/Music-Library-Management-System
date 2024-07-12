import mysql.connector as con
db=con.connect(user='root',host='localhost',password='0829')
if db.is_connected():
    print("connected")
    cur = db.cursor()
    cur.execute("create database python")
    cur.execute('use python')
    db.close()
    db = con.connect(user='root', host='localhost', password='0829', database='python')
    cur = db.cursor()
    cur.execute('create table music (MusicCode int(3) primary key,Name varchar(20)not null,Artist varchar(20),Releases varchar(20),Price int(3),Genre varchar(20)default "N/A",Quantity int(3))')
    cur.execute('create table customer_details (Code int(3) primary key,CustomerName varchar(20),PhoneNo int(10),IssueDate date,ReturnDate date)')
    print('created')
    db.close()
else:
    print('not connected')
    exit()

#to add records in customdeets
def cadd():
 
    db=con.connect(user='root',host='localhost',password='0829',database='python')
    cur=db.cursor()
    issdate=input('enter issue date')
    rtdate=input("enter return date you want to add")
    custname=input("enter name of customer date you want to add")
    custph=int(input("enter phone no. of customer you want to add"))
    custcode=int(input("enter customer code you want to add"))
    sql='insert into customer_details values(%s,%s,%s,%s,%s)'
    val=(custcode,custname,custph,issdate,rtdate)
    cur.execute(sql,val)
    db.commit()
    db.close()
    print('added')
    
#to search by code in customdeets
def searchbycode():
 
    db=con.connect(user='root',host='localhost',password='0829',database='python')
    cur=db.cursor()
    c=int(input("enter customer code you want to search"))
    sql='select * from customer_details where code=%s'
    val=(c,)
    cur.execute(sql,val)
    r=cur.fetchone()
    print(r)
    db.commit()
    db.close()
    
#to search by name in customdeets
def searchbyname():
 
    db=con.connect(user='root',host='localhost',password='0829',database='python')
    cur=db.cursor()
    n=input("enter customer name you want to search")
    sql='select * from customer_details where customername=%s'
    val=(n,)
    cur.execute(sql,val)
    r=cur.fetchone()
    print(r)
    db.commit()
    db.close()
    
#to search by phone in customdeets
def searchbyphone():
    db=con.connect(user='root',host='localhost',password='0829',database='python')
    cur=db.cursor()
    c=int(input("enter customer phone number you want to search"))
    sql='select * from customer_details where code=%s'
    val=(c,)
    cur.execute(sql,val)
    r=cur.fetchone()
    print(r)
    db.commit()
    db.close()
    
#to modify in customdeets
def modify():
    db=con.connect(host='localhost',user='root',password='0829',database='python')
    cur=db.cursor()
    code=int(input("enter customer code you want to modify details of"))
    ch=input("do you want to change name Y/N")
    if ch=='y' or ch=='Y':
        n2=input('enter new name')
        sql='update CUSTOMER_details set customer   ame=%s where code=%s'
        val=(n2,code)
        cur.execute(sql,val)
        db.commit()
    ch=input("do you want to change phone number? Y/N")
    if ch=='y' or ch=='Y':
        n2=int(input('enter new number'))
        sql='update CUSTOMER_details set phoneno=%s where code=%s'
        val=(n2,code)
        cur.execute(sql,val)
        db.commit()
    ch=input("do you want to change date of issue? Y/N")
    if ch=='y' or ch=='Y':
        n2=input('enter new date of issue')
        sql='update CUSTOMER_details set issuedate=%s where issuedate=%s'
        val=(n2,code)
        cur.execute(sql,val)
        db.commit()
    ch=input("do you want to change date of return? Y/N")
    if ch=='y' or ch=='Y':
        n2=input('enter new date of return')
        sql='update CUSTOMER_details set returndate=%s where returndate=%s'
        val=(n2,code)
        cur.execute(sql,val)
        db.commit()
    else:
        db.close()
        
#to delete customer from customdeets
def cdel():
    e=int(input("enter no. of customer you want to delete"))
    db=con.connect(user='root',host='localhost',password='granth',database='python')
    cur=db.cursor()
    sql='delete from customer_details where code=%s'
    val=(e,)
    cur.execute(sql,val)
    db.commit()
    db.close()
    
#to add records in music
def madd():
    db=con.connect(user='root',host='localhost',password='0829',database='python')
    cur=db.cursor()
    mcode=int(input("enter music code:"))
    mname=input("enter name of music:")
    artist=input("enter name of artist: ")
    genre=input("enter genre of music:")
    ryear=int(input("Enter the year of release:"))
    price=int(input("enter price of music rented:"))
    qty=int(input("enter quantity:"))
    sql='insert into MUSIC values(%s,%s,%s,%s,%s,%s,%s)'
    val=(mcode,mname,artist,ryear,price,genre,qty)
    cur.execute(sql,val)
    db.commit()
    db.close()
    print('record inserted')
    
#to delete from music
def mdel():
    e=int(input("enter no. of music name you want to delete"))
    db=con.connect(user='root',host='localhost',password='0829',database='python')
    cur=db.cursor()
    sql='delete from MUSIC where musiccode=%s'
    val=(e,)
    cur.execute(sql,val)
    db.commit()
    db.close()
    
#search by code in music
def msearchbycode():
    db=con.connect(host='localhost',user='root',password='0829',database='python')
    cur=db.cursor()
    mcode=int(input("enter music code you want to search"))
    sql='select * from MUSIC where musiccode=%s'
    val=(mcode,)
    cur.execute(sql,val)
    r=cur.fetchone()
    print(r)
    db.commit()
    db.close()
    
#search by name in music
def msearchbyname():
    db=con.connect(host='localhost',user='root',password='0829',database='python')
    cur=db.cursor()
    n=input("enter music name you want to search")
    sql='select * from MUSIC where name=%s'
    val=(n,)
    cur.execute(sql,val)
    r=cur.fetchone()
    print(r)
    db.commit()
    db.close()
    
#search by artist in music
def searchbyartist():
    b=con.connect(host='localhost',user='root',password='0829',database='python')
    cur=db.cursor()
    a=input("enter artist of songs you want to search")
    sql='select * from MUSIC where artist=%s'
    val=(a,)
    cur.execute(sql,val)
    r=cur.fetchall()
    for i in r:
        print(i)
    db.commit()
    db.close()
#to search by genre in music
def searchbygenre():
    db=con.connect(host='localhost',user='root',password='0829',database='python')
    cur=db.cursor()
    a=input("enter genre of songs you want to search")
    sql='select * from MUSIC where genre=%s'
    val=(a,)
    cur.execute(sql,val)
    r=cur.fetchall()
    for i in r:
        print(i)
    db.commit()
    db.close()
#to modify in music
def mmodify():
    db=con.connect(host='localhost',user='root',password='0829',database='python')
    cur=db.cursor()
    mcode=int(input("enter music code you want to modify details of"))
    ch=input("do you want to change name Y/N")
    if ch=='y' or ch=='Y':
        n2=input('enter new name')
        sql='update music set name=%s where musiccode=%s'
        val=(n2,mcode)
        cur.execute(sql,val)
        db.commit()
    ch=input("do you want to change artist Y/N")
    if ch=='y' or ch=='Y':
        n2=input('enter new artist')
        sql='update music set artist=%s where musiccode=%s'
        val=(n2,mcode)
        cur.execute(sql,val)
        db.commit()
    ch=input("do you want to change price Y/N")
    if ch=='y' or ch=='Y':
        n2=int(input('enter new price'))
        sql='update music set price=%s where price=%s'
        val=(n2,mcode)
        cur.execute(sql,val)
        db.commit()
    ch=input("do you want to change genre Y/N")
    if ch=='y' or ch=='Y':
        n2=input('enter new genre')
        sql='update music set genre=%s where genre=%s'
        val=(n2,mcode)
        cur.execute(sql,val)
        db.commit()
    ch=input("do you want to change qty Y/N")
    if ch=='y' or ch=='Y':
        n2=int(input('enter new qty'))
        sql='update music set quantity=%s where quantity=%s'
        val=(n2,mcode)
        cur.execute(sql,val)
        db.commit()
    ch=input("do you want to change year of release Y/N")
    if ch=='y' or ch=='Y':
        n2=int(input('enter new price'))
        sql='update music set releases=%s where releases=%s'
        val=(n2,mcode)
        cur.execute(sql,val)
        db.commit()
n='y'
while n in 'yY':
    a=int(input('''Press 1 to add records in Customer table
Press 2 to search using code in Customer table
Press 3 to search using name in Customer table
Press 4 to search using phone number in Customer table
Press 5 to modify details in Customer table
Press 6 to delete details in Customer table
Press 7 to add records in music table
Press 8 to search using code in music table
Press 9 to search using name in music table
Press 10 to search using artist in music table
Press 11 to search using genre in music table
Press 12 to modify details in music table
Press 13 to delete records in Music table'''))
    if a==1:
        cadd()
    elif a==2:
        searchbycode()
    elif a==3:
        searchbyname()
    elif a==4:
        searchbyphone()
    elif a==5:
        modify()
    elif a==6:
        cdel()
    elif a==7:
        madd()
    elif a==8:
        msearchbycode()
    elif a==9:
        msearchbyname()
    elif a==10:
        searchbyartist()
    elif a==11:
        searchbygenre()
    elif a==12:
        mmodify()
    elif a==13:
        mdel()
    else:
        print('wrong choice, try again!')
    n=input('Do you want to continue?(Y/N)?')
