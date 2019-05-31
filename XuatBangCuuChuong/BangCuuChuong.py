for j in range (1,11):
    for i in range (1,11):
        line = "{0}*{1} = {1:>2}".format(j,i, i*j)
        print(line,end='\t')
        print()