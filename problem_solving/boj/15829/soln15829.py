"""
# 백준
# No. 15829
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    L = int(input())
    S = input()

    # Logic
    r, M = 31, 1234567891
    ans = 0
    for i in range(L):
        a = ord(S[i]) - ord("a") + 1
        ans += a * r**i
        ans %= M

    # Output
    print(ans)


if __name__ == "__main__":
    main()
