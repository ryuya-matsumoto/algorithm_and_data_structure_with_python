n = int(input('nの値を入力してください: '))
v = int(input('vの値を入力してください: '))

a = [ int(input('{}番目の数字を入力してください: '.format(i+1))) for i in range(n)]

exist = False
found_id = -1

for i in range(n):
    if a[i] == v:
        found_id = i #見つかったらそのインデックスを記録
        exist = True
        break

print(found_id)