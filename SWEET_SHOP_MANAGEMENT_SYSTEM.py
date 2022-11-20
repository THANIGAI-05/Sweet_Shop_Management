import mysql.connector
from datetime import datetime
con=mysql.connector.connect(host='localhost',user='ragu',passwd='password')

if con.is_connected():
    print("connected")
cur=con.cursor()
cur.execute("create database if not exists items")
cur.execute("use items")
cur.execute("create table if not exists menu(sno int,products varchar(20),cost int)")
sql="select* from menu"
cur.execute(sql)
res=cur.fetchall()
if res==[]:
    cur.execute("insert into menu values(1,'Cake',50)")
    cur.execute("insert into menu values(2,'Pastry',20)")
    cur.execute("insert into menu values(3,'Milk',60)")
    cur.execute("insert into menu values(4,'Butter',20)")
    cur.execute("insert into menu values(5,'Cheese',30)")
    con.commit()
cur.execute("create table if not exists vip(sno int,varities varchar(20))")
sql="select * from vip"
cur.execute(sql)
res=cur.fetchall()
if res==[]:
    cur.execute("insert into vip values(1,'Vannila')")
    cur.execute("insert into vip values(2,'Chocolate')")
    cur.execute("insert into vip values(3,'Strawberry')")
    cur.execute("insert into vip values(4,'Butter_scotch')")
    con.commit()
cur.execute("create table if not exists worker(Sno int,Name varchar(20),Salary int)")
sql="select* from worker"
cur.execute(sql)
res=cur.fetchall()
if res==[]:
    cur.execute("insert into worker values(1,'Prashanna',12364)")
    cur.execute("insert into worker values(2,'Hem',1234)")
    cur.execute("insert into worker values(1,'SIG',23459)")
    cur.execute("insert into worker values(1,'Srini',8987)")
    con.commit()

print(" ______________________________________________________________________________")
print("|.................... SWEET_SHOP_MANAGEMENT_SYSTEM ............................|")
print("|...............PROJECT FOR Gaxlaxy Techonlogy Services .......................|")
print(" ------------------------------------------------------------------------------")

