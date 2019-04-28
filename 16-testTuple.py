# system yang paling ringan

import sys

data_list =[1,2,3,4,5,"pisang goreng","syahrini","via vallen",False,3.14]
data_tuple=(1,2,3,4,5,"pisang goreng","syahrini","via vallen",False,3.14)

besar_datalist =sys.getsizeof(data_list)
besar_datatuple=sys.getsizeof(data_tuple)

print("besar data list:",besar_datalist)
print("besar data tuple:",besar_datatuple)

