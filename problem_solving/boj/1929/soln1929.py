"""
# 백준
# No. 1929
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    M, N = map(int, input().split())

    # Logic
    P = [True] * (N + 1)
    P[0], P[1] = False, False
    for i in range(2, int(N**0.5) + 1):
        if P[i]:
            for j in range(i * i, N + 1, i):
                P[j] = False

    # Output
    for i in range(M, N + 1):
        if P[i]:
            print(i)


if __name__ == "__main__":
    main()
