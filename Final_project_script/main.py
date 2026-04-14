from Create_account import Create_account 
from login_system import login 
from Admin_login import Admin

create_obj = Create_account()
login_obj = login()
admin_obj = Admin()

admin_obj.newfile("Admin", "TIPadmin2026", "123456")

choice = 0

print("|-----------------------------------------------------|")
print("| Welcome to the E-waste Management & Tracking System |")
print("|-----------------------------------------------------|")

while choice != 4:
    print("====== Main Menu ======\n 1. New account \n 2. Login \n 3. Admin \n 4. Exit")
    
    try:
        choice = int(input("\nChoice: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    if choice == 1:
        create_obj.createacc()
    elif choice == 2:
        login_obj.user_login()
    elif choice == 3:
        admin_obj.admin_login()
    elif choice == 4:
        print("Goodbye!")
    else:
        print("Please enter a valid choice\n")
        continue
