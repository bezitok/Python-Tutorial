from BaiTapXuLyFile import *

# masp = input("Nhập mã sản phẩm: ")
# tensp = input("Nhập tên sản phẩm ")
# dongia = float(input("Nhập giá: "))
# line = masp + ";" + tensp + ";" + str(dongia) + ";"
# LuuFile("database.txt", line)
arr = DocFile("database.txt")
def XuatSanPham(arr):
    for row in arr:
        for element in row:
            print(element, end='\n')
    print()
XuatSanPham(arr)