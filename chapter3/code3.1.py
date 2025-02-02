n = int(input('nの値を入力してください: '))
v = int(input('vの値を入力してください: '))

a = [ int(input('{}番目の数字を入力してください: '.format(i+1))) for i in range(n)]

exist = False

for i in range(n):
    if a[i] == v:
        exist = True

if exist:
    print('Yes')
else:
    print('No')