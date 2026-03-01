"""
# 백준
# No. 2292
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    ans, ofs, k = 1, 1, 1
    while ofs < N:
        ofs += 6 * k
        k += 1
        ans += 1

    # Output
    print(ans)

    # Hint
    # 1 7  19  37  61 ... (val)
    #  6 12  18  24 ...  (diff)


if __name__ == "__main__":
    main()
