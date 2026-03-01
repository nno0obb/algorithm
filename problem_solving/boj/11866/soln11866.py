"""
# 백준
# No. 11866
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque


def main():
    # Input
    N, K = map(int, input().split())

    # Logic
    deq = deque(range(1, N + 1))
    ans_lst, idx = [], 0
    for _ in range(N):
        idx += K - 1
        idx %= len(deq)
        ans_lst.append(str(deq[idx]))
        del deq[idx]
    ans_str = ", ".join(ans_lst)
    ans = f"<{ans_str}>"

    # Output
    print(ans)


if __name__ == "__main__":
    main()
