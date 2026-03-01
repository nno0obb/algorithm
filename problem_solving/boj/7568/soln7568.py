"""
# 백준
# No. 7568
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    # Logic
    R = [1] * N
    for i in range(N):
        for j in range(N):
            i_w, i_h = A[i]
            j_w, j_h = A[j]
            if i_w < j_w and i_h < j_h:
                R[i] += 1

    # Output
    print(*R)


if __name__ == "__main__":
    main()
