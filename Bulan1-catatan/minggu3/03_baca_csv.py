import csv
with open("data.csv",mode='r') as baca:
    reader = csv.reader(baca)
    header = next(reader)
    for baris in reader:
        print(baris[0])