n = int(input("Nhập chiều cao: "))
for i in range(n):
    for j in range(n):
        if j == n-1:
            print("*", end="")
        else:
            print("", end='')