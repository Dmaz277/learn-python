data = {}
def tambah(data):
    while True:
        nama = input('masukan nama:')
        nilai = int(input('masukan nilai:'))
        data[nama] = nilai
        lanjut = input("lanjut ga y/n?")
        if lanjut == "n" :
            break
    return data

def hitung(data):
    total = sum(data.values())
    panjang = len(data)
    rata_rata = total/panjang
    return rata_rata

print(tambah(data))
print(hitung(data))