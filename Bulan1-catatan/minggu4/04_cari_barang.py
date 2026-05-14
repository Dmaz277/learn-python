import csv
with open('stok.csv',mode='r',newline='') as read:
    reader = csv.reader(read)
    user = input('enter product do you look for : ')
    found = False
    for search in reader :
        if search[0] == user :
            print(search)                      
            found = True
    if found == False:
        print('empty')