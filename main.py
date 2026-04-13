from Create_account import Create_account 
from login_system import login 
from Admin_login import Admin


print("\n Welcome to our tracking system! ")
print(" 1. New account \n 2. Login \n 3. Admin \n ")

choice = int(input("Choice: "))

create = Create_account()
login = login()
admin = Admin()



if choice == 1:
    create.createacc()
 
    
elif choice ==2:
    login.user_login()
  

elif choice ==3:
    admin.admin_login()

else:
    print("Goodbye!")
    
    



  
     
   
    
    
    
    
    
    
   
            
  
    
    




    
