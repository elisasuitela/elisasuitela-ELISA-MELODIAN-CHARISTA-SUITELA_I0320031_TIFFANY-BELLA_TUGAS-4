berat_max_lbs = 50
berat_max_kg = float(berat_max_lbs * 0.453592)

berat_bagasi = float(input("berat bagasi anda (kg): "))

#if els
if berat_bagasi <= berat_max_kg:
    berat_bagasi = True
    print("bagasi anda diizinkan untuk masuk pesawat",", ",  berat_bagasi)
else:
    berat_bagasi = False
    print("bagasi anda tidak diizinkan untuk masuk pesawat", ", ", berat_bagasi)

# percobaan a
berat_bagasi = float(110 + berat_max_kg)
print("berat bagasi anda (kg): ", berat_bagasi )
if berat_bagasi <= berat_max_kg:
    berat_bagasi = True
    print("bagasi anda diizinkan untuk masuk pesawat",", ",  berat_bagasi)
else:
    berat_bagasi = False
    print("bagasi anda tidak diizinkan untuk masuk pesawat", ", ", berat_bagasi)

# percobaan b
berat_bagasi = 49
print("berat bagasi anda (kg): ", berat_bagasi )
if berat_bagasi <= berat_max_kg:
    berat_bagasi = True
    print("bagasi anda diizinkan untuk masuk pesawat",", ",  berat_bagasi)
else:
    berat_bagasi = False
    print("bagasi anda tidak diizinkan untuk masuk pesawat", ", ", berat_bagasi)
