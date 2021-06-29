import csv

towrite = list()

with open("table_in.csv") as csvfile:
    data = csv.reader(csvfile)
    for i in data:
        towrite.append([i[1], i[0]])

with open("filtered_csv.csv", "w") as filteredcsv:
    data = csv.writer(filteredcsv)
    data.writerows(towrite)
