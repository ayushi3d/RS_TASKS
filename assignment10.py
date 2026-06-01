import numpy as np
a=np.array([[26,12,5],[17,11,5]])
print("ARRAY:")
print(a)
print("\nshape:",a.shape)
print("\nsize:",a.size)
print("\ndim:",a.ndim)
print("\ndtype:",a.dtype)
b=a.astype(complex)
print("\nnew array with complex data type:")
print(b)
#can we use a[:,1] to slice 1D array?
#no, we cannot use a[:,1] to slice a 1D array because it is not a 2D array.
#The slicing syntax a[:,1] is used for 2D arrays to select all rows and the second column. 
# a 1D array has only 1 axis, so it does not support this type of slicing.