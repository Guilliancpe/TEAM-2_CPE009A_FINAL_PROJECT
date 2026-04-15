import os, csv

class Create_file():
    def __init__(self, filename="E-waste.csv"):
        self.filename = filename

    def newfile(self):
            with open(self.filename, "w", newline="") as my_file:
                write = csv.writer(my_file)
                write.writerow(["Name", "components", "composition", "condition", "net_weight", "hazard", "recycle_rating"])


class Create_item(Create_file):
    def create_item(self):
        self.newfile()

        self.Name = input("Input Item Name")
        self.components = input("Input Item Component")
        self.composition = input("Input Item Composition")
        self.condition = input("Input Item Condition")
        self.net_weight = input("Input Item Net Weight")
        self.hazard = input("Input Item Hazard")
        self.recycle_rating = input("Input Item Recycle Rating")

        with open(self.filename, "a", newline="") as my_file:
            write = csv.writer(my_file)
            write.writerow([self.Name, self.components, self.composition, self.condition, self.net_weight, self.hazard, self.recycle_rating])
            print("Item saved!")
         
 
         
        
         

