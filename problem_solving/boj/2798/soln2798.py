"""
# 백준
# No. 2798
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # Logic
    A.sort()
    ans = -1
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if A[i] + A[j] + A[k] <= M:
                    ans = max(ans, A[i] + A[j] + A[k])
                else:
                    break

    # Output
    print(ans)


if __name__ == "__main__":
    main()
