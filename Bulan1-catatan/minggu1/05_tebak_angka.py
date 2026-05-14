angka = 5
while True:
    tebak = int(input("tebak angka dari 1 - 10 : "))
    if tebak == 5 :
        print('selamat anda benar')  
        break  
    elif tebak > angka :
        print('kebesaran bos')
    elif tebak < angka :
        print('kekecilan bos')
    
