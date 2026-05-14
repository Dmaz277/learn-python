import csv
import os
if not os.path.exists('stock.csv'):
    with open('stock.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name_product', 'price', 'stock'])

def add_product():
    with open('stock.csv', 'a', newline='') as stock_product:
        writer = csv.writer(stock_product)
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        writer.writerow([name, price, stock])

def show_all():
    with open('stock.csv',mode='r') as show:
        reader = csv.reader(show)
        header = next(reader)
        for row in reader:
            if not row:
                continue
            print(f"Product: {row[0]} | Price: {row[1]} | stock: {row[2]}")
        

def search_product():
    with open('stock.csv',mode='r') as read:
        reader = csv.reader(read)
        user = input('enter product do you looking for:')
        found = False
        for row in reader:
            if not row:
                continue
            if row[0] == user :
                print(f'{row}')
                found = True
        if found == False :
            print('null')

def update_price():
    with open('stock.csv',mode='r') as read:
        reader = csv.reader(read)
        header = next(reader)
        user = input('enter product do you want to update the price: ')
        remnant = []
        new_price = input('enter the new price:')
        remnant.append(header)
        for row in reader:
            if not row:
                continue
            if row[0] == user :
                new_row = [row[0],new_price,row[2]]
                remnant.append(new_row)
            else:
                remnant.append(row)
    with open('stock.csv',mode='w',newline='') as update:
        writer = csv.writer(update)
        writer.writerows(remnant)

def delete_product():
    with open('stock.csv',mode='r',newline='') as read:
        reader = csv.reader(read)
        header = next(reader)
        user = input('enter product that you want to delete:')
        remnant = [] 
        remnant.append(header)
        for row in reader:
            if row[0] != user :
                remnant.append(row)
    with open('stock.csv',mode='w',newline='') as deleted:
        writer = csv.writer(deleted)
        writer.writerows(remnant)

def filter_stock_low():
    with open('stock.csv',mode='r',newline='') as read:
        reader = csv.reader(read)
        header = next(reader)
        for row in reader :
            if int(row[2]) <= 100:
                print(f"Product: {row[0]} | Price: {row[1]} | stock: {row[2]} is low! need restock")

def export_report():
    with open('stock.csv',mode='r') as read:
        reader = csv.reader(read)
        remnant = []
        for row in reader:
            remnant.append(row)
    with open('laporan_product.csv',mode='w',newline='') as write:
        writer = csv.writer(write)
        writer.writerows(remnant)

def out():
    exit()
while True:
    print('''
    1. Add Product
    2. Show All
    3. Search Product
    4. Update Price
    5. Delete Product
    6. Filter Stock Low
    7. Export Report
    8. Exit
    ''')
    choice = input('Choose menu: ')
    if choice == '1':
        add_product()
    elif choice == '2':
        show_all()
    elif choice == '3':
        search_product()
    elif choice == '4':
        update_price()
    elif choice == '5':
        delete_product()
    elif choice == '6':
        filter_stock_low()
    elif choice == '7':
        export_report()
    elif choice == '8':
        out()

