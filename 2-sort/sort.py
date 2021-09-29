from random import seed, sample
from time import perf_counter


def quicksort(lyst):
    def partition(lyst, left, right, pivot):
        while left <= right:
            while lyst[left] < pivot:
                left += 1
            while lyst[right] > pivot:
                right -= 1

            if left <= right:
                lyst[left], lyst[right] = lyst[right], lyst[left]
                left += 1
                right -= 1
        return left

    def quicksort_helper(lyst, left, right):
        if left >= right:
            return

        pivot = lyst[(left + right) // 2]
        part_index = partition(lyst, left, right, pivot)
        quicksort_helper(lyst, left, part_index - 1)
        quicksort_helper(lyst, part_index, right)

    quicksort_helper(lyst, 0, len(lyst) - 1)

    return lyst


def mergesort(lyst):
    if len(lyst) <= 1:
        return lyst

    middle = len(lyst) // 2
    left = lyst[:middle]
    right = lyst[middle:]
    mergesort(left)
    mergesort(right)
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lyst[k] = left[i]
            i += 1
        else:
            lyst[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        lyst[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        lyst[k] = right[j]
        j += 1
        k += 1

    return lyst


def selection_sort(lyst):
    for i in range(len(lyst)):
        min_index = i

        for j in range(i + 1, len(lyst)):
            if lyst[j] < lyst[min_index]:
                min_index = j

        lyst[i], lyst[min_index] = lyst[min_index], lyst[i]

    return lyst


def insertion_sort(lyst):
    for i in range(1, len(lyst)):
        key = lyst[i]
        j = i - 1
        while j >= 0 and key < lyst[j]:
            lyst[j + 1] = lyst[j]
            j -= 1
        lyst[j + 1] = key

    return lyst


def is_sorted(lyst):
    sorted_lyst = lyst.copy()
    sorted_lyst.sort()
    return bool(sorted_lyst == lyst)


def make_data():
    data_size = 15000
    seed(42)
    return sample(range(data_size * 3), k=data_size)


def main():
    # SELECTION SORT
    print("starting selection sort...")
    start = perf_counter()
    selection_sort(make_data())
    selection_sort_elapsed = perf_counter() - start
    print("selection sort duration:", "%.04f" %
          selection_sort_elapsed, "seconds.\n")

    # INSERTION SORT
    print("starting insertion sort...")
    start = perf_counter()
    insertion_sort(make_data())
    insertion_sort_elapsed = perf_counter() - start
    print("insertion sort duration:", "%.04f" %
          insertion_sort_elapsed, "seconds.\n")

    # MERGESORT
    print("starting mergesort...")
    start = perf_counter()
    mergesort(make_data())
    mergesort_elapsed = perf_counter() - start
    print("mergesort duration:", "%.04f" %
          mergesort_elapsed, "seconds.\n")

    # QUICKSORT
    print("starting quicksort...")
    start = perf_counter()
    quicksort(make_data())
    quicksort_elapsed = perf_counter() - start
    print("quicksort duration:", "%.04f" %
          quicksort_elapsed, "seconds.\n")

    # TIMSORT
    print("starting timsort...")
    start = perf_counter()
    make_data().sort()
    timsort_elapsed = perf_counter() - start
    print("timsort duration:", "%.04f" %
          timsort_elapsed, "seconds.\n")


if __name__ == "__main__":
    main()
