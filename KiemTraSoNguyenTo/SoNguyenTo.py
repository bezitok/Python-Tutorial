while True:
    n = float(input("Nhập n: "))
    kt = 0
    for i in range (2,int(n/2)+1):
        if n%i == 0:
            kt = 1
            break
    if kt == 0:
        print("n là số nguyên tố")
    elif kt == 1:
        print("n ko là số nguyên tố")
    hoi = input("Do you want to continue? Y/N ")
    if hoi is  "n":
        break
print("Thank you")
