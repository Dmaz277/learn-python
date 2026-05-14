import csv
with open('stok.csv', 'w', newline='') as stock_product:
    writer = csv.writer(stock_product)
    header = ['name_product','stock','price']
    writer.writerow(header)
    name_product = input('enter name product :')
    stock = input('enter stock :')
    price = input('enter price :')
    new_row = [name_product,stock,price]
    writer.writerow(new_row)
    