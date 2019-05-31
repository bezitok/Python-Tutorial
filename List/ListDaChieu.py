from random import randrange

# Cách khởi tạo List đa chiều:
#Tạo 1 mảng có m dòng, n cột:

row = 5 #Ma trận có 5 dòng
column = 3 #Ma trận có 3 cột
arr = [[0]*column]*row #khoải tạo ma trận
print(arr)

arr=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Duyệt ma trận:
print('='*50)
print("\nDuyệt mảng theo Collection:")
for row in arr:
    for column in row:
        print(column, end='\t')
    print()

# Tạo 1 ma trận có số dòng và số cột bất kì:

arr = []
print('='*50)
row = int(input("\nNhập số dòng: "))
column = int(input("Nhập số cột: "))
for i in range(row): #Khởi tạo các giá trị ngẫu nhiên cho ma trận trong phạm vi từ -100 đến 100
    onerow = []
    for j in range(column):
        onerow.append(randrange(-100,100))
    arr.append(onerow)
print("Ma trận do máy tạo ra ngẫu nhiên là:")
for i in range(len(arr)): #Xuất ma trận ra màn hình
    for j in range(len(arr[i])):
        print(arr[i][j], end='\t')
    print()