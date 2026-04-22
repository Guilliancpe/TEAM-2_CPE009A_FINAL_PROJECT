import os
import csv
from rich.console import Console
from rich.table import Table

os.environ['COLUMNS'] = "150"

class Refresh_file:
    def __init__(self, filename="E-waste.csv"):
        self.filename = filename
        self.console = Console()

    def refresh_list(self):
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
            print("No items found.")
            print("\nReturning to User Menu...")
            return

        with open(self.filename, "r", newline="") as my_file:
            read = csv.reader(my_file)
            rows = list(read)

        if len(rows) <= 1:
            print("No items found.")
            print("\nReturning to User Menu...")
            return

        print(" " * 47, "===== Refresh list =====", " " * 47)
        print("-" * 120)
        print("|", " " * 48, " E-waste Registry", " " * 49, "|")
        print("-" * 120)

        table = Table(show_lines=True, expand=True, width=120)
        
        table.add_column("No.", justify="center", overflow="fold")
        table.add_column("Name", justify="center", overflow="fold")
        table.add_column("Components", justify="center", overflow="fold")
        table.add_column("Composition", justify="center", overflow="fold")
        table.add_column("Condition", justify="center", overflow="fold")
        table.add_column("Net Weight", justify="center", overflow="fold")
        table.add_column("Hazard", justify="center", overflow="fold")
        table.add_column("Recycle Rating", justify="center", overflow="fold")

        count = 1
        for row in rows[1:]:
            if row and len(row) >= 7:
                table.add_row(f"{count}.", row[0], row[1], row[2], 
                    row[3], row[4], row[5], row[6])
                count += 1

        self.console.print(table)
        print("\nReturning to User Menu...")

if __name__ == "__main__":
    obj = Refresh_file()
    obj.refresh_list()
