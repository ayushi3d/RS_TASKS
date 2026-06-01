"""#difference between dtype&astype"""
import numpy as np
a=np.array([1,2,3,4])
print("\n dtype")
print(a.dtype) #shows datatype of array
print("\n astype")
print(a.astype(complex)) #converts datatype of array from one to another
print("original array",a)