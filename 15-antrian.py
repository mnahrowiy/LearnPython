from collections import deque

antrian = deque([1,2,3,4,5])

print('data sekarang: ',antrian)

# menambahkan data
antrian.append(6)
print('data masuk: ',6)
print('data sekarang: ',antrian)

antrian.append(7)
print('data masuk: ',7)
print('data sekarang: ',antrian)

# mengurangi antrian
out =antrian.popleft() # ini cara membuang di depan
print('data keluar: ',out)
print('data sekaran: ',antrian)

out =antrian.popleft() # ini cara membuang di depan
print('data keluar: ',out)
print('data sekaran: ',antrian)

out =antrian.popleft() # ini cara membuang di depan
print('data keluar: ',out)
print('data sekaran: ',antrian)


# menambahkan data lagi
antrian.append(8)
print('data masuk: ',8)
print('data sekarang: ',antrian)