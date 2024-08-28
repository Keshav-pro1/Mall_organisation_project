import restaurant
import signup
import pickle
import login
'''-------------------------------------------------------------------------------------------------------------------------------------- '''
ans="yes"
while ans=="yes" or ans=="y":
  
  print("-" * 35,"WELCOME TO OUR MALL","-" * 38)
  print("1.PREMIUM ACCOUNT")
  print("2.RESTAURANT")
  print("3.PLAY GAMES")
  print("4.SIGN IN FOR PREMIUM ACCOUNT")
  print("5.LEADERBOARD OF GAMES")
  print("6.EXIT")
  print("*"*25,"DECIDE YOUR PLACE","*"*25)
  choice=int(input("YOUR CHOICE (OPTION NO.)= "))
  print()

  if choice==1:
    print("-" * 38,"LOGIN PLATFORM","-" * 45)
    login.login()
    print("-" * 35,"HOPE YOU ENJOYED","-" * 35)
    ans=input("continue?(y/n)").lower()
    

  elif choice==2:
    print("-" * 45,"RESTAURANT","-" * 45)
    restaurant.order()
    print("-" * 35,"HOPE YOU ENJOYED","-" * 35)
    ans=input("continue?(y/n)").lower()
  
  elif choice==3:
    login.game()
    print("-" * 35,"HOPE YOU ENJOYED","-" * 35)
    ans=input("continue?(y/n)").lower()  
    
  elif choice==4:
    print("-" * 45,"SIGN UP","-" * 50)
    signup.login()
    print("-" * 35,"HOPE YOU ENJOYED","-" * 35)
    ans=input("continue?(y/n)").lower()

  elif choice==5:
    print("-" * 45,"LEADERBOARD","-" * 45)
    login.board()
    print("-" * 35,"HOPE YOU ENJOYED","-" * 35)
    ans=input("continue?(y/n)").lower()

  else:
    ans="no"
    print("$ "*7,"* "*10,"THANK YOU","- "*10,"# "*10)
  
