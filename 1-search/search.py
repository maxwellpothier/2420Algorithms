from random import seed, sample
from time import perf_counter
import math
import time

DATA_SIZE = 100000


def linear_search(lyst, target):
    for i in range(len(lyst)):
        if (lyst[i] == target):
            return True
    return False


def binary_search(lyst, target):
    min = 0
    max = len(lyst) - 1
    while min <= max:
        mid = (min + max) // 2
        if lyst[mid] == target:
            return True
        elif lyst[mid] < target:
            min = mid + 1
        else:
            max = mid - 1
    return False


def jump_search(lyst, target):
    incr = int(math.sqrt(len(lyst))) - 1
    curr = 0

    while target > lyst[curr]:
        curr = incr
        if curr >= len(lyst):
            return False

        incr += int(math.sqrt(len(lyst)))

    if target == lyst[curr]:
        return True

    for i in range(incr):
        if (lyst[curr - i] == target):
            return True
    return False


def make_data():
    seed(0)
    data = sample(range(DATA_SIZE), k=100)
    data.sort()
    while True:
        return data


def main():
    data = make_data()

    # First element of sorted array
    print('1.')

    print('Linear search for the first element...')
    start = time.perf_counter()
    result = linear_search(data, data[0])
    fastest = time.perf_counter() - start
    print(result, fastest)

    print('Binary search for the first element...')
    start = time.perf_counter()
    result = binary_search(data, data[0])
    fastest = time.perf_counter() - start
    print(result, fastest)

    print('Jump search for the first element...')
    start = time.perf_counter()
    result = jump_search(data, data[0])
    fastest = time.perf_counter() - start
    print(result, fastest)

    print('\n')

    # Number at the middle of the sorted array
    print('2.')

    print('Linear search for the middle element...')
    start = time.perf_counter()
    result = linear_search(data, data[(len(data) // 2) - 1])
    fastest = time.perf_counter() - start
    print(result, fastest)

    print('Binary search for the middle element...')
    start = time.perf_counter()
    result = binary_search(data, data[(len(data) // 2) - 1])
    fastest = time.perf_counter() - start
    print(result, fastest)

    print('Jump search for the middle element...')
    start = time.perf_counter()
    result = jump_search(data, data[(len(data) // 2) - 1])
    fastest = time.perf_counter() - start
    print(result, fastest)

    print('\n')

    # Last element of the sorted array
    print('3.')

    print('Linear search for the last element...')
    start = time.perf_counter()
    result = linear_search(data, data[-1])
    fastest = time.perf_counter() - start
    print(result, fastest)

    print('Binary search for the last element...')
    start = time.perf_counter()
    result = binary_search(data, data[-1])
    fastest = time.perf_counter() - start
    print(result, fastest)

    print('Jump search for the last element...')
    start = time.perf_counter()
    result = jump_search(data, data[-1])
    fastest = time.perf_counter() - start
    print(result, fastest)

    print('\n')

    # Number not in the array
    print('4.')

    print('Linear search for number not in the array...')
    start = time.perf_counter()
    result = linear_search(data, DATA_SIZE * 4)
    fastest = time.perf_counter() - start
    print(result, fastest)

    print('Binary search for number not in the array...')
    start = time.perf_counter()
    result = binary_search(data, DATA_SIZE * 4)
    fastest = time.perf_counter() - start
    print(result, fastest)

    print('Jump search for number not in the array...')
    start = time.perf_counter()
    result = jump_search(data, DATA_SIZE * 4)
    fastest = time.perf_counter() - start
    print(result, fastest)

    print('\n')

    # Print results in seconds


if __name__ == "__main__":
    main()
