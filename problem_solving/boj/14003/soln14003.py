"""
# 백준
# No. 14003
# Python 3.11.9
# by "nno0obb"
"""

from bisect import bisect_left


def main():
    # Input
    N = int(input())
    A = list(map(int, input().split()))

    # Logic
    dp1 = [0] * N
    dp2 = [0] * N

    dp1[0] = 1
    dp2[0] = A[0]
    max_len = 1

    for i in range(1, N):
        if A[i] > dp2[max_len - 1]:
            max_len += 1
            dp1[i] = max_len
            dp2[max_len - 1] = A[i]
        else:
            idx = bisect_left(dp2, A[i], lo=0, hi=max_len)
            dp2[idx] = A[i]
            dp1[i] = idx + 1

    ans = []
    for i in range(N - 1, -1, -1):
        if dp1[i] == max_len:
            ans.append(A[i])
            max_len -= 1

    # Output
    print(max(dp1))
    print(*ans[::-1])


if __name__ == "__main__":
    main()
