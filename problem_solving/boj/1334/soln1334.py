"""
# 백준
# No. 1334
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = input()

    # Logic
    ans = -1
    if len(N) > 1:
        F1 = str(int(N[: (len(N) + 1) // 2]))
        C1 = F1 + F1[::-1][len(N) % 2 :]
        F2 = str(int(N[: (len(N) + 1) // 2]) + 1)
        C2 = F2 + F2[::-1][len(N) % 2 + len(F2) - len(F1) :]

        ans = int(C1)
        if ans <= int(N):
            ans = int(C2)
    elif int(N) < 9:
        ans = int(N) + 1
    elif int(N) == 9:
        ans = 11

    # Output
    print(ans)


if __name__ == "__main__":
    main()
