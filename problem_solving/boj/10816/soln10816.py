"""
# 백준
# No. 10816
# Python 3.11.9
# by "nno0obb"
"""

from collections import Counter


def main():
    # Input
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))

    # Logic
    counter = Counter(A)
    ans = [counter[b] for b in B]

    # Output
    print(*ans, sep=" ")


if __name__ == "__main__":
    main()
