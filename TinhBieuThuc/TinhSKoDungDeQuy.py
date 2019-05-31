#Tinh S = x + x^2/2! + x^3/3! + ... + x^n/n!
import math
x = int(input("Nhập x= "))
n = int(input("Nhập n= "))
s = 0.0
for i in range (1, n+1):
    tu = x**i
    mau = 1
    for j in range(1, i+1):
        mau *= j
    s += tu/mau
s = round(s, 5)
print("S({0},{1}) = {2}".format(x,n,s))