ch=''
while ch!='N' or ch!='n':
    print("\n\n PLEASE CHOOSE \n 1 FOR ADMIN \n 2 FOR CUSTOMER \n FOR EXIT:\n")
    choice= int(input("enter your choice:"))
    if choice==3:
        break
    elif choice ==1:
        admin=input("USERNAME : ")
        password=int(input("ENTER PASSWORD : "))
        if password==1234 and admin == "ragu":
            print("\n\n**************HELLO RAGU, You logged in as Admin successfully*************")
            print(" ____________________________________________________________________________")
            print("Press 1 To Add item in the shop...")
            print("Press 2 To See items in the shop...")
            print("Press 3 To Update cost of any item...")
            print("Press 4 To Add varities of cake in the shop...")
            print("Press 5 To Add worker in the shop...")
            print("Press 6 To See workers...")
            print("Press 7 To Update of any worker...")

            c=int(input("enter your choice"))
            if c==1:
                def add():
                    sno=int(input("enter sno:"))
                    product1=input("enter product name:")
                    cost=int(input("enter the cost:"))
                    d1=(sno,product1,cost)
                    s1='insert into menu values(%s,%s,%s)'
                    cur.execute(s1,d1)
                    con.commit()
                    print('........//////ITEM ADDED SUCCESSFULLY//////..........')
                add()
            elif c==2:
                def items():
                    print("Items in the shop:")
                    sql="select * from menu"
                    cur.execute(sql)
                    res=cur.fetchall()
                    t=(['serial_no','products','cost'])
                    for serial_no,products,cost in res:
                        print(serial_no,":","\t",products,":\t\t",'cost',cost)
                items()
            elif c==3:
                def money():
                    sno=int(input("enter sno of the product"))
                    n_cost=int(input("enter the rupees to be added:"))
                    cur.execute("update menu set cost=cost+"+n_cost+" where sno="+sno+';')
                    con.commit()
                    print("TABLE AFTER UPDATION")
                    sq="select * from menu"
                    cur.execute(sq)
                    res=cur.fetchall()
                    t=(['sno','products','cost'])
                    for sno,products,cost in res:
                        print(sno,":","\t",products,":\t\t",'cost',cost)
                money()
            elif c==4:
                def variety():
                    sno=int(input("enter sno:"))
                    varieties=input("enter variety:")
                    d2=(sno,varieties)
                    s2='insert into vip values(%s,%s)'
                    cur.execute(s2,d2)
                    con.commit()
                variety()
            elif c==5:
                def ad():
                    sno=int(input("enter sno:"))
                    emp=input("enter name:")
                    salary=int(input("enter the salary:"))
                    dx=(sno,emp,salary)
                    sy='insert into worker values (%s,%s,%s)'
                    cur.execute(sy,dx)
                    con.commit()
                    print('........//////WORKER ADDED SUCCESSFULLY//////..........')
                ad()

            elif ch==6:
                def workers():
                    print("Workers in the shop:")
                    sql="select * from worker "
                    cur.execute (sql)
                    res=cur.fetchall()
                    t=(['serial_no','name','salary'])
                    for serial_no,name,salary in res:
                        print(serial_no,":","\t",name,":",'cost',salary)
                workers()
            elif ch==7:
                def up():
                    print("choose 1 to increase the salary")
                    print("choose 2 to decrease:")
                    name=input("Enter the name of EMPLOYEE:")
                    n_salary=input("Enter the Rupees to be added")
                    sig=int(input("enter choice(1/2):"))
                    if sig==1:
    
                        cur.execute("update worker set salary=salary+"+n_salary+" where name="+name+"")
                        con.commit()
                        print("TABLE AFTER UPDATING")
                        sq="select * from worker"
                        cur.execute(sq)
                        res=cur.fetchall()
                        t=(['sno','name','salary'])
                        for sno,name,salary in res:
                            print(sno,":","\t",name,":","\t",salary)
                    elif sig==2:
                        cur.execute("update worker set salary =salary-"+n_salary+" where name="+name+"")
                        con.commit()
                        print("TABLE AFTER UPDATING")
                        sql="select * from worker"
                        cur.execute(sql)
                        res=cur.fetchall()
                        t=(['sno','name','salary'])
                        for sno,name,salary in res:
                            print(sno,":","\t",name,":","\t",salary)
                    
                    else:
                        print("SORRY... YOU HAVE ENTERED THE WRONG INPUT FROM 1 to 7")
            
                        print("\t\t\t\t\t\t\t********WRONG PASSWORD*****************")
                up()
    elif choice==2:
              name=input("Enter your name:")
              phone=int(input("Enter your phone number"))
              print('Press 1 to see the MENU',sep='....')
              print('Press 2 to oder an item')
              c=int(input('enter your choice'))
              if c==1:
                  def items():
                      print("Items in the shop:")
                      sql="select * from menu "
                      cur.execute(sql)
                      res=cur.fetchall()
                      t=(['serial_no','products','cost'])
                      for serial_no,products,cost in res:
                          print(serial_no,":","\t",products,":\t\t",'cost',cost)
                  items()
              elif c==2:
                  print("What to do you want to order?")
                  sql="select * from menu "
                  cur.execute(sql)
                  res=cur.fetchall()
                  t=(['serial_no','products','cost'])
                  for serial_no,products,cost in res:
                      print(serial_no,":","\t",products,":\t\t",'cost',cost)
                  sql="select sno from menu"
                  cur.execute(sql)
                  res=cur.fetchall()
                  print(res)
                  l=[]
                  for i in range(len(res)):
                      l.append(res[i][0])
                      

                      d=int(input("enter your serial no of the item to buy:"))
                      if d==1:
                          def items():
                              print("Which cake do you want?")
                              kl="select * from vip"
                              cur.execute(k1)
                              srh=cur.fetchall()
                              f=(['sno','varieities'])
                              for sno,varieties in srh:
                                  print(sno,":","\t\t",varieties)
                              print("Choose which cake do you want?")
                              ck=int(input("enter choice"))
                              if ck==1:
                                  print("How much Quantity of Vannila cake do you want?")
                                  qty=int(input("Enter Qty."))
                                  print("You have successfully ordered your cake!!!|t:")
                                  cur.execute ("select * from menu where products='cake'")
                                  for i in cur:
                                      c=i[2]
                                      con.commit()
                                  print("Total amount:",qty*c)
                                  print ("\n")
                                  print(".........................................................................................")
                                  print("YOUR BILL ")
                                  print("_________________________________________________________________________________________")
                                  print("Costumer's name :",name)
                                  print("Contact no,:",phone)
                                  print("Cake type: Vannila")
                                  print("No of cakes:",qty)
                                  print("Total amount:",qty*c)
                                  print("@@@@@@@@@@@@@@@@@@@ THANK_YOU FOR ORDERING THE ITEM @@@@@@@@@@@@@@@@@@@@@@")
                                  print("\t\t\t\t\t\t\t\t\t\t Date:",datetime.now())
                              elif ck==2:
                                  print("How much Quantity of chocolate cake do you want?")
                                  qty=int(input("Enter Qty."))
                                  print("You have successfully ordered your cake!!!|t:")
                                  cur.execute ("select * from menu where products='cake'")
                                  for i in cur:
                                      L=i[2]
                                      con.commit()
                                  print("Total amount:",qty*L)
                                  print ("\n")
                                  print(".........................................................................................")
                                  print("YOUR BILL ")
                                  print("_________________________________________________________________________________________")
                                  print("Costumer's name :",name)
                                  print("Contact no,:",phone)
                                  print("Cake type: Chocolate")
                                  print("No of cakes:",qty)
                                  print("Total amount:",qty*L)
                                  print("@@@@@@@@@@@@@@@@@@@ THANK_YOU FOR ORDERING THE ITEM @@@@@@@@@@@@@@@@@@@@@@")
                                  print("\t\t\t\t\t\t\t\t\t\t Date:",datetime.now())
                              elif ck==3:
                                  print("How much Quantity of Strawberry cake do you want?")
                                  qty=int(input("Enter Qty."))
                                  print("You have successfully ordered your cake!!!|t:")
                                  cur.execute ("select * from menu where products='cake'")
                                  for i in cur:
                                      N=i[2]
                                      con.commit()
                                  print("Total amount:",qty*N)
                                  print ("\n")
                                  print(".........................................................................................")
                                  print("YOUR BILL ")
                                  print("_________________________________________________________________________________________")
                                  print("Costumer's name :",name)
                                  print("Contact no,:",phone)
                                  print("Cake type: Strawberry")
                                  print("No of cakes:",qty)
                                  print("Total amount:",qty*N)
                                  print("@@@@@@@@@@@@@@@@@@@ THANK_YOU FOR ORDERING THE ITEM @@@@@@@@@@@@@@@@@@@@@@")
                                  print("\t\t\t\t\t\t\t\t\t\t Date:",datetime.now())
                              elif ck==4:
                                  print("How much Quantity of Butter_scotch cake do you want?")
                                  qty=int(input("Enter Qty."))
                                  print("You have successfully ordered your cake!!!|t:")
                                  cur.execute ("select * from menu where products='cake'")
                                  for i in cur:
                                      M=i[2]
                                      con.commit()
                                  print("Total amount:",qty*M)
                                  print ("\n")
                                  print(".........................................................................................")
                                  print("YOUR BILL ")
                                  print("_________________________________________________________________________________________")
                                  print("Costumer's name :",name)
                                  print("Contact no,:",phone)
                                  print("Cake type: Butter_scotch")
                                  print("No of cakes:",qty)
                                  print("Total amount:",qty*M)
                                  print("@@@@@@@@@@@@@@@@@@@ THANK_YOU FOR ORDERING THE ITEM @@@@@@@@@@@@@@@@@@@@@@")
                                  print("\t\t\t\t\t\t\t\t\t\t Date:",datetime.now())
                          items()
                      elif d==2:
                          print("How much pastry do you want:")
                          past=int(input("enter your choice:"))
                          print("You have successfully ordered",past,"pastry")
                          cur.execute("select * from menu where products='pastry'")
                          for i in cur:
                              c=i[2]
                          print("Total amount:",past*c)
                          print ("\n")
                          print(".........................................................................................")
                          print("YOUR BILL ")
                          print("_________________________________________________________________________________________")
                          print("Costumer's name :",name)
                          print("Contact no,:",phone)
                          print("No of pastry:",past)
                          print("Total amount:",past*c)
                          print("@@@@@@@@@@@@@@@@@@@ THANK_YOU FOR ORDERING THE ITEM @@@@@@@@@@@@@@@@@@@@@@")
                          print("\t\t\t\t\t\t\t\t\t\t Date:",datetime.now())
                      elif d==3:
                          print("How much milk do you want:")
                          mlk=int(input("enter your choice:"))
                          print("You have successfully ordered",mlk,"L of milk")
                          cur.execute("select * from menu where products='milk'")
                          for i in cur:
                              c=i[2]
                          print("Total amount:",mlk*c)
                          print ("\n")
                          print(".........................................................................................")
                          print("YOUR BILL ")
                          print("_________________________________________________________________________________________")
                          print("Costumer's name :",name)
                          print("Contact no,:",phone)
                          print("Quantity of milk :",mlk)
                          print("Total amount:",mlk*c)
                          print("@@@@@@@@@@@@@@@@@@@ THANK_YOU FOR ORDERING THE ITEM @@@@@@@@@@@@@@@@@@@@@@")
                          print("\t\t\t\t\t\t\t\t\t\t Date:",datetime.now())
                      elif d==4:
                          print("How many packets(20gm) do you want:")
                          but=int(input("enter your choice:"))
                          print("You have successfully ordered",but,"packets of butter")
                          cur.execute("select * from menu where products='butter'")
                          for i in cur:
                              c=i[2]
                          print("Total amount:",but*c)
                          print ("\n")
                          print(".........................................................................................")
                          print("YOUR BILL ")
                          print("_________________________________________________________________________________________")
                          print("Costumer's name :",name)
                          print("Contact no,:",phone)
                          print("Quantity of butter :",but)
                          print("Total amount:",but*c)
                          print("@@@@@@@@@@@@@@@@@@@ THANK_YOU FOR ORDERING THE ITEM @@@@@@@@@@@@@@@@@@@@@@")
                          print("\t\t\t\t\t\t\t\t\t\t Date:",datetime.now())
                      elif d==5:
                          print("How much cheese (in kg) do you want:")
                          chs=int(input("enter your choice:"))
                          print("You have successfully ordered",chs,"Kg of cheese")
                          cur.execute("select * from menu where products='cheese'")
                          for i in cur:
                              c=i[2]
                          print("Total amount:",chs*c)
                          print ("\n")
                          print(".........................................................................................")
                          print("YOUR BILL ")
                          print("_________________________________________________________________________________________")
                          print("Costumer's name :",name)
                          print("Contact no,:",phone)
                          print("Quantity of cheese :",chs)
                          print("Total amount:",chs*c)
                          print("@@@@@@@@@@@@@@@@@@@ THANK_YOU FOR ORDERING THE ITEM @@@@@@@@@@@@@@@@@@@@@@")
                          print("\t\t\t\t\t\t\t\t\t\t Date:",datetime.now())
                      elif d in l:
                          qty=int(input("Enter Qty"))
                          print ("You have successfully ordered your selected item!!!\t:")
                          cur.execute("select * from menu where sno="+str(d))
                          for i in cur:
                              L=i[2]
                          print("Total amount:",qty*L)
                          print ("\n")
                          print(".........................................................................................")
                          print("YOUR BILL ")
                          print("_________________________________________________________________________________________")
                          print("Costumer's name :",name)
                          print("Contact no,:",phone)
                          print("Quantity  :",qty)
                          print("Total amount:",qty*L)
                          print("@@@@@@@@@@@@@@@@@@@ THANK_YOU FOR ORDERING THE ITEM @@@@@@@@@@@@@@@@@@@@@@")
                          print("\t\t\t\t\t\t\t\t\t\t Date:",datetime.now())
                      else:
                          print("Wrong Input")
                      
                          print("\t\t\t\t\t\t\t********WRONG PASSWORD*****************")
                  ch=input("DO YOU WANT TO CONTINUE (Y/N)?")
                  if ch=='n' or ch=='N':
                      exit()
                            
                            
                            
                            
                            
                            
                        
                            
                            
                            
                        
                                
                                
                                    
                                    
                                        
                                
                                
                        
                    
                    
                        
                        
        
                    
                        
                        
                        
        
        
                                
                
                    
                
                
                    
                    
                    
                        
                    
                    

