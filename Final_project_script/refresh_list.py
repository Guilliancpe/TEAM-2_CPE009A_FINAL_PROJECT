import os
import csv

class Refresh_file:
    def __init__(self, filename="E-waste.csv"):
        self.filename = filename

    def refresh_list(self):
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
            with open(self.filename, "w", newline="") as my_file:
                write = csv.writer(my_file)
                write.writerow(["Name", "components", "composition", "condition", "net_weight", "hazard", "recycle_rating"])

        with open(self.filename, "r", newline="") as my_file:
            read = csv.reader(my_file)
            rows = list(read)

        print("=====Refresh list=====")

        if len(rows) <= 1:
            print("No items found.")
        else:
            for row in rows[1:]:
                print(" | ".join(row))

        print("\nReturning to User Menu...")

if __name__ == "__main__":
    obj = Refresh_file()
    obj.refresh_list()
