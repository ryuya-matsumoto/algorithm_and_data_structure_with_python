def main():
    fibo(6)

def fibo(N: int) -> int:
    # 再帰関数を呼び出したことを報告する
    print('fibo({})を呼び出しました'.format(N))
    # ベースケース
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    # 再帰的に答えを求めて出力する
    result = fibo(N-1) + fibo(N-2)
    print(N, '項目 =', result)
    return result

if __name__ == '__main__':
    main()