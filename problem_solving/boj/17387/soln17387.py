"""
# 백준
# No. 17387
# Python 3.11.9
# by "nno0obb"
"""

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def main():
    # Input
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    # Logic
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    p4 = Point(x4, y4)

    def ccw(p1, p2, p3):
        return p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p1.y * p2.x - p2.y * p3.x - p3.y * p1.x

    ccw1 = ccw(p1, p2, p3)
    ccw2 = ccw(p1, p2, p4)
    ccw3 = ccw(p3, p4, p1)
    ccw4 = ccw(p3, p4, p2)

    r1 = ccw1 * ccw2
    r2 = ccw3 * ccw4

    ans = None
    if r1 == 0 and r2 == 0:
        if (
            min(x1, x2) <= max(x3, x4)
            and min(x3, x4) <= max(x1, x2)
            and min(y1, y2) <= max(y3, y4)
            and min(y3, y4) <= max(y1, y2)
        ):
            ans = 1
        else:
            ans = 0
    elif r1 <= 0 and r2 <= 0:
        ans = 1
    else:
        ans = 0

    # Output
    print(ans)


if __name__ == "__main__":
    main()
