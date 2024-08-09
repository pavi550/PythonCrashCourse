import csv

data = ['Id','Name','Age']

rows = [[101,'Rohit',21],
        [101,'Rohit',21],
        [103,'Rohan',21],
        [104,'Priya',21]]

with open("Write_csv",'w') as file1:
    x = csv.writer(file1)
    x.writerow(data)
    x.writerow(rows)

    print('Data is written')