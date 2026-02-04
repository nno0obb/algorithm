"""
# 백준
# No. 1722
# Python 3.11.9
# by "nno0obb"
"""

import math


def main():
    # Input
    N = int(input())
    Q = list(map(int, input().split()))

    # Logic
    ans = None
    if Q[0] == 1:
        K = Q[1] - 1
        ans = []
        A = list(range(1, N + 1))
        offset = math.factorial(N)
        for i in range(N, 0, -1):
            offset //= i
            q, r = divmod(K, offset)
            ans.append(A.pop(q))
            K = r

    elif Q[0] == 2:
        K = Q[1:]
        ans = 0
        A = list(range(1, N + 1))
        offset = math.factorial(N)
        for i, k in enumerate(K):
            offset //= N - i
            ans += A.index(k) * offset
            A.remove(k)
        ans += 1

    # Output
    print(*ans if isinstance(ans, list) else [ans])


if __name__ == "__main__":
    main()
