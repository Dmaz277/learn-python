produk_toko = {
    "baju" : 50000,
    "celana" : 30000,
    "sepatu" : 70000
}
print(produk_toko.keys())
print(produk_toko.values())
del produk_toko["baju"]
if "celana" in produk_toko:
    print(True)
else:
    print(False)