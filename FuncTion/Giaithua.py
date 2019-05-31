def giaithua(n):
    """Hàm tính giai thừa"""
    if n<=1:
        return 1
    else:
        return n*giaithua(n-1)


