# coding:utf-8


# 冒泡排序（优化版）
# 方法核心1：i每循环一次，从最右侧依次比较相邻两个，若相同，则交换，最终将最大的数放到最右侧，下次比较则不比较最右侧的数
# 方法核心2：首先假设数组是有序的，若产生了交换，则证明数组无序，若未产生交换，则数组为有序，可结束方法。
# 最优时间复杂度：O(n)
# 最差时间复杂度：O(n^2)
def bubble_sort(arr):
    le = len(arr)
    for i in range(le - 1):
        is_sorted = 1
        for j in range(le - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = 0
        if is_sorted:
            return arr
    return arr


# 插入排序
# 特点：特点：stable sort、In-place sort
# 方法核心1：从左到右依次保证有序，然后将下一个元素插入到左侧适当位置
# 方法核心2：对第i个，依次，从右往左比较，若大于第i个的值，则将当前值向右移动，最后不能移动时，则将i插入到最终的位置
# 最优时间复杂度：当输入数组就是排好序的时候，复杂度为O(n)，而快速排序在这种情况下会产生O(n^2)的复杂度。
# 最差时间复杂度：当输入数组为倒序时，复杂度为O(n^2)
def insert_sort(arr):
    le = len(arr)
    for i in range(1, le):
        j = i - 1
        tmp_val = arr[i]
        while j >= 0 and arr[j] > tmp_val:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp_val
    return arr


# 选择排序
# 方法核心：每次找一个未排序部分的最小值，并放到未排列部分的最左侧
# 最优时间复杂度：O(n^2)
# 最差时间复杂度：O(n^2)
def select_sort(arr):
    le = len(arr)
    for i in range(le - 1):
        min_index = i
        for j in range(i + 1, le):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# 快速排序
# 最差时间复杂度：O(n^2)
# 平均时间复杂度：O(NlogN)
def fast_sort(arr):
    # 将arr数组中left到right中right放置到正确的位置，并使左侧都小于这个值，右侧都大于这个值
    def partition(arr, left, right):
        swapping_index = left
        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[i], arr[swapping_index] = arr[swapping_index], arr[i]
                swapping_index += 1
        arr[swapping_index], arr[right] = arr[right], arr[swapping_index]
        return swapping_index

    # 递归做partition操作，最终使得所有值都在正确的位置
    def sort(arr, left, right):
        if right > left:
            sep = partition(arr, left, right)
            # 放置一个正确的值后，递归操作这个位置两边部分
            sort(arr, left, sep - 1)
            sort(arr, sep + 1, right)
        return arr

    return sort(arr, 0, len(arr) - 1)


# 归并排序
# TODO 归并排序
def merge_sort(arr):
    return

arr1 = [7, 1, 5, 3, 6, 4, 8, 2, 6]
# print bubble_sort(arr1)
# print insert_sort(arr1)
# print select_sort(arr1)
print(fast_sort(arr1))
