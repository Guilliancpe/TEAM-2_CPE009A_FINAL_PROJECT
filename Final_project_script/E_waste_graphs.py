import pandas as pd
import matplotlib.pyplot as plt

class e_file:
    def __init__(self, filename="E-waste.csv" ):
        self.filename = filename

    def load_csv(self):
        data = pd.read_csv(self.filename)
        return data
    
    def save_csv(self, data):
        data.to_csv(self.filename, index=False)
    
class E_graph(e_file):
    def __init__(self, filename: e_file):
        self.filename = filename

    def load_graph(self, Name):
        data = self.filename.load_csv()

        counts = data[Name].value_counts()

        if "composition" in counts.index:
            counts = counts.drop("composition")

        plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%')
        plt.title(f"E-Waste {Name} Distribution")
        plt.savefig("ewaste_graph.png")
       
       
    
efile = e_file("E-waste.csv")
graph = E_graph(efile)
graph.load_graph("composition")



     





        


    
        