import csv

with open("nifty100.csv", "r") as file:
    reader = csv.reader(file)
    # reader = csv.DictReader(file)
    # print(reader) #object
    for row in reader:
        # company = row["Company Name"]
        company = row[0]
        print(company)
        