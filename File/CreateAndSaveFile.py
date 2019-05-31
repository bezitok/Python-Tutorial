def LuuFile(path):
    file = open(path,'w',encoding='utf-8')
    file.writelines("2017604634; Nguyễn Ngọc Hải; 14/06/1999\n")
    file.writelines("2018604634; Hải Ngọc Nguyễn; 14/06/99")
    file.close()
LuuFile("CSDLHocSinh.txt")