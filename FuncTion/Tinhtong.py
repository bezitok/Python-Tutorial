def tong(n):
    '''Hàm này dùng để tính tổng các số từ 1 đến n'''
    if(n==0):
        return n
    else:
        return n+tong(n-1)
