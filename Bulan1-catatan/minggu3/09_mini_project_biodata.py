import csv
def add():
    with open('data.csv',mode='a',newline='') as add:
        writer = csv.writer(add)
        new_name = input("enter new name :")
        new_age = input("enter new age :")
        new_city = input("enter new city :")
        new_hobby = input("enter new hobby :")
        new_row = [new_name,new_age,new_city,new_hobby]
        writer.writerow(new_row)

def show():
    with open('data.csv',mode='r',newline='') as read:
        reader = csv.reader(read)
        header = next(reader)
        for row in reader :
            print(row)

def search():
    with open('data.csv',mode='r',newline='') as read:
        reader = csv.reader(read)
        user = input('enter name that you want to search:')
        found = False
        for search in reader :
            if search[0] == user:
                print(search)
                found = True
        if not found:
            print('not found')

def leave():
    exit()

while True:
    print("1. add biodata")
    print("2. show all")
    print("3. search")
    print("4. leave")
    pilihan_user = input('pilih menu :')
    if pilihan_user == "1" :
        add()
    elif pilihan_user == '2' :
        show()
    elif pilihan_user == '3' :
        search()
    elif pilihan_user == '4' :
        leave()


        


