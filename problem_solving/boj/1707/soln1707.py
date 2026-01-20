"""
# 백준
# No. 1707
# Python 3.11.9
# by "nno0obb"
"""

import sys
from collections import defaultdict, deque

# Gloval Variables
RED, BLUE = 1, ~1


def main():
    # Input
    K = int(input())
    for _ in range(K):
        V, E = map(int, input().split())
        G = defaultdict(list)
        for _ in range(E):
            u, v = map(int, sys.stdin.readline().strip().split())
            G[u].append(v)
            G[v].append(u)

        # Logic
        is_visited = [False] * (V + 1)
        que = deque()
        C = [None] * (V + 1)

        ans = "YES"
        for i in range(1, V + 1):
            if is_visited[i]:
                continue

            que.append((i, RED))
            is_visited[i] = True
            C[i] = RED

            while que:
                curr, color = que.popleft()
                for _next in G[curr]:
                    if not is_visited[_next]:
                        que.append((_next, ~color))
                        is_visited[_next] = True
                        C[_next] = ~color
                    elif C[_next] is not None:
                        if C[_next] == color:
                            ans = "NO"
                            break

            if ans == "NO":
                break

        # Output
        print(ans)


if __name__ == "__main__":
    main()
