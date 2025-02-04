def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))

    if func(n, w, a):
        print('Yes')
    else:
        print('No')

def func(i: int, w: int, a: list) -> bool:
    # Base case
    if i == 0:
        if w == 0:
            return True
        else:
            return False
    # a[i-1]を選ばない場合
    if func(i-1, w, a):
        return True
    # a[i-1]を選ぶ場合
    if func(i-1, w-a[i-1], a):
        return True
    
    # どちらもfalseの場合はfalse
    return False

if __name__ == '__main__':
    main()

