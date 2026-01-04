"""
# 백준
# No. 1747
# Python 3.11.9
# by "nno0obb"
"""

from bisect import bisect_left


def main():
    # Input
    N = int(input())

    # Logic
    A, MAX = [], 1_003_001
    P = [True] * (MAX + 1)
    P[0], P[1] = False, False
    for i in range(2, MAX + 1):
        if P[i]:
            if str(i) == str(i)[::-1]:
                A.append(i)
            for j in range(i * i, MAX + 1, i):
                P[j] = False

    ans = A[bisect_left(A, N)]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
