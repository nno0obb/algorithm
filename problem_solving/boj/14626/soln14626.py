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
    remainder, idx_damaged = 0, -1
    for idx, num in enumerate(ISBN):
        weight = 1 + (idx % 2) * 2
        if num.isdigit():
            remainder += int(num) * weight
        elif num == "*":
            idx_damaged = idx
    remainder %= 10
    ans = 10 - remainder if remainder != 0 else 0
    if idx_damaged % 2 == 1:
        ans = {
            0: 0,
            1: 7,
            2: 4,
            3: 1,
            4: 8,
            5: 5,
            6: 2,
            7: 9,
            8: 6,
            9: 3,
        }[ans]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
