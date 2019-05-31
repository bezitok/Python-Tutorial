from random import randrange

print("GAME ĐOÁN SỐ")
while True:
    somay = randrange(0, 101)
    print("Máy tính đã tạo ra 1 số ngẫu nhiên trong khoảng [0..100]")
    print("Bạn hãy đoán nó trong vòng 7 lần. Nếu quá 7 lần bạn sẽ thua")
    solandoan = 0
    while solandoan<7:
        songuoi = int(input("Bạn đoán số gì?\n"))
        solandoan += 1
        if songuoi == somay:
            print("Bạn đã đoán đúng. Chúc mừng")
            break
        elif songuoi<somay:
            print("Số bạn đoán nhỏ hơn đáp án")
        else:
            print("Số bạn đoán lớn hơn đáp án")
        if solandoan==7:
            print("Đã hết 7 lượt đoán")
            print("GAME OVER")
            print("Đáp án là: ", somay)
            break
    answer = input("Do you want to continue? Press N to exit\n")
    if answer == 'n' or answer == 'N':
        print("Thank you")
        exit()
