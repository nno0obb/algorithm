"""
# 백준
# No. 4949
# Python 3.11.9
# by "nno0obb"
"""

import re


def main():
    # Input
    while True:
        S = input()
        if S == ".":
            break

        # Logic
        S = re.sub(r"[^\(\)\[\]]", "", S)
        stack, ans = [], True
        for c in S:
            if c in ["(", "["]:
                stack.append(c)
            else:
                if not stack:
                    ans = False
                    break
                elif c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    ans = False
                    break
        if stack:
            ans = False

        # Output
        print("yes" if ans else "no")


if __name__ == "__main__":
    main()
