"""
# 백준
# No. 28702
# Python 3.11.9
# by "nno0obb"
"""


def fizzbuzz(n: int):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def main():
    # Input
    S = [input() for _ in range(3)]

    # Logic
    num = None
    if S[0].isdigit():
        num = int(S[0]) + 3
    elif S[1].isdigit():
        num = int(S[1]) + 2
    elif S[2].isdigit():
        num = int(S[2]) + 1
    else:
        raise RuntimeError()

    ans = fizzbuzz(num)

    # Output
    print(ans)

    # Hint
    # FizzBuzz: 15x
    # Fizz:     15x + (3,6,9,12)
    # Buzz:     15x + (5, 10)
    # i:        15x + (1,2,4,7,8,11)


if __name__ == "__main__":
    main()
