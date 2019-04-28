# inout output file

# membuat file text
"""
w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan dibuat file baru
r = read mode only / hanya bisa baca
a = appending mode / menambahkan data di akhir baris
r+= write and read mode
"""


file = open("data.txt",'w')
file.write("ini adalah data text yang dibuat dengan menggunakan python")
file.write("\nini baris kedua")
file.write("\nini baris ketiga")
file.write("\nini baris keempat")
file.close() # ini untu menutup file

# membaca file text
file2 = open("data.txt",'r')

# print(file2.read()) # tidak usah close, hanya baca doang

print(file2.readline()) # menampilkan baris pertama pada console
file2.close()

# appending mode

file3 = open("data.txt", 'a') # jika di ganti dengan 'w' maka file akan menimpa file sebelumnya

file3.write("\nbaris ini dibuat dengan menggunakan mode append")

file3.close()


