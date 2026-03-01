"""
# 백준
# No. 1966
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque


def main():
    # Input
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        W = list(map(int, input().split()))

        # Logic
        que = deque(list(zip(W, range(N))))
        stack = list(sorted(W))
        cnt = 0

        while que:
            cw, cdx = que.popleft()
            if cw == stack[-1]:
                cnt += 1
                if cdx == M:
                    ans = cnt
                    break
                stack.pop()
            else:
                que.append((cw, cdx))

        # Output
        print(ans)


if __name__ == "__main__":
    main()
