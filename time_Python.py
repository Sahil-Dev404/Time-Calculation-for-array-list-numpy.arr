import numpy as np
import time
import array as array 

N=10000000

#for the list time calculation 
start=time.perf_counter()
lst=[]
for i in range(N):
    lst.append(i)

#some benchmark test 
s=0
for x in lst:
    s += x

end=time.perf_counter()
print(f"List Time: {end-start} seconds")

#for the array time calculation 
start=time.perf_counter()

arr = array.array('i')
for i in range(N):
    arr.append(i)

#some benchmark test
s = 0
for x in arr:
    s += x

end=time.perf_counter()
print(f"Array Time: {end-start} seconds")


#using the numpy libraries 
start=time.perf_counter()

np_arr=np.arange(N, dtype=np.int64)
s=np_arr.sum()

end=time.perf_counter()
print(f"Numpy array time: {end-start} seconds")