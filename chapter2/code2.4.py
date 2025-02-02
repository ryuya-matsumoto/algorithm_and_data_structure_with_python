import math
# 2点（x1、y1）、（x2、y2）間の距離を求める関数
def calc_dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

n = int(input())
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

minimum_dist = 1000000000
for i in range(n):
    for j in range(i + 1, n):
        # (x[i], y[i]) と (x[j], y[j]) の距離を計算
        dist_i_j = calc_dist(x[i], y[i], x[j], y[j])

        # 暫定最小値 minimum_dist と dist_i_j を比べる
        minimum_dist = min(minimum_dist, dist_i_j)

print(minimum_dist)