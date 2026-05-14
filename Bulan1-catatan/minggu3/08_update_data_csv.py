import csv 
with open('data.csv',mode='r') as update :
    reader = csv.reader(update)
    header = next(reader)
    user = input('enter the data do you want to update: ')
    remnant = []
    new_name = input("enter new name :")
    new_age = input("enter new age :")
    new_city = input("enter new city :")
    new_hobby = input("enter new hobby :")
    new_row = [new_name,new_age,new_city,new_hobby]
    remnant.append(header)
    for row in reader :
        if row[0] == user :
            remnant.append(new_row)
        else:
            remnant.append(row)
        print(remnant)

with open('data.csv',mode='w',newline='') as update :
    writer = csv.writer(update)
    writer.writerows(remnant)