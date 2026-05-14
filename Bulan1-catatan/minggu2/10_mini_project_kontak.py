kontak = {}
def tambah(kontak):
    while True:
        nama = input("masukan nama kontak :")
        nilai = int(input("masukan nomor kontak :"))
        kontak[nama] = nilai
        lanjut = input("next? y/n :")
        if lanjut == "n" :  
            break     
    return kontak

def cari(kontak) :
    while True :

        nama = input("masukan nama kontak yang mau di cari:")
        if nama in kontak:
            print((kontak)[nama])
        else:
            print("ga ada")
        lanjut = input("next? y/n :")
        if lanjut == "n" :  
            break     
    return kontak

def tampilkan_semua(kontak):
    for nama, nomor in kontak.items():
        print(f"{nama} : {nomor}")
    return


kontak = tambah(kontak)
cari((kontak))
tampil = tampilkan_semua(kontak)