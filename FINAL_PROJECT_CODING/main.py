from Create_account import Create_account 
from login_system import login 
from Admin_login import Admin




create = Create_account()
login = login()
admin = Admin()


choice = 0
    
    
while choice != 4:
    for i in range(1):
    
        print(" 1. New account \n 2. Login \n 3. Admin \n 4. Exit \n ")

        choice = int(input("Choice: "))
        
        if choice == 1:
            create.createacc()
         
            
        elif choice ==2:
            login.user_login()
          

        elif choice ==3:
            admin.admin_login()

        elif choice == 4:
            print("Goodbye!")
        
 
    


  
     
   
    
    
    
    
    
    
   
            
  
    
    




    
