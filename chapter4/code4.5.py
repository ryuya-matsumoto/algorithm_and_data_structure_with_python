def func(N: int) -> int:
    if N == 0:
        return 0
    elif N == 1:
        return 1
    return func(N-1) + func(N-2)