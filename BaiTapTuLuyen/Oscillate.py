def oscillate(a, b):
    for i in range(a, b):
        print(a, "\t", -a)
        a += 1
        if (a == b):
            break

try:
    for n in oscillate(-3, 5):
        print(n, end='\t')
    print()
except Exception:
    print("This is not a bug. This is feature")
