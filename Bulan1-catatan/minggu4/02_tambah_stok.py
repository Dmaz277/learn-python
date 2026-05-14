import csv
with open('stok.csv', 'a', newline='') as add_product:
    writer = csv.writer(add_product)
    name_product = input('enter name product :')
    stock = input('enter stock :')  
    price = input('enter price :')
    new_row = [name_product,stock,price]
    writer.writerow(new_row)