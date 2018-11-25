# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html


def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst)-1)


def quick_sort_helper(lst, left, right):
    if left < right:
        split_point = partition(lst, left, right)

        quick_sort_helper(lst, left, split_point-1)
        quick_sort_helper(lst, split_point+1, right)


def partition(lst, left, right):
    from random import randint
    pivot_i = randint(left, right)
    pivot = lst[pivot_i]

    low = left
    high = right

    while True:

        while low <= high and low < right and lst[low] <= pivot:
            low += 1

        while low <= high and high > 0 and lst[high] >= pivot:
            high -= 1

        if low >= high:
            if pivot_i > low:
                lst[pivot_i], lst[low] = lst[low], lst[pivot_i]
                return low
            elif pivot_i < high:
                lst[pivot_i], lst[high] = lst[high], lst[pivot_i]
                return high
            else:
                return pivot_i
        else:
            lst[low], lst[high] = lst[high], lst[low]


# Test case
def main():
    lst = [5, 2, 3, 1, 17, 4, 3, 2]
    print(f"Initial List: {lst}")
    quick_sort(lst)
    print(f"Sorted List: {lst}")


if __name__ == "__main__":
    main()
