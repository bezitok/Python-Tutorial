name = 'Nguyễn Ngọc Hải'

print("Tên của bạn viết bằng chữ in hoa: ",name.upper()) #Hàm chuyển chuỗi thành chữ hoa
print("Tên của bạn viết bằng chữ in thường: ",name.lower())  #Hàm chuyển chuỗi thành chữ thường

print(name.ljust(20, '^')) #Hàm canh lề trái
print(name.rjust(20,"@")) #Hàm canh lề phải
print(name.center(32,"-")) #Hàm canh giữa

print("="*50)

s = '          Tôi đẹp trai               '
print(s.__len__())#Đưa ra độ dài của chuỗi
print(s.strip()) #Hàm xóa khoảng trắng dư thừa

print("="*50)

f = '@Nguyenhaikiller%'
print(f.startswith('@'))#Kiểm tra xem chuỗi có bắt đầu bằng 1 kí tự nào đó ko, kết quả trả về là True hoặc False
print(f.startswith('%'))
print(f.endswith('%'))   #Kiểm tra xem chuỗi có kết thúc bằng 1 kí tự nào đó ko. kết quả trả về là True hoặc False


##################################################

#Hàm find trả về vị trí đầu tiên tìm thấy, nếu ko tìm thấy trả về giá trị -1

print("$"*50)
s = 'một con chó đang chạy rông ngoài đường'
print("Chữ cần tìm ở vị trí thứ", s.find('đ'))

##################################################
#Hàm rfind trả về giá trị cuối cùng tìm thấy, nếu ko tìm thấy trả về giá trị -1

print("Lần xuất hiện cuối cùng của kí tự cần tìm là", s.rfind('g'))

##################################################

#Hàm count trả về số lần xuất hiện của chuỗi con trong chuỗi gốc, nếu ko tìm thấy trả về giá trị 0

print("^"*50,"\n")
a = 'Hồn lỡ sa vào đôi mắt em'
print("Số lần xuất hiện chuỗi là:",a.count('m'))

##################################################

#Hàm format sử dụng {} để dành chỗ xuất dữ liệu

print("="*50)
x = 6
y = 8
z = x/y
print("{0}/{1}={2}".format(x,y,z))

#Hàm substring dùng để trích lọc chuỗi, thông qua index

chuoi = 'Hello World'
print(chuoi[2:]) #Trích toàn bộ kí tự đằng sau 2 kí tự đầu
print(chuoi[:2]) #Trích 2 kí tự đầu chuỗi

#Hàm split dùng để tách chuỗi

print("="*50)
v = 'Nguyễn Ngọc Hải, 14/06/1999, Nam'
arr = v.split(',') #tách chuỗi theo dấu ,
for x in arr:
    print(x)

#Hàm join dùng để nối chuỗi

s2 = ','
s2 = s2.join(arr) #Nỗi chuỗi theo dấu ,
print(s2)