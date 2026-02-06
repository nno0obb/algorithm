"""
# 백준
# No. 1463
# Python 3.11.9
# by "nno0obb"
"""

from collections import defaultdict, deque


def main():
    # Input
    N = int(input())

    # Logic
    dp = defaultdict(int)
    que = deque()
    que.append(N)

    dp[N] = 0
    ans = -1
    while que:
        c = que.popleft()
        if c == 1:
            ans = dp[c]
            break

        if c % 3 == 0:
            if c // 3 not in dp:
                dp[c // 3] = dp[c] + 1
                que.append(c // 3)

        if c % 2 == 0:
            if c // 2 not in dp:
                dp[c // 2] = dp[c] + 1
                que.append(c // 2)

        if c - 1 not in dp:
            dp[c - 1] = dp[c] + 1
            que.append(c - 1)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
