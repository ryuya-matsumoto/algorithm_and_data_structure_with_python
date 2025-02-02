# ペア和の最小値を求める
INF = 20000000

n, k = map(int, input('数値NとKをスペース区切りで入力').split())
a = list(map(int, input('数列Aの要素をスペース区切りで{}個入力'.format(n)).split()))
b = list(map(int, input('数列Bの要素をスペース区切りで{}個入力'.format(n)).split()))

min_value = INF
for i in range(n):
    for j in range(n):
        # 和がk未満の場合はスキップ
        if a[i] + b[j] < k:
            continue
        # それ以外の場合はmin_valueを更新
        if a[i] + b[j] < min_value:
            min_value = a[i] + b[j]

print(min_value)
