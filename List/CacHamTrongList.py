#Các hàm thường sử dụng trong List:
from random import randrange

arr = [1,2,3,4,5,6]

#Hàm Insert: dùng để chèn 1 phần tử x nào đó vào 1 vị trí thứ i nào đó trong mảng

print("Mảng ban đầu là:\n",arr)
arr.insert(3,8) #Chèn 8 vào vị trí thứ 3
print("Mảng sau khi chèn 8 vào vị trí thứ tư là:\n",arr) #Xuất lại mảng

#Hàm Append: dùng để chèn giá trị mới vào cuối danh sách

arr.append(7) #Chèn 7 vào cuối mảng
print("Mảng sau khi chèn 7 vào cuối là: \n",arr)

#Hàm Remove: xóa 1 phần tử x nào đó dựa trên giá trị của phần tử
#Nếu trong mảng có nhiều phần tử trùng nhau thì hàm Remove sẽ xóa đi phần tử đầu tiên được tìm thấy trong mảng

arr.remove(8) #Xóa phần tử có giá trị bằng 8
print("Mảng sau khi xóa bằng Remove là:\n",arr)

#Hàm Del cũng giống như hàm Remove, cũng dùng để xóa, tuy nhiên nó có thể xóa cùng lúc nhiều phần tử dựa trên index của các phần tử đó

del arr[6] #Xóa phần tử ở vị trí thứ 7
print("Mảng sau khi xóa bằng Del là:\n",arr)
del arr[1:5] #Xóa các phần tử từ vị trí thứ 2 đến vị trí thứ 5 trong mảng
print("Mảng sau khi xóa nhiều phần tử bằng Del là:\n",arr)

#Hàm Reverse dùng để đảo danh sách

arr.insert(1,2)
arr.insert(2,3)
print("Mảng trước khi đảo là:\n", arr)
arr.reverse()
print("Mảng sau khi đảo lại là:\n",arr)
arr.reverse()
print("Đảo lại mảng:\n",arr)

#Hàm Sort dùng để sắp xếp lại hàm

arr = [0]*10 #Mảng mới có 10 phần tử
for i in range(len(arr)):
    arr[i]=randrange(-100,100) #Tạo ra các phần tử ngẫu nhiên
print("Mảng mới là: \n",arr)
arr.sort()
print("Mảng sau khi được sắp xếp là:\n", arr)

#Hàm Slicing: trích lọc chuỗi
#Statement: list[begin,end,step]

print("Mảng mới:\n",arr[:2]) #Lấy 2 phần tử đầu tiên
print("Mảng mới:\n",arr[2:]) #Lấy toàn bộ danh sách từ vị trí thứ 3
print("Mảng mới:\n",arr[4:7]) #Phần tử đầu ở vị trí thứ 5, phần tử cuối ở vị trí thứ 7
print("Mảng mới:\n",arr[:]) #Lấy ra toàn bộ danh sách
print("Mảng mới:\n",arr[2:6:1]) #Trích lọc ra mảng có phần tử đầu ở vị trí thứ 3, phần tử cuối ở vị trí thứ 6, bước nhảy là 1
print("Mảng mới:\n",arr[::2]) #Trích lọc mảng có bước nhảy là 2, begin và end bỏ trống nên lấy từ phần tử đầu tiên của mảng