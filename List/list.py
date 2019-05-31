import random
# khai báo 1 mảng rỗng:
from random import randrange

arr = []
print(len(arr))
# Khởi tạo các giá trị cho mảng:
arr = [1,2,3, "Nguyễn Ngọc Hải"] # Một mảng trong Python có thể chứa nhiều kiểu dữ liệu khác nhau
print("arr[1] =",arr[1])
for i in arr:
    print(i)

# Cách duyệt mảng: Có 2 cách duyệt mảng
#Duyệt theo collection:

print("="*50)
list = [1,2,3,4,5,6,7,8,9]
print("Duyệt theo Collection:")
for i in list:
    print(i, end='\t')
print("\n")

#Duyệt theo index:
print("Duyệt theo index:")
for i in range(len(list)):
    x = list[i]
    print(x, end='\t')

#Duyệt ngược mảng:
print('\n')
print("Duyệt ngược mảng:")
for i in range(len(list)-1,-1,-1):
    print(list[i], end='\t')

#Khởi tạo 1 mảng chứa các phần tử ngẫu nhiên

print("\n")
print("="*50)
n = int(input("Nhập n: "))
arr1 = [0]*n
for i in range(n):
    arr1[i] = randrange(-100,100)
print(arr1)
