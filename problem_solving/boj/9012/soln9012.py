"""
# 백준
# No. 9012
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    T = int(input())
    for _ in range(T):
        S = input()

        # Logic
        is_vps = True
        stack = []
        for c in S:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    is_vps = False
                    break
        if stack:
            is_vps = False

        # Output
        print("YES" if is_vps else "NO")


if __name__ == "__main__":
    main()
