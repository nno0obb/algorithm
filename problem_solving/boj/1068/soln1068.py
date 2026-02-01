"""
# 백준
# No. 1068
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque


def main():
    # Input
    N = int(input())
    P = list(map(int, input().split()))
    D = int(input())

    # Logic
    G = [[] for _ in range(N)]
    R = None
    for i, p in enumerate(P):
        if p == -1:
            R = i
        else:
            G[p].append(i)

    que = deque()

    if R != D:
        que.append(R)

    ans = 0
    while que:
        c = que.popleft()
        if D in G[c]:
            G[c].remove(D)
        if not G[c]:
            ans += 1
        else:
            for n in G[c]:
                if n != D:
                    que.append(n)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
