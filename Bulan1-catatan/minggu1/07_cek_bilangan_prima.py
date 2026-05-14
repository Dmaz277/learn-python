angka_user = int(input("masukan angka :"))
prima = True
for i in range(2,angka_user):
    if angka_user % i == 0 : 
        prima = False
        break
if prima == True :
    print("prima")
else:
    print("bukan bilangan prima")


