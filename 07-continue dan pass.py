for i in range(1,10):
    # mendeteksi 6
    if i is 6:
        print("nilai i adalah ",6)
        # break    : fungsinya untuk mengakhiri for (terminasi)
        # continue : fungsinya untuk melanjutkan ke step berikutnya / langsung looping lagi ke atas
        pass # kata kunci kosong
        print("cek bro 1")
    print("nilai saat ini adalah ",i)
else:
    print("akhir dari loop")

print("print di luar loop")

# contoh pass :
# pass itu melewati saja
for i in range(1,10):
    pass
    print(i)