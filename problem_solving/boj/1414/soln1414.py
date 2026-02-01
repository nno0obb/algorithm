"""
# 백준
# No. 1414
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = [input() for _ in range(N)]

    # Logic
    edges = []
    for i in range(N):
        for j in range(N):
            if A[i][j] != "0":
                if i == j:
                    continue

                if "a" <= A[i][j] <= "z":
                    edge = (i, j, ord(A[i][j]) - ord("a") + 1)
                elif "A" <= A[i][j] <= "Z":
                    edge = (i, j, ord(A[i][j]) - ord("A") + 27)
                else:
                    raise RuntimeError()

                edges.append(edge)

    all_len = 0
    for i in range(N):
        for j in range(N):
            if A[i][j] != "0":
                if "a" <= A[i][j] <= "z":
                    all_len += ord(A[i][j]) - ord("a") + 1
                elif "A" <= A[i][j] <= "Z":
                    all_len += ord(A[i][j]) - ord("A") + 27
                else:
                    raise RuntimeError()

    P = list(range(N))

    def find(x: int) -> int:
        if P[x] != x:
            P[x] = find(P[x])
        return P[x]

    def union(x: int, y: int) -> None:
        a = find(min(x, y))
        b = find(max(x, y))
        if a != b:
            P[b] = a

    edges.sort(key=lambda x: x[::-1])

    ans = all_len
    for a, b, c in edges:
        if find(a) != find(b):
            union(a, b)
            ans -= c

    is_connected = True
    for i in range(1, N):
        if find(i) != find(0):
            is_connected = False
            break

    # Output
    print(ans if is_connected else -1)


if __name__ == "__main__":
    main()
