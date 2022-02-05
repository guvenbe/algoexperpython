import ctypes
import sys

a = [1 ,2, 4]
id(a)
print(sys.getrefcount(a))

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(a)))
b = a
print(ref_count(id(a)))
