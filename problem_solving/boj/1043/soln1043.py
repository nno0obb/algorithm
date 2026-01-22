"""
# 백준
# No. 1043
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque


def main():
    # Input
    N, M = map(int, input().split())
    truth_tellers = list(map(int, input().split()))[1:]
    parties = [list(map(int, input().split()))[1:] for _ in range(M)]

    # Logic
    parties = deque(parties)
    P = list(range(N + 1))
    TRUTH_TELLER = 0  # P[0] = 0 <-- Always Truth Teller

    def find(x: int) -> int:
        if P[x] != x:
            P[x] = find(P[x])
        return P[x]

    def union(x: int, y: int):
        a = find(min(x, y))
        b = find(max(x, y))
        if a != b:
            P[b] = a

    for truth_teller in truth_tellers:
        union(truth_teller, TRUTH_TELLER)

    prev, curr = -1, len(parties)
    while parties and prev != curr:
        prev = curr
        for _ in range(len(parties)):
            party = parties.popleft()
            can_lie = True
            for person in party:
                if find(person) == TRUTH_TELLER:
                    can_lie = False
                    break
            if can_lie:
                parties.append(party)
            else:
                for person in party:
                    union(person, TRUTH_TELLER)
        curr = len(parties)

    ans = len(parties)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
