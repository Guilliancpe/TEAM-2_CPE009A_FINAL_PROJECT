import csv
import hashlib
import os

username = "Admin"
password = "TIPadmin2026"



class Adminfile():
    def __init__(self, filename="admin.csv"):
        self.filename = filename

    def newfile(self, username, password):
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as my_file:
                 write = csv.writer(my_file)
                 write.writerow(["username", "pasword"])
                 hash_pass = hashlib.sha256(password.encode()).hexdigest()
                 write.writerow([username, hash_pass])
    


class Admin(Adminfile):
    def admin_login(self):
        admin_user = input("Enter your username: ")
        admin_pass = input("Enter your password: ")
        
        hash_pass = hashlib.sha256(admin_pass.encode()).hexdigest()
        
        with open(self.filename, "r") as admin_file:
            read = csv.reader(admin_file)
            next(read)
          
            for row in read:
                if row[0] == admin_user and row[1] == hash_pass:
                    print("Login succesful!")
                    return
                print("Wrong username or password!")
                
       
         
