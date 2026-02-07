"""
# 백준
# No. 2342
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A = list(map(int, input().split()))

    # Logic
    nums = A[:-1]

    def cost(_from, _to):
        if _from == 0:
            return 2
        elif _from == _to:
            return 1
        elif abs(_from - _to) == 2:
            return 4
        else:
            return 3

    dp = [[[float("inf")] * 5 for _ in range(5)] for _ in range(len(A))]
    dp[0][0][0] = 0
    ans = float("inf")
    for i, num in enumerate(nums, start=1):
        for j in range(5):
            for k in range(5):
                dp[i][j][num] = min(dp[i][j][num], dp[i - 1][j][k] + cost(k, num))
                dp[i][num][k] = min(dp[i][num][k], dp[i - 1][j][k] + cost(j, num))
                if i == len(A) - 1:
                    ans = min(ans, dp[i][j][num], dp[i][num][k])

    # Output
    print(ans)


if __name__ == "__main__":
    main()
