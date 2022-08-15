# https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]

        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)

        left_ind = 0
        right_ind = 0
        result_ind = 0
        result_array = [None] * len(array)
        while left_ind < len(left_array) and right_ind < len(right_array):
            if left_array[left_ind] < right_array[right_ind]:
                result_array[result_ind] = right_array[right_ind]
                right_ind = right_ind + 1
            else:
                result_array[result_ind] = left_array[left_ind]
                left_ind = left_ind + 1
            
            result_ind = result_ind + 1

        while right_ind < len(right_array):
            result_array[result_ind] = right_array[right_ind]
            right_ind = right_ind + 1
            result_ind = result_ind + 1

        while left_ind < len(left_array):
            result_array[result_ind] = left_array[left_ind]
            left_ind = left_ind + 1
            result_ind = result_ind + 1
        
        return result_array
    else:
        return array

    

if __name__ == '__main__':
    Numbers = [41, 33, 17, 80, 61, 5, 55]
    result = merge_sort(Numbers)
    print(result)