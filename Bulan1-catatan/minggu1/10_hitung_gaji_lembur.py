while True :
    gaji_pokok = int(input("masukan gaji bulanan anda: "))
    jam_lembur = int(input("lembur berapa jam: "))
    gaji_perjam = gaji_pokok/173
    upah_lembur = gaji_perjam * 1.5 * jam_lembur
    total_gaji = gaji_pokok + upah_lembur
    print(total_gaji)
    lanjut = input("lanjut ketik y/n ")
    if lanjut == "n":     
          break
