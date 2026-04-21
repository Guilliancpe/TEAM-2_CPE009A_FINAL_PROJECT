import csv
from Parent_file import CSVFileReaderWriter as CSV


class Update_Item(CSV):
    def __init__(self, filename="E-waste.csv"):
        self.filename = filename

    def update_item(self):
        name = input("Enter item name to update: ")
        updated_rows = []
        found = False

        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)
            updated_rows.append(header)

            for row in reader:
                if row[0] == name:
                    found = True
                    print("\nLeave blank to keep old value.\n")

                    row[1] = input(f"components ({row[1]}): ") or row[1]
                    row[2] = input(f"composition ({row[2]}): ") or row[2]
                    row[3] = input(f"condition ({row[3]}): ") or row[3]
                    row[4] = input(f"net_weight ({row[4]}): ") or row[4]
                    row[5] = input(f"hazard ({row[5]}): ") or row[5]
                    row[6] = input(f"recycle_rating ({row[6]}): ") or row[6]

                updated_rows.append(row)

        if not found:
            print("Item not found!")
            return

        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)

        print("Item updated successfully!")
