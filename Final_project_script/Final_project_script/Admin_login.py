import csv
import hashlib
import os

class Adminfile():
    def __init__(self, filename="admin.csv"):
        self.filename = filename

    def newfile(self, username, password, auth_code):
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as my_file:
                write = csv.writer(my_file)
                write.writerow(["username", "password", "auth_code"])
                hash_pass = hashlib.sha256(password.encode()).hexdigest()
                write.writerow([username, hash_pass, auth_code])

class Admin(Adminfile):
    def admin_login(self):
        admin_user = input("Enter your username: ")
        admin_pass = input("Enter your password: ")
        admin_auth = input("Enter 6-digit auth code: ")
        
        hash_pass = hashlib.sha256(admin_pass.encode()).hexdigest()
        
        if not os.path.exists(self.filename):
            print("Admin file not found!")
            return

        login_success = False
        with open(self.filename, "r") as admin_file:
            read = csv.reader(admin_file)
            next(read)
          
            for row in read:
                if row[0] == admin_user and row[1] == hash_pass and row[2] == admin_auth:
                    login_success = True
                    break
            
        if login_success:
            print("Login successful!")
            
            
            
        else:
            print("Wrong username, password, or auth code!")