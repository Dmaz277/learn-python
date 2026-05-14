import csv
with open('stok.csv',mode='r',newline='') as read:
    reader = csv.reader(read)
    header = next(reader)
    for row in reader :
        print(f"{header[0]}: {row[0]}, {header[1]}: {row[1]}, {header[2]}: {row[2]}")