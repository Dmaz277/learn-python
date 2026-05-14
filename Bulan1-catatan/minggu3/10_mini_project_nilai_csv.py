import csv
def add():
    with open('value.csv',mode='a',newline='') as add:
        writer = csv.writer(add)
        new_name = input("enter new name :")
        new_value = input("enter new nilai :")
        new_row = [new_name,new_value]
        writer.writerow(new_row)
def show():
    with open('value.csv',mode='r',newline='') as read:
        reader = csv.reader(read)
        header = next(reader)
        for row in reader :
            print(row)
def search_by_name():
    with open('value.csv',mode='r',newline='') as read:
        reader = csv.reader(read)
        user = input('enter name that you want to search:')
        found = False
        for search in reader :
            if search[0] == user:
                print(search)
                found = True
        if not found:
            print('not found')
def rata_rata():
    with open('value.csv',mode='r',newline='') as read:
        reader = csv.reader(read)
        header = next(reader)
        total = 0
        count = 0
        for row in reader :
            total += int(row[1])
            count += 1
        if count > 0:
            print(f"average value: {total/count}")
        else:
            print("no value.")

def leave():
    exit()
while True:
    print("1. add nilai")
    print("2. show all")
    print("3. search by name")
    print("4. rata-rata nilai")
    print("5. leave")
    pilihan_user = input('pilih menu :')
    if pilihan_user == "1" :
        add()
    elif pilihan_user == '2' :
        show()
    elif pilihan_user == '3' :
        search_by_name()
    elif pilihan_user == '4' :
        rata_rata()
    elif pilihan_user == '5' :
        leave()