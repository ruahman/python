import csv


phones = []

# Open the CSV file
with open("isabela.csv", mode="r") as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate through the rows in the file
    for row in csv_reader:
        # phones_row = []
        for cell in row:
            # cell_split = cell.split("\xa0\n")
            cell_split = cell.split("\n")
            # print(cell_split)
            phone = {}

            phone["name"] = cell_split[0]

            try:
                phone["address"] = cell_split[1]
            except IndexError:
                phone["address"] = ""

            try:
                phone["phone"] = cell_split[2]
            except IndexError:
                phone["phone"] = ""

            phones.append(phone)

        # phones.append(phones_row)

# print(phones)

# Write the split data to the CSV file
with open("isabela-pretty.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    # Write the split_text list as a row in the CSV
    # writer.writerow(split_text)
    for phone in phones:
        writer.writerow([phone["name"], phone["address"], phone["phone"]])

print("Done!")
