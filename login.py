import random
import pickle

def member():
  c1="yes"
  if c1=="yes":
    name=input("your name=")
    no=(input("your Password="))
    flag=0
    print("1. SILVER")
    print("2. GOLD")
    print("3. PLATINUM")
    e=input("Which mebership you have?:")
    e.lower()
    op1=str("silver")
    op2=str("gold")
    op3=str("platinum")
    if e==op1:
      file=open("silver.dat","rb+")
      while True:
        try:
          sc=pickle.load(file)
          print(sc)
          for i in sc:
            if i==no:
              print("-" * 35,"YOUR DATA","-" * 35)
              print("-" * 35,name,"\n","YOU ARE OUR SILVER MEMBERSHIP OWNER")
              print("10% discount on everybooking+3month free access+free drinks")
              i=random.randrange(100,400)
              print(i)
              print("copy the unique code above to avail the offer")
              flag=1
        except EOFError:
          break
      if flag==0:
        print("Record not found...")
      file.close()
        
    elif e==op2:
      file=open("gold.dat","rb+")
      while True:
        try:
          sc=pickle.load(file)
          print(sc)
          for i in sc:
            if i==no:
              print("-" * 35,"YOUR DATA","-" * 35)
              print("-" * 35,name,"\n","YOU ARE A GOLD MEMBERSHIP OWNER")
              print("20% discount on everybooking+4.5month free access+free drinks")
              i=random.randrange(100,400)
              print(i)
              print("copy the unique code above to avail the offer")
              flag=1
        except EOFError:
          break
      if flag==0:
        print("Record not found...")
      file.close()
        
    elif e==op3:
      file=open("platinum.dat","rb+")
      while True:
        try:
          sc=pickle.load(file)
          print(sc)
          for i in sc:
            if i==no:
              print("-" * 35,"YOUR DATA","-" * 35)
              print("-" * 35,name,"\n","YOU ARE OUR PLATINUM MEMBERSHIP OWNER")
              print("50% discount on everybooking+6 month free access+free drinks")
              i=random.randrange(100,400)
              print(i)
              print("copy the unique code above to avail the offer")
              flag=1
        except EOFError:
          break
      if flag==0:
        print("Record not found...")
      file.close()
        
def login():
  z=1
  while z==1:
    x=random.randrange(1000,9999)
    print("otp generated:",x)
    y=int(input("enter the otp here:"))
    if x==y:
      print("you are successfully logged in")
      z=2
    else:
      print("#"*20,"INVALID TRY AGAIN","#"*20)
  str1=str(input("Do you have a premium membership (yes/no)"))
  str1.lower
  q= str("yes")
  if str1==q:
    member()
  else:
    print("THANK YOU")
    
   


def game():
  print("-" *25,"WELCOME TO THE GAMING AREA ","-" * 35)
  print()
  print("RULES------> For every correct ans 4marks are awarded and -1 for every incorrect")
  g=["*","-","+"]
  j=0
  l=0
  t1=0
  x2=int(input("how many times you want to play="))
  for k in range(x2):
    m=random.randint(0,2)
    m=g[m]
    h=int(random.randint(1,100))
    i=int(random.randint(1,100))
    print(k+1,". Question=",h,m,i)
    n=int(input("ANSWER="))
    if m=='*':
      o=h*i
    elif m=='+':
      o=h+i
    elif m=='-':
      o=h-i
    if o==n:
      j+=4
      l+=1
      t1+=5
      print("CORRECT")
    else:
      j-=1
      print("INCORRECT")
    print()
  print("     Total correct Questions=",l)
  print("     Total score=",j)
  if t1<0:
    t1=0
    print("    tickets won=",0)
  else:
    print("    tickets won=",t1)
  print("DO YOU HAVE A MEMBERSHIP? ")
  c1=input("(yes/no)=").lower()
  
  if c1=="yes":
    e=str(input("choose your mebership offer (silver,gold,platinum):"))
    e.lower
    op1=str("silver")
    op2=str("gold")
    op3=str("platinum")

    if e==op1:
      a=open("silver.dat","rb+")
      f=0
      sn=(input("Enter PASSWORD"))
      while True:
        try:
          z=pickle.load(a)
          print(z)
          for i in z:
            if i==sn:
              print("-" * 35,z[1],"\n","YOU ARE OUR SILVER MEMBERSHIP OWNER")
              print("20 more tickets")
              ns=t1+20
              print("NEW VALUE=",ns)
              f=1
          leader(ns,z,x2)
        except EOFError:
          break
      if f==0:
        print("Record not found...")
      a.close()

    if e==op2:
      a=open("gold.dat","rb+")
      f=0
      sn=(input("Enter PASSWORD"))
      while True:
        try:
          z=pickle.load(a)
          print(z)
          for i in z:
            if i==sn:
              print("-" * 35,z[1],"\n","YOU ARE OUR GOLD MEMBERSHIP OWNER")
              print("50 more tickets")
              ns=t1+50
              print("NEW VALUE=",ns)
              f=1
          leader(ns,z,x2)
        except EOFError:
          break

      if f==0:
        print("Record not found...")
      a.close()

    if e==op3:
      a=open("platinum.dat","rb+")
      f=0
      sn=(input("Enter PASSWORD"))
      while True:
        try:
          z=pickle.load(a)
          print(z)
          for i in z:
            if i==sn:
              print("-" * 35,z[1],"\n","YOU ARE OUR PLATINUM MEMBERSHIP OWNER")
              print("70 more tickets")
              ns=t1+70
              print("NEW VALUE=",ns)
              f=1
          leader(ns,z,x2)      
        except EOFError:
          break
      if f==0:
        print("Record not found...")
      a.close()
      
      
  elif c1=="no":
    ns=t1
    name=input("Your name=")
    z=[777,name]
    print("VALUE =",t1)
    leader(ns,z,x2)
  
  print()
  print("THANK YOU FOR PLAYING")
  print("-" * 35,"HOPE YOU ENJOYED","-" * 35)


def leader(t1,z,x2):
  f=open("leader.txt","a")
  l=[z[1],"\t","\t",t1,"\t","\t",x2]
  f.writelines([z[1],"\t","\t",str(t1),"\t","\t",str(x2),"\n"])
  f.close()

def board():
  f=open("leader.txt","r")
  re=f.readlines()
  for i in re:
    print(i)
  f.close()


  
  
  
  
  

