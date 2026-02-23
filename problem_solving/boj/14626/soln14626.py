"""
# 백준
# No. 14626
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    ISBN = input()

    # Logic
    remainder = 0
    for i, num in enumerate(ISBN):
        weight = 1 + (i % 2) * 2
        if num.isdigit():
            remainder += int(num) * weight
    remainder %= 10
    ans = 10 - remainder if remainder != 0 else 0

    # Output
    print(ans)


if __name__ == "__main__":
    main()
