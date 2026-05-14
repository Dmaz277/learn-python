import csv
with open('data.csv',mode='w',newline='') as tulis :
    writer = csv.writer(tulis)
    writer.writerow(['nama','umur','kota','hobi'])
    writer.writerow(['dimz','18','jakarta','paddle'])
    writer.writerow(['mira','18','bandung','raket'])



