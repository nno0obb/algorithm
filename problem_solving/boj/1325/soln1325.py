"""
# 백준
# No. 1325
# Python 3.11.9 (PyPy3)
# by "nno0obb"
"""

import sys
from collections import deque


def main():
    # Input
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().strip().split())
        G[B].append(A)

    # Logic
    cands = set(range(1, N + 1))
    for i in range(1, N + 1):
        if not G[i]:
            cands.remove(i)

    ans, max_cnt = [], -1
    for cand in cands:
        is_visited = [False] * (N + 1)
        que = deque()

        que.append(cand)
        is_visited[cand] = True
        cnt = 1
        while que:
            c = que.popleft()
            for n in G[c]:
                if not is_visited[n]:
                    que.append(n)
                    is_visited[n] = True
                    cnt += 1
        if cnt > max_cnt:
            ans, max_cnt = [cand], cnt
        elif cnt == max_cnt:
            ans.append(cand)

    # Output
    print(*ans)


if __name__ == "__main__":
    main()
