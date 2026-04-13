from Parent_file import CSVFileReaderWriter as CSV
import csv

class login(CSV):
    def user_login(self):
        self.newfile()
        
        login_user = input("Enter your username: ")
        login_pass = input("Enter your password: ")
        
        login_success = False
        with open(self.filename, "r") as login_file:
            read = csv.reader(login_file)
            next(read)
          
            for row in read:
                if row[0] == login_user and row[1] == login_pass:
                    login_success = True
                    break
        
        if login_success:
            print("\nLogin successful!\n")
        else:
            print("\nInvalid credentials!\n")