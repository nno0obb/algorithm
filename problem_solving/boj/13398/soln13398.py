"""
# 백준
# No. 13398
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = list(map(int, input().split()))

    # Logic
    dp = [[0, 0] for _ in range(N)]
    dp[0][0] = A[0]
    ans = A[0]
    for i in range(1, N):
        dp[i][0] = max(dp[i - 1][0] + A[i], A[i])
        dp[i][1] = max(dp[i - 1][1] + A[i], A[i], dp[i - 1][0])
        ans = max(ans, dp[i][0], dp[i][1])

    # Output
    print(ans)


if __name__ == "__main__":
    main()
