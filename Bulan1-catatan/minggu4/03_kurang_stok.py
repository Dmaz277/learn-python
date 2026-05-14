import csv
with open('stok.csv',mode='r',newline='') as reduce_stock:
    reader = csv.reader(reduce_stock)
    header = next(reader)
    user = input('enter the name of product do you want to reduce the stock: ')
    remnant = []
    new_stock = input("enter the new stock :")
    remnant.append(header)
    for row in reader:
        if row[0] == user:
            new_row = [row[0], new_stock, row[2]]
            remnant.append(new_row)
        else:
            remnant.append(row)
            
with open('stok.csv',mode='w',newline='') as write_stock:
    writer = csv.writer(write_stock)
    writer.writerows(remnant)
        