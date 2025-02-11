def main():
    N = int(input("Nを入力してください"))
    h = list(map(int, input("{}個の数字を空白区切りで入力してください".format(N)).split()))

    dp = [float('inf')] * N
    dp[0] = 0
    for i in range(1, N):
        if i == 1:
            dp[i] = abs(h[i] - h[i - 1])
            print(dp[i])
        else:
            dp[i] = min([dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2])])
            print(dp[i])

    print(dp[N - 1])

if __name__ == "__main__":
    main()