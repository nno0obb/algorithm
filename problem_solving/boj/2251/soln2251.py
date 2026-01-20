"""
# 백준
# No. 2251
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque


def main():
    # Input
    A, B, C = map(int, input().split())

    # Logic
    volumes = [A, B, C]

    que = deque()
    is_visited = set()
    ans = set()

    que.append([0, 0, C])
    is_visited.add(tuple([0, 0, C]))
    ans.add(C)
    while que:
        curr_waters = que.popleft()

        if curr_waters[0] == 0:
            ans.add(curr_waters[2])

        for src, dst in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]:
            _next_waters = curr_waters.copy()
            if curr_waters[src] + curr_waters[dst] <= volumes[dst]:
                _next_waters[dst] = curr_waters[src] + curr_waters[dst]
                _next_waters[src] = 0
            else:
                _next_waters[src] = curr_waters[src] + curr_waters[dst] - volumes[dst]
                _next_waters[dst] = volumes[dst]

            if tuple(_next_waters) not in is_visited:
                que.append(_next_waters)
                is_visited.add(tuple(_next_waters))

    # Output
    print(*sorted(ans))


if __name__ == "__main__":
    main()
