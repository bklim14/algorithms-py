# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_fast(number, m):
    if number <= 1:
        return number

    seq = [0, 1]
    index, prev1, prev2 = 2, 0, 1
    while index <= number:
        seq.append((prev1+prev2) % m)
        if seq[index - 1] == 0 and seq[index] == 1:
            index = number % (len(seq) - 2)
            return seq[index]

        prev1, prev2 = prev2, prev1+prev2
        index += 1
    return seq[index-1]


if __name__ == '__main__':
    n, m = map(int, input().split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n, m))
