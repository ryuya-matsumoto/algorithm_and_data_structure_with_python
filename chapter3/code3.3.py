INF = 20000000

n = int(input('nの値を入力してください: '))

a = [ int(input('{}番目の数字を入力してください: '.format(i+1))) for i in range(n)]

min_value = INF
for i in range(n):
    if a[i] < min_value:
        min_value = a[i]

print(min_value)