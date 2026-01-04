"""
# 백준
# No. 1016
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A, B = map(int, input().split())

    # Logic
    MAX, P = 1_000_000, []
    is_nono = [True] * (B - A + 1)
    is_prime = [True] * (MAX + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, MAX + 1):
        if is_prime[i]:
            P.append(i)
            for j in range(i * i, MAX + 1, i):
                is_prime[j] = False
            s = (A + i * i - 1) // (i * i) * (i * i)
            for j in range(s, B + 1, i * i):
                is_nono[j - A] = False

    ans = is_nono.count(True)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
