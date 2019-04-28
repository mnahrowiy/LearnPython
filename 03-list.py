# list
Data = [1,4,9,16,25,36,49,64]

subdata = Data[0]    # 1
subdata1 = Data[-1]  # 64
subdata2 = Data[-3]  # 36
subdata3 = Data[2:4] # [9, 16]
subdata4 = Data[-4:] # [25, 36, 49, 64]
subdata5 = Data[:4]  # [1, 4, 9, 16]

Data2 = [100,200,300,400,500,600,700,800]

# menambah list
Data3 = Data + Data2 # [1, 4, 9, 16, 25, 36, 49, 64, 100, 200, 300, 400, 500, 600, 700, 800]

# menambah content dari list
# print(Data)
# print(Data3)
# Data[4] = 87
# print(Data)

# a    = Data # ini bahaya karena akan membuat
# a[4] = 87   # file a dan Data saling berbagi

a = Data[:] # ini solusi
a[4] = 87   # file a akan mencopy semua isi dari Data namun a tidak merubah nilai dari Data
# karena jika cara pertama dilakukan maka yang
# berubah dari a akan diberikan juga pada data
# maka solusinya adalah dengan menggunakan
# a = Data[:]
# print(a)    # isi a yang dicopy dari data akan berubah namun tidak pada File Data
# # [1,4,9,16,87,36,49,64]
#
# print(Data) # isi dari Data akan tetap
# # [1,4,9,16,25,36,49,64]

# merubah content list dengan menggunakan metode slicing

Data[3:5]= [11,12]
# print(Data)

# membuat list di dalam list

x = [Data,Data2]

# mengakses list dalam multidimensional list

y = x[1][4]
# print(x)
print(y)

# method untuk list
# append
Data.append(Data2)

# Function yang bisa kita gunakan kepada list

panjang_list = len(Data)

print(panjang_list)