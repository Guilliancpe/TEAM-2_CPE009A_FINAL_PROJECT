import os
import csv

class CSVFileReaderWriter():
    def __init__(self, filename = "user_accounts.csv"):
        self.filename = filename
        
    def newfile(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as my_file:
                write = csv.writer(my_file)
                write.writerow(["username", "pasword"])
                
                