"""
# 백준
# No. 9252
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A = input()
    B = input()

    # Logic
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    for i, a in enumerate(A, start=1):
        for j, b in enumerate(B, start=1):
            if a == b:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j, lcs = len(A), len(B), ""
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            lcs += A[i - 1]
            i -= 1
            j -= 1
    lcs = lcs[::-1]

    ans = [dp[len(A)][len(B)], lcs]

    # Output
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
