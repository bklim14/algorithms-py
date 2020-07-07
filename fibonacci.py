# Uses python3
def calc_fibonacci_naive(number):
    if number <= 1:
        return number

    return calc_fibonacci_naive(number - 1) + calc_fibonacci_naive(number - 2)


def calc_fibonacci_fast(number):
    if number <= 1:
        return number

    index, prev1, prev2 = 2, 0, 1
    while index <= number:
        prev1, prev2 = prev2, prev1+prev2
        index += 1

    return prev2


if __name__ == '__main__':
    n = int(input())
    # print("Slow ", calc_fibonacci_naive(n))
    print(calc_fibonacci_fast(n))
