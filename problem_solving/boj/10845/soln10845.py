"""
# 백준
# No. 10845
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    Q = [sys.stdin.readline().strip() for _ in range(N)]

    # Logic
    que = []
    for q in Q:
        cmd, *args = q.split()
        if cmd == "push":
            num = int(args[0])
            que.append(num)
        elif cmd == "pop":
            # Output
            if que:
                print(que.pop(0))
            else:
                print(-1)
        elif cmd == "size":
            # Output
            print(len(que))
        elif cmd == "empty":
            # Output
            print(0 if que else 1)
        elif cmd == "front":
            # Output
            if que:
                print(que[0])
            else:
                print(-1)
        elif cmd == "back":
            # Output
            if que:
                print(que[-1])
            else:
                print(-1)


if __name__ == "__main__":
    main()
