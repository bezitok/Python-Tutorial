from random import randrange

def CreateMatrix(m,n):
    arr = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(0,100))
        arr.append(row)
    return arr
def DisplayMatrix(arr):
    for row in arr:
        for element in row:
            print(element, end='\t')
        print()
def ChooseElement(r):
    R = arr[r]
    return R
def ChooseRow(c):
    C=[]
    for i in range(len(arr)):
        C.append(arr[i][c])
    return C
def DisplayList(R):
    for element in R:
        print(element,end='\t')
def Max(arr):
    max = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (max < arr[i][j]):
                max = arr[i][j]
    return max
m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))
arr = CreateMatrix(m,n)
DisplayMatrix(arr)
print('='*50)
r = int(input("Nhập dòng bạn muốn xuất: "))
DisplayList(ChooseElement(r))
print("\n")
print('='*50)
c = int(input("Nhập cột bạn muốn xuất: "))
DisplayList(ChooseRow(c))
print("\n")
print('='*50)
max = Max(arr)
print("Số lớn nhất trong list là: ",max)