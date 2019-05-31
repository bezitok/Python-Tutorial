from random import randrange

print("CHƯƠNG TRÌNH XỬ LÝ LIST")
print("="*50)
n = int(input("Nhập số lượng các phần tử: "))
arr = [0]*n
for i in range(n):
    arr[i] = randrange(-100,100)
print("Mảng ngẫu nhiên là: \n",arr)
print("="*50)
k = int(input("Nhập phần tử cần xóa: "))
for i in range(len(arr)):
    if k!= arr[i]:
        print(k,"không tồn tại trong mảng")
        break
    else:
        while arr.count(k):
            arr.remove(k)
        print("Mảng sau khi xóa là: \n", arr)
print("="*50)
value = int(input("Nhập giá trị thêm: "))
arr.append(value)
for i in range(len(arr)):
    if arr[i] == arr[len(arr)-i-1]:
        print("Đây là list đối xứng")
        break
    else:
        print("Đây là list không đối xứng")
        break