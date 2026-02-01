"""
# 백준
# No. 1991
# Python 3.11.9
# by "nno0obb"
"""

from collections import defaultdict, deque


def main():
    # Input
    N = int(input())
    A = [input().split() for _ in range(N)]

    # Logic
    G = defaultdict(list)
    for p, l, r in A:
        G[p] = [l, r]

    T = defaultdict(str)

    que = deque()
    que.append((0, "A"))
    T[0] = "A"

    while que:
        idx, c = que.popleft()
        l, r = G[c]
        if l != ".":
            T[idx * 2 + 1] = l
            que.append((idx * 2 + 1, l))
        if r != ".":
            T[idx * 2 + 2] = r
            que.append((idx * 2 + 2, r))

    pre, _in, post = [], [], []

    def dfs(idx: int) -> None:
        pre.append(T[idx])

        ldx, rdx = 2 * idx + 1, 2 * idx + 2

        if ldx in T:
            dfs(ldx)

        _in.append(T[idx])

        if rdx in T:
            dfs(rdx)
        post.append(T[idx])

    dfs(0)

    # Output
    print("".join(pre))
    print("".join(_in))
    print("".join(post))


if __name__ == "__main__":
    main()
