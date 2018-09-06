def two_sum(nums, target):
    buff_dict = {}
    for i, v in enumerate(nums):
        if v in buff_dict:
            return [buff_dict[v], i]
        else:
            buff_dict[target - v] = i
    return False


print(two_sum([2, 3, 4], 6))
