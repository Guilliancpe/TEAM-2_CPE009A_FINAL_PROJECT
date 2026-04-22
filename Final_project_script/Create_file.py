import os, csv

class Create_file:
    def __init__(self, filename="E-waste.csv"):
        self.filename = filename

    def newfile(self):
        # Only create header if file does not exist yet
        if not os.path.exists(self.filename):
            with open(self.filename, "a", newline="") as my_file:
                write = csv.writer(my_file)
                write.writerow([
                    "Name", "components", "composition",
                    "condition", "net_weight", "hazard", "recycle_rating" ])