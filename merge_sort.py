
from operator import le
from re import A


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]

        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)

        tzu = 1

if __name__ == '__main__':
    Numbers = [41, 33, 17, 80, 61, 5, 55]
    merge_sort(Numbers)
    print(Numbers)