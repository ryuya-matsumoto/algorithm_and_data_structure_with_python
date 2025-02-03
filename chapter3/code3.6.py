n, w = map(int, input('数値NとWをスペース区切りで入力').split())
a = list(map(int, input('数列Aの要素をスペース区切りで{}個入力'.format(n)).split()))
exist = False

for bit in range(1 << n):
    sum = 0
    for i in range(n):
        if bit & (1 << i):
            sum += a[i]
    if sum == w:
        exist = True

if exist:
    print('Yes')
else:
    print('No')