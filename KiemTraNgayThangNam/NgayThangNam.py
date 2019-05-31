thang = int(input("Nhập tháng: \n"))
nam = int(input("Nhập năm: \n"))
if thang in(1, 3, 5, 7, 8, 10, 12):
    print("Tháng",thang,"năm",nam,"có 31 ngày")
elif thang in (4, 6, 9, 11):
    print("Tháng",thang,"năm",nam,"có 30 ngày")
elif thang == 2:
    if nam % 4 == 0 or nam % 400 == 0 and nam % 100 != 0:
        print("Tháng",thang,"năm",nam," có 29 ngày")
    else:
        print("Tháng",thang,"năm",nam,"có 28 ngày")