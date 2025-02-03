memo = []
def main():
    # メモ化テーブルを-1で初期化する
    memo.extend([-1] * 50)
    fibo(49)
    for i in range(2, 50):
        print(i, '項目 =', memo[i])

def fibo(n):
    # ベースケース
    if n <= 1:
        return n
    # メモをチェック(すでに計算済みならば答えをリターンする)
    if memo[n] != -1:
        return memo[n]
    # メモ化しながら再帰呼び出し
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

if __name__ == '__main__':
    main()