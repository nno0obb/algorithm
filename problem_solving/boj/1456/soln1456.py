"""
# 백준
# No. 1456
# Python 3.11.9
# by "nno0obb"
"""

from math import sqrt


def main():
    # Input
    A, B = map(int, input().split())

    # Logic
    P = [True] * (int(sqrt(B)) + 1)
    P[0], P[1] = False, False
    for i in range(2, int(sqrt(B)) + 1):
        if P[i]:
            for j in range(i * i, int(sqrt(B)) + 1, i):
                P[j] = False

    ans = 0
    for i in range(2, int(sqrt(B)) + 1):
        if P[i]:
            offset = i * i
            while offset <= B:
                if offset >= A:
                    ans += 1
                offset *= i

    # Output
    print(ans)


if __name__ == "__main__":
    main()
