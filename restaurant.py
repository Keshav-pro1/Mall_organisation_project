s=1
import pickle
def member(s):
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
              print("10% discount")
              s=s-(s*0.1)
              print("NEW BILL=",s)
              s=s-(s*0.1)
              flag=1
        except EOFError:
          file.close()
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
              print("20% discount")
              s=s-(s*0.2)
              print("NEW BILL=",s) 
              flag=1
        except EOFError:
          file.close()
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
              print("50% discount")
              s=s-(s*0.5)
              print("NEW BILL=",s)
              flag=1
        except EOFError:
          break
      if flag==0:
        print("Record not found...")
        file.close()


def order():
  import random
  print("-" * 40,"WELCOME TO THE RESTAURANT","-" * 40)
  print("HERE IS OUR MENU CARD")
  print()
  print( "SOUTH INDIAN :-") 
  print("1.IDLI                                                                        155.00 ")
  print("2.BATATA                                                                  160.00")
  print("3.IDLI FRY                                                                  160.00")
  print("4.DAHI BHALLA                                                        160.00")
  print("5.DOSA MASALA                                                        170.00")
  print("6.MASALA UTTAPA                                                     180.00")
  print()
  print("BEVERAGES :-")
  print("7.TEA                                                                          120.00")
  print("8.COFFEE                                                                    130.00")
  print("9.MILK CUP                                                                 135.00")
  print("10.NESCAFE                                                                135.00")
  print()
  t=0
  s=0
  k=[]
  e=int(input("NO. OF ITEMS YOU WANT TO ORDER="))
  for i in range (e):
    a=int(input("Enter order no. acc to food's S.NO.="))
    if a==1:
      s=s+155
      t+=5
      k.append("IDLI")
    elif a==2:
      s=s+160
      t+=5
      k.append("BATATA")
    elif a==3:
      s=s+160
      t+=5
      k.append("IDLI FRY")
    elif a==4:
      s=s+160
      t+=5
      k.append("DAHI BHALLA")
    elif a==5:
      s=s+170
      t+=5
      k.append("DOSA")
    elif a==6:
      s=s+180
      t+=5
      k.append("UTTAPA")
    elif a==7:
      s=s+120
      t+=5
      k.append("TEA")
    elif a==8:
      s=s+130
      t+=5
      k.append("COFFEE")
    elif a==9:
      s=s+135
      t+=5
      k.append("MILK CUP")
    elif a==10:
      s=s+135
      t+=5
      k.append("NESCAFE")
    else:
      continue
  print()
  print(k)
  print()
  print("-" * 35,"YOUR ORDER HAS BEEN REGISTERED","-" * 35)
  print()
  print("\t","YOUR SEAT NO. IS -->", random.randint(1,100) )
  print("AVG. WAITING TIME IS=" , t,"MINUTES")
  print("YOUR TOTAL BILL IS=",s,"Ruppees only")
  print("*"*60)
  print("DO YOU HAVE A MEMBERSHIP? ")
  c1=input("(yes/no)=").lower()
  if c1=="yes":
    member(s)
  else:
    print("bill =",s)
    
  print("")
  print()
  print("1. CASH                                                   2.PAYTM")
  d=int(input("INPUT (OPTION)="))
  if d==2:
    print("SCAN OUR CODE AND PAY= IIIIIIIIIIIIIIIII")
  b=1
  b=int(input("RATE OUR SERVICE BETWEEN 1-5 = "))
  print()

  if b>=3 and b<=5:
    print("*"*20,"we wish you a great day")
  elif b<3 and b>=1:
    print("*"*20,"THANK YOU")
  else:
    print("*"*20,"THANK YOU")
  print()
  c=input("ENTER YOUR FEEDBACK AND MAKE US BETTER =")
  print("*"*20,"HOPE YOU HAVE ENJOYED","*"*20)



