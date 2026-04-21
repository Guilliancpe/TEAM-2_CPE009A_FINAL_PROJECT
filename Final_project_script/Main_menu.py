from refresh_list import Refresh_file
from Create_item import Create_item
from Update_item import Update_item

Refresh_obj = Refresh_file()
Create_Item_obj = Create_item()
Update_obj = Update_item()

class Main_menu():
    def __init__(self, user):
        self.user = user
        
    def show_menu(self):
        decision = 0
        
        while decision != 5:
            print("|------------------------------------|")
            print("|              User Menu             |")
            print("|------------------------------------|")
            print("1. Refresh list")
            print("2. Sort list")
            print("3. Create Item")
            print("4. Update Item")
            print("5. Exit to Main Menu\n")
            
            decision = int(input("Enter a number: "))
            
            if decision == 1:
                Refresh_obj.refresh_list()
            elif decision == 2:
                print("=====Sort list=====")
            elif decision == 3:
                print("=====Create Item=====")
                Create_Item_obj.create_item()
            elif decision == 4:
                print("=====Update Item Info=====")
                Update_obj.update_item()
            elif decision == 5:
                print("Exiting to Main Menu...")
                return

