"""
# 백준
# No. 21568
# Python 3.11.9
# by "nno0obb"
"""

from math import gcd


def sol(a, b):
    if b == 0:
        return 1, 0  # x, y

    q, r = divmod(a, b)
    _x, _y = sol(b, a % b)
    return _y, _x - q * _y


def main():
    # Input
    A, B, C = map(int, input().split())

    # Logic
    _gcd = gcd(A, B)
    x, y = -1, ""
    if C % _gcd == 0:
        x, y = sol(A, B)
        x *= C // _gcd
        y *= C // _gcd

    # Output
    print(x, y)

    # Hint
    # (x, y) = (_y, _x - _y * q)
    # ----------------------------------------------
    #             (q, r) -...-> (x, y)
    # 5x + 9y = 1 (0, 5) ----> (2, -1) # 9y = 1 - 5x
    # 9x + 5y = 1 (1, 4) ---> (-1, 2)  # 5y = 1 - 9x
    # 5x + 4y = 1 (1, 1) --> (1, -1)   # 4y = 1 - 5x
    # 4x + 1y = 1 (4, 0) -> (0, 1)     # 1y = 1 - 4x
    # ----------------------------------------------
    # 유클리드 호제법상 마지막에는 무조건 나머지가 0 이므로
    # x=0 으로 설정하면 y=1 로 시작할 수 밖에 없음


if __name__ == "__main__":
    main()
