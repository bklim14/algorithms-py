def max_pairwise_product(numbers):

    first_index, first_max = 0, 0
    for index, first in enumerate(numbers):
        if first > first_max:
            first_index, first_max = index, first

    second_max = 0
    for index, second in enumerate(numbers):
        if index != first_index and second > second_max:
            second_max = second

    return first_max*second_max


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers[:input_n]))
