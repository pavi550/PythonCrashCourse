import csv

with open('example.txt')as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'{" ".join(row)}')
            line_count+=1
        print(row)
        line_count+=1