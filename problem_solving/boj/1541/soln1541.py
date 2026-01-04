"""
# 백준
# No. 1541
# Python 3.11.9
# by "nno0obb"
"""

import re


def main():
    # Input
    S = input()

    # Logic
    tokens = re.findall(r"(\d+|[+-])", S)
    tokens = list(map(lambda x: int(x) if x.isdigit() else x, tokens))

    ans, flag = 0, 1
    for i in range(len(tokens)):
        if tokens[i] == "-":
            flag = -1
        elif tokens[i] == "+":
            pass
        else:
            ans += flag * tokens[i]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
