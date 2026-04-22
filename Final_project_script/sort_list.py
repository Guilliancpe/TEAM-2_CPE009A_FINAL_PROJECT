import os
import csv
from rich.console import Console
from rich.table import Table

os.environ['COLUMNS'] = "150"

class Sort_list:
    def __init__(self, filename="E-waste.csv"):
        self.filename = filename
        self.console = Console()

    def sort_list(self):
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

        print(" " * 47, "===== Sort list =====", " " * 47)
        print("-" * 120)
        print("|", " " * 48, " E-waste Registry", " " * 49, "|")
        print("-" * 120)

        print("\nChoose column to sort by:")
        print("1. Name")
        print("2. Components")
        print("3. Composition")
        print("4. Condition")
        print("5. Net Weight")
        print("6. Hazard")
        print("7. Recycle Rating")

        choice = input("Enter a number: ")

        columns = {
            "1": 0,
            "2": 1,
            "3": 2,
            "4": 3,
            "5": 4,
            "6": 5,
            "7": 6
        }

        if choice not in columns:
            print("Invalid choice.")
            print("\nReturning to User Menu...")
            return

        index = columns[choice]
        data = [row for row in rows[1:] if len(row) >= 7]
        data.sort(key=lambda x: x[index].lower())

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
        for row in data:
            table.add_row(
                f"{count}.",
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )
            count += 1

        self.console.print(table)
        print("\nReturning to User Menu...")

if __name__ == "__main__":
    obj = Sort_list()
    obj.sort_list()
