def func(N: int) -> int:
    if N == 0:
        return 0
    return N + func(N-1)

print(str(func(5))) # 15