# Queues bagian dari list
# Queues adalah seperti tumpukan buku yang dia mbil pasti yan dia atas dulu

tumpukan = [1,2,3,4,5,6]
print('data sekarang :',tumpukan)

# masukan data baru
tumpukan.append(7)
print('data masuk:',7)
tumpukan.append(8)
print('data masuk:',8)

# pop() untuk keluarkan data
out = tumpukan.pop()
print('data keluar:',out)
print('data sekarang:',tumpukan)