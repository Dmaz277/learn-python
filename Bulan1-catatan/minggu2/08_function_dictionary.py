produk = {
    "baju" : 30000,
    "celana" : 500000,
    "sepatu" : 100000
}
def mahal(produk):
    termahal = max(produk, key=produk.get)
    return termahal
print(mahal(produk))