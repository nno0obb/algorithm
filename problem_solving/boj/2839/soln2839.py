"""
# 백준
# No. 2839
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    ans = -1
    for i in range(N // 5, -1, -1):
        if (N - 5 * i) % 3 == 0:
            ans = i + (N - 5 * i) // 3
            break

    # Output
    print(ans)


if __name__ == "__main__":
    main()
