# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
datas = range(1, 5)
count = 0

for i in datas:
    for j in datas:
        for x in datas:
            for z in datas:
                if (i != j) and (j != x) and (x != z):
                    count += 1
                    num = i * 1000 + j * 100 + x * 10 + z
                    print(num)
print('totalCount:', count)
