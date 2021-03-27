umur = int(input("Umur Anda: "))
lulus_ujian = input("Apakah anda sudah lulus ujian kualifikasi? (Y / T): ")

if umur >= 21:
    umur = True
else:
    umur = False

if lulus_ujian == "Y":
    lulus_ujian = True
if lulus_ujian == "T":
    lulus_ujian = False

hasil = umur and lulus_ujian

if hasil == True:
    print("Anda dapat mendaftar di kursus")
if hasil == False:
    print("anda tidak dapat mendaftar di kursus")