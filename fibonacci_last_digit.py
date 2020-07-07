# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_fast(number):
    if number <= 1:
        return number

    index, prev1, prev2 = 2, 0, 1
    while index <= number:
        prev1, prev2 = prev2, (prev1+prev2) % 10
        index += 1

    return prev2


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_fast(n))
