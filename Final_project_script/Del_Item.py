import pandas as pd


class e_file:
    def __init__(self, file="E-waste.csv"):
        self.file = file

    def load_csv(self):
        return pd.read_csv(self.file)

    def save_csv(self, data):
        data.to_csv(self.file, index=False)

class E_admin(e_file):
    def __init__(self, file: e_file):
        self.file = file

    def delete_item(self, name, value):
     data = self.file.load_csv()

     if name not in data.columns:
        print(f"Column '{name}' not found.")
        return

     new_data = data[data[name] != value]
     self.file.save_csv(new_data)
     print(f"Deleted items where {name} = {value}")


   



 

