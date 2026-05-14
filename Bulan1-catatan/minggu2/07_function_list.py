angka = [1,3,2,4,6,7,9]

def hitung(angka):
    total = sum(angka)
    panjang = len(angka)
    rata_rata = total/panjang
    return rata_rata
print(hitung(angka))
