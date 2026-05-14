import csv
with open('stok.csv', mode='r', newline='') as read :
    reader = csv.reader(read)
    user = input("enter the data you want to delete :")
    remnant = []
    for row in reader :
        if row[0] != user:
            remnant.append(row) 
with open('stok.csv', mode='w', newline='') as delete :
    writer = csv.writer(delete)
    writer.writerows(remnant)            