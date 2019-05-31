from random import randrange

def SNT(n):
    if n < 2:
        return 0
    else:
        for i in range(2,n//2+1):
            if n%i == 0:
                return 0
    return 1


print("CHƯƠNG TRÌNH XỬ LÝ LIST")
n = int(input("Nhập số phần tử: "))
arr = [0]*n
for i in range(n):
    arr[i]=randrange(-100,100)
print("List ngẫu nhiên là:\n",arr)
print("="*50)
value = int(input("Mời bạn nhập phần tử mới: "))
arr.append(value)
print("Mảng mới là: \n", arr)
print("="*50)
k = int(input("Nhập vào giá trị muốn kiểm tra: "))
dem = arr.count(k)
if k == 0:
    print(k, "không tồn tại trong List")
else:
    print(k,"xuất hiện",dem,"lần trong List")
tong = 0
count = 0
print("="*50)
print("Các số nguyên tố trong List là: ")
for i in range(len(arr)):
    if SNT(arr[i]):
        print(arr[i],end='\t')
        count+=1
        tong += arr[i]
print("\nCó",count,"số nguyên tố trong List")
print("Tổng các số nguyên tố trong List là: ",tong)
print("="*50)
arr.sort()
print("Mảng đã được sắp xếp là: \n",arr)
print("="*50)
del arr
print("Mảng đã được xóa")






