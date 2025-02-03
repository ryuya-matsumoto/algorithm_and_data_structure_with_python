def main():
    print(func(5))

def func(N: int) -> int:
    print('func({})を呼び出しました'.format(N))
    if N == 0:
        return 0
    result = N + func(N-1)
    print(N, 'までの和 =', result)
    return result

if __name__ == '__main__':
    main()