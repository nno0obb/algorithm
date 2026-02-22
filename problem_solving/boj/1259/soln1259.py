"""
# 백준
# No. 1259
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    while True:
        num = input()
        if num == "0":
            break

        # Logic
        ans = "yes" if num == num[::-1] else "no"

        # Output
        print(ans)


if __name__ == "__main__":
    main()
