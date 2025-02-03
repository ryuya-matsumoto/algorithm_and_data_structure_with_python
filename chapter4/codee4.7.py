def main():
    F = []
    F[0] = 0
    F[1] = 1
    for i in range(2, 50):
        F[i] = F[i-1] + F[i-2]
        print(i, '項目 =', F[i])