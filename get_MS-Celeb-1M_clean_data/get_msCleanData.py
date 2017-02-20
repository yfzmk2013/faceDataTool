# coding=utf-8
f = open("/home/yanhao/0_data/MS-Celeb-1M_clean_list.txt", "r")
n = 0
while True:
    line = f.readline()
    if line:
        # pass    # do something here
        n = n + 1
        print line.strip().split()
    else:
        break
f.close()
