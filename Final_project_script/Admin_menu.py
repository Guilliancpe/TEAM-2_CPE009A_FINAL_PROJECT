class Admin_menu():
    def __init__ (self, admin):
        self.admin = admin
        
    def show_menu(self):
      choice = 0
      
      while choice != 4:
          print("\n=====Admin Menu=====\n")
          print("1. Archive/delete Item")
          print("2. E-waste Statistics")
          print("3. E-waste Trackings")
          print("4. Exit\n")
          
          
          
          choice = int(input("Enter a number\n"))
          
          if choice == 1:
              print("=====Refresh list=====")
          elif choice== 2:
              print("=====E-waste Statistic=====")
          elif choice == 3:
              print("=====E-waste Tracking=====") 
          elif choice == 4:
              print("=====Exit=====")
      