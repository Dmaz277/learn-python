import csv
with open('data.csv',mode='a',newline='') as nambah:
    writer = csv.writer(nambah)
    writer.writerow(['ran','19','sukabumi','bola'])
