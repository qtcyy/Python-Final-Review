n = input()
tot = 0

while n:  # 空字符串为False
    tot += eval(n)  # 转换为int类型并累加
    n = input()  # 再输入

print(tot)
