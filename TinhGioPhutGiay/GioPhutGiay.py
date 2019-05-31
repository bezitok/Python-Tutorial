s = int(input("Nhập số giây bạn muốn chuyển đổi: \n"))
h = s//3600
m = (s-h*3600)//60
s1 = s - h*3600 - m*60
print("Chuyển thành: ",h, "h", m,"m", s1, "s")