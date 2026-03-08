"""
# 백준
# No. 14940
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque


def main():
    # Input
    n, m = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(n)]

    # Logic
    A = [[-1] * m for _ in range(n)]
    que = deque()
    is_visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if B[i][j] == 2 or B[i][j] == 0:
                A[i][j] = 0

            if B[i][j] == 2:
                que.append((i, j, 0))
                is_visited[i][j] = True

    while que:
        cy, cx, cd = que.popleft()

        for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < m:
                if B[ny][nx] == 1 and not is_visited[ny][nx]:
                    is_visited[ny][nx] = True
                    A[ny][nx] = cd + 1
                    que.append((ny, nx, cd + 1))

    # Output
    for i in range(n):
        print(*A[i])


if __name__ == "__main__":
    main()
