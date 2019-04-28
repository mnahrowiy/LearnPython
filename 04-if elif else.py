# if elif else
#
# bahasa c
# if (nilai < 75){
#     print("Nilai anda "+ nilai);
# } // hanya perbandingan

nilai1 = 75
nilai2 = 80

if nilai1 is 75: # is pengganti ==
    print("Nilai anda: ",nilai1)
    print("step satu")
# sepasi pada python sangat berpengaruh
# dan sebagai penutup
    if nilai2 is not 80: # not equal
        print("Nilai anda: ",nilai2)
        print("step kedua")
        #if di dalam if


# elif sebagai syarat tambahan
# else syarat terakhir
nilai = 49
print(70*"=")
if 80 <=nilai <= 100:
    print("Nilai anda adalah A")
elif 70 <= nilai <80:
    print("Nilai anda adalah B")
elif 60 <=nilai <70:
    print("Nilai anda adalah C")
elif 50 <=nilai <60:
    print("Nilai anda adalah D, lakukan perbaikkan")
else:
    print("Maaf anda tidak lulus mata kuliah ini")

print(100*"+")
print("operator logika untuk list dan string")
print(" ")
gorengan = ["bakwan","cireng","bala-bala","gehu","combro","pisang goreng","pukis","risoles"]

beli = "sepatu"

if beli in gorengan:
    print('Mamang bilang," ya saya jual',beli,'"')

if not beli in gorengan:
    print('"Saya gak jual ',beli,'"')


# in cek string
karakter = "z"
if 'karakter' in beli:
    print("ada ",karakter,"di",beli)
else:
    print("tidak ada ",karakter, " di",beli)
