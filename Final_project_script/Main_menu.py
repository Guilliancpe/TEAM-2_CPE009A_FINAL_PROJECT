from refresh_list import Refresh_file
from Create_item import Create_item
from Update_item import Update_Item
from sort_list import Sort_list

class Main_menu():
    def __init__(self, user):
        self.user = user
        self.Refresh_obj = Refresh_file()
        self.Create_Item_obj = Create_item()
        self.Update_obj = Update_Item()
        self.Sort_obj = Sort_list()
        
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
                self.Refresh_obj.refresh_list()
            elif decision == 2:
                print("=====Sort list=====")
                self.Sort_obj.sort_list()
            elif decision == 3:
                print("=====Create Item=====")
                self.Create_Item_obj.create_item()
            elif decision == 4:
                print("=====Update Item Info=====")
                self.Update_obj.update_item()
            elif decision == 5:
                print("Exiting to Main Menu...")
                return
