import math
try:
    r = float(input("Nhập bán kính hình tròn: \n"))
    p = float((2 * r) * math.pi)
    s = float(r * r * math.pi)
    print("Chu vi hình tròn là ", p)
    print("Diện tích hình tròn là: ",s)
except:
    print("bị lỗi")