# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum_fast(number):
    if n <= 1:
        return n

    seq = [0, 1]
    index, prev1, prev2 = 2, 0, 1
    sum = 1
    while index <= number:
        prev1, prev2 = prev2, (prev1 + prev2) % 10
        sum = (sum + prev2) % 10
        seq.append(sum)
        if seq[index - 1] == 0 and seq[index] == 1:
            index = number % (len(seq) - 2)
            return seq[index]
        index+=1

    return seq[index-1]


if __name__ == '__main__':
    n = int(input())
    # print(fibonacci_sum_naive(n))
    print(fibonacci_sum_fast(n))
