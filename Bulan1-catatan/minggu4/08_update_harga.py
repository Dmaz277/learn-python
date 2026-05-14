import csv
with open('stok.csv',mode='r',newline='') as read:
    reader = csv.reader(read)
    header = next(reader)
    user = input('enter the name of product do you want to update the price: ')
    remnant = []
    new_price = input("enter the new price :")
    remnant.append(header)
    for row in reader:
        if row[0] == user:
            new_row = [row[0],row[1],new_price]
            remnant.append(new_row)
        else:
            remnant.append(row)
with open('stok.csv',mode='w',newline='') as update_price:
    writer = csv.writer(update_price)
    writer.writerows(remnant)