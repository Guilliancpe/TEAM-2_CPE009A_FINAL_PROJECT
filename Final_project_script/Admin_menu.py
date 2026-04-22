from E_waste_graphs import E_graph, e_file
from Del_Item import E_admin




Es_obj = E_graph(e_file("E-waste.csv"))

efile = e_file("E-waste.csv")
Ea_obj = E_admin(efile)

class Admin_menu():
    def __init__ (self, admin):
        self.admin = admin
        
    def show_menu(self):
      choice = 0
      
      while choice != 3:
          print("\n=====Admin Menu=====\n")
          print("1. Delete Item")
          print("2. E-waste Statistics")
          print("3. Exit\n")
          
          choice = int(input("Enter a number\n"))
          
          if choice == 1:
              print("=====Delete Item=====")
              choice = input("Enter choice: ")

              if choice == "1":
                column = input("Enter column to match (e.g. Name, composition, recycle_rating): ")
                value = input(f"Enter the {column} value to delete: ")
                Ea_obj.delete_item(column, value)
                Ea_obj.delete_item("Name", "Value")
          elif choice== 2:
              print("=====E-waste Statistic=====")
              Es_obj.load_graph("composition")
          elif choice == 3:
              print("=====Exit=====")
      