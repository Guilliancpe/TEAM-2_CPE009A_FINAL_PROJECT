import os
import csv

class Refresh_file:
    def __init__(self, filename="E-waste.csv"):
        self.filename = filename

    def refresh_list(self):
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
            print("No items found.")
            print("\nReturning to User Menu...")
            return

        with open(self.filename, "r", newline="") as my_file:
            read = csv.reader(my_file)
            rows = list(read)

        print(" " * 30, "===== Refresh list =====", " " * 30)
        print("-" * 86)
        print("|", " " * 31, " E-waste Registry", " " * 32, "|")
        print("-" * 86)
        print("| Name | Components | Composition | Condition | Net Weight | Hazard | Recycle Rating |")
        print("-" * 86)

        if len(rows) <= 1:
            print("No items found.")
        else:
            count = 1
            for row in rows[1:]:
                if row and row != rows[0]:
                    print(f"| {count}. | {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} |")
                    count += 1

        print("\nReturning to User Menu...")

if __name__ == "__main__":
    obj = Refresh_file()
    obj.refresh_list()
