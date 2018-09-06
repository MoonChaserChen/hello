def fast_sort(arr):
    le = len(arr)

    def partition(arr, left, right):
        swapping_index = left
        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[i], arr[swapping_index] = arr[swapping_index], arr[i]
                swapping_index += 1
        arr[swapping_index], arr[right] = arr[right], arr[swapping_index]
        return swapping_index

    def sort(arr, left, right):
        if right > left:
            sep = partition(arr, left, right)
            sort(arr, left, sep - 1)
            sort(arr, sep + 1, right)
        return arr

    return sort(arr, 0, le - 1)


arr1 = [7, 1, 2, 3, 6, 4, 8, 5]
print(fast_sort(arr1))
