"""
# 백준
# No. 2162
# Python 3.11.9
# by "nno0obb"
"""

import sys
from collections import defaultdict, deque
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    p1: Point
    p2: Point

    def ccw(self, p3):
        v1 = (self.p2.x - self.p1.x, self.p2.y - self.p1.y)
        v2 = (p3.x - self.p1.x, p3.y - self.p1.y)
        cross_product = v1[0] * v2[1] - v1[1] * v2[0]
        return cross_product

    def is_meet(self, l2):
        r1 = self.ccw(l2.p1)
        r2 = self.ccw(l2.p2)
        r3 = l2.ccw(self.p1)
        r4 = l2.ccw(self.p2)
        if r1 * r2 == 0 and r3 * r4 == 0:
            return (
                min(self.p1.x, self.p2.x) <= max(l2.p1.x, l2.p2.x)
                and min(l2.p1.x, l2.p2.x) <= max(self.p1.x, self.p2.x)
                and min(self.p1.y, self.p2.y) <= max(l2.p1.y, l2.p2.y)
                and min(l2.p1.y, l2.p2.y) <= max(self.p1.y, self.p2.y)
            )
        else:
            return r1 * r2 <= 0 and r3 * r4 <= 0


def main():
    # Input
    N = int(input())
    L = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        l = Line(Point(x1, y1), Point(x2, y2))
        L.append(l)

    # Logic
    G = defaultdict(list)

    for i in range(N):
        for j in range(i + 1, N):
            if L[i].is_meet(L[j]):
                G[i].append(j)
                G[j].append(i)

    que = deque()
    is_visited = [False] * N
    ans = [0, 0]
    for i in range(N):
        if not is_visited[i]:
            ans[0] += 1
            cnt = 1
            que.append(i)
            is_visited[i] = True
            while que:
                c = que.popleft()
                for n in G[c]:
                    if not is_visited[n]:
                        que.append(n)
                        is_visited[n] = True
                        cnt += 1
            ans[1] = max(ans[1], cnt)

    # Output
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
