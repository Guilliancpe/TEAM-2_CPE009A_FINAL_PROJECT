class Main_menu():
    def __init__ (self, user):
        self.user = user
        
    def show_menu(self):
      decision = 0
      
      while decision != 5:
          print("\n=====Main Menu=====\n")
          print("1. Refresh list")
          print("2. Sort list")
          print("3. Create Item")
          print("4. Update Item Info")
          print("5. Exit\n")
          
          
          
          decision = int(input("Enter a number\n"))
          
          if decision == 1:
              print("=====Refresh list=====")
          elif decision == 2:
              print("=====Sort list=====")
          elif decision == 3:
              print("=====Create Item=====")
          elif decision == 4:
              print("=====Update Item Info")
          elif decision == 5:
              print("=====Exit=====")
      