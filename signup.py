def login():
  import pickle
  import random
  print("-" * 35,"SIGN IN TO AVAIL OFFERS","-" * 35)
  a=int(input("YOUR MOBILE NO.="))
  z=random.randrange(1000,9999)
  print(z)
  y=int(input("Enter your four digit otp here sent :"))
  x1={}
  if y==z:
   
    n1=input("NAME=")
    g1=input("GENDER(M/F)=")
    d1=int(input("YOUR AGE="))
    m1=input("DATE OF BIRTH=")
    e1=input("EMAIL ID=")
    sn=(input("PASSWORD.="))

    print("1. SILVER")
    print("2. GOLD")
    print("3. PLATINUM")
    sc=int(input("Which membership you will take?(option no.)"))
    x1=[sn,n1,g1,d1,m1,e1]
    if sc==1:
      file=open("silver.dat","ab")
      data=pickle.dump(x1,file)
      file.close()
    elif sc==2:
      file=open("gold.dat","ab")
      data=pickle.dump(x1,file)
      file.close()
    elif sc==3:
      file=open("platinum.dat","ab")
      data=pickle.dump(x1,file)
      file.close()
    else:
      print("INVALID")
    print("YOU ARE SUCCESSFULLY SIGNED IN ")
    print()
    print(x1)
  else:
    print("INCORRECT OTP !!!!")

