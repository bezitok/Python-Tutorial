import math
print("Chương trinh giải phương trình bậc hai")
a = int(input("Nhập a>0: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
d = b*b - 4*a*c
if d<0:
    print("Phương trình vô nghiệm")
elif d == 0:
    x = float((-b) / 2 * a)
    print("Phương trình có nghiệm kép là: x = ", x)
else:
    x1 = ((-b) + math.sqrt(d)) / (2 * a)
    x2 = ((-b) - math.sqrt(d)) / (2 * a)
    print("Phương trình có 2 nghiệm phân biệt là: x1 = ", x1, " x2 = ", x2)
