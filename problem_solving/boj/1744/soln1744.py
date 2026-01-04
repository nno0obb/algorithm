"""
# 백준
# No. 1744
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = [int(input()) for _ in range(N)]

    # Logic
    P, _1, M = [], [], []
    for a in A:
        if a > 1:
            P.append(a)
        elif a == 1:
            _1.append(a)
        else:
            M.append(a)

    if len(P) % 2 != 0:
        P.append(1)
    if len(M) % 2 != 0:
        M.append(1)

    P.sort()
    M.sort()
    ans = 0
    for a, b in zip(P[::2], P[1::2]):
        ans += a * b
    for a, b in zip(M[::2], M[1::2]):
        ans += a * b
    ans += sum(_1)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
