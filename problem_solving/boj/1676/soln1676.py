"""
# 백준
# No. 1676
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    i = int(input())

    # Logic
    _2, _5 = 0, 0
    for i in range(1, i + 1):
        num = i
        while True:
            if num % 2 == 0:
                _2 += 1
                num //= 2
            elif num % 5 == 0:
                _5 += 1
                num //= 5
            else:
                break

    ans = min(_2, _5)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
