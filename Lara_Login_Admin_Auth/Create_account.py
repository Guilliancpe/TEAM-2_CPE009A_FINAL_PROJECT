from Parent_file import CSVFileReaderWriter as CSV
import csv

class Create_account(CSV):
    def createacc(self):
        self.newfile()
        
        username = input("Please enter your username: ")
        password = input("Please enter a password: ")
        
        with open(self.filename, "a", newline="") as my_file:
            write = csv.writer(my_file)
            write.writerow([username, password])
            print("Account saved!")