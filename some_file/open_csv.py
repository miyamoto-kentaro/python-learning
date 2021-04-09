import csv

with open("./somefiles/test.csv", "w") as csv_file:
    fieldnames = ["Name", "Count"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "A", "Count": 1})
    writer.writerow({"Name": "B", "Count": 2})

# with open("./somefiles/test.csv", "r") as csv_file:
#     reader = csv.DictReader(csv_file)
#     print("####", reader)
#     for row in reader:
#         print(row["Name"], row["Count"])

# with open("./somefiles/test.csv", "a") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["C", 3])

# with open("./somefiles/test.csv", "r") as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print(row["Name"], row["Count"])
