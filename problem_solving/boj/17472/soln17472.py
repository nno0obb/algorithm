"""
# 백준
# No. 17472
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque


def main():
    # Input
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]

    # Logic
    islands: list[tuple[int, int]] = []
    is_visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if B[i][j] == 1 and not is_visited[i][j]:

                que = deque()
                island = []

                que.append((i, j))
                is_visited[i][j] = True
                island.append((i, j))

                while que:
                    cy, cx = que.popleft()
                    for dy, dx in [(-1, 0), (0, -1), (+1, 0), (0, +1)]:
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < N and 0 <= nx < M:
                            if B[ny][nx] == 1 and not is_visited[ny][nx]:
                                que.append((ny, nx))
                                is_visited[ny][nx] = True
                                island.append((ny, nx))

                islands.append(island)

    for no, island in enumerate(islands, start=1):
        for y, x in island:
            B[y][x] = no

    edges = []
    for no, island in enumerate(islands, start=1):
        que = deque()
        is_visited: set[tuple[int, int, int, int]] = set()
        for y, x in island:
            for dy, dx in [(-1, 0), (0, -1), (+1, 0), (0, +1)]:
                ay, ax = y + dy, x + dx
                if 0 <= ay < N and 0 <= ax < M:
                    if B[ay][ax] == 0 and (ay, ax, dy, dx) not in is_visited:
                        que.append((ay, ax, dy, dx, no, 1))
                        is_visited.add((ay, ax, dy, dx))

        while que:
            cy, cx, dy, dx, cno, cl = que.popleft()
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < M:
                if B[ny][nx] == 0 and (ny, nx, dy, dx) not in is_visited:
                    que.append((ny, nx, dy, dx, cno, cl + 1))
                    is_visited.add((ny, nx, dy, dx))
                elif B[ny][nx] > 0 and B[ny][nx] != cno and cl >= 2:
                    edges.append((cno, B[ny][nx], cl))
                    continue

    edges.sort(key=lambda x: x[2])

    P = list(range(len(islands) + 1))

    def find(x: int) -> int:
        if P[x] != x:
            P[x] = find(P[x])
        return P[x]

    def union(x: int, y: int) -> None:
        a = find(x)
        b = find(y)
        if a != b:
            P[b] = a

    ans = 0
    for i1, i2, bridge_len in edges:
        if find(i1) != find(i2):
            union(i1, i2)
            ans += bridge_len

    is_impossible = False
    for i in range(2, len(islands) + 1):
        if find(i) != find(1):
            is_impossible = True
            break

    if is_impossible:
        ans = -1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
