import csv
with open('stok.csv',mode='r') as read:
    reader = csv.reader(read)
    remnant = []
    for row in reader:
        remnant.append(row)
with open('laporan.csv',mode='w',newline='') as write:
    writer = csv.writer(write)
    writer.writerows(remnant)
