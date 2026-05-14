import csv
with open('data.csv',mode='r',newline='') as read:
    reader = csv.reader(read)
    user = input('masukan nama yang mau dicari : ')
    found = False
    for search in reader :
        if search[0] == user :
            print(search)                      
            found = True                       
    if found == False:#ini diperjelasin lagi dan ada variabel untuk menjelaskannya lagi gabisa 1 alur
        print('ga ada')

