while True:
    suhu = int(input("masukan suhu dalam bentuk celcius:"))
    fahrenheit = suhu * 9/5 + 32
    kelvin = suhu + 273.15
    print(fahrenheit)
    print(kelvin)
    lanjut = input("lanjut ga nih? (y/n):")
    if lanjut == "n":
        break

        