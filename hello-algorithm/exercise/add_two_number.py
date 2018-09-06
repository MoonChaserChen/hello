def addTwoNumbers(l1, l2):
    def list2int(list):
        result = 0
        while len(list) > 0:
            result = result * 10 + list.pop()
        return result

    def int2list(int_val):
        if int_val == 0:
            return [0]
        list = []
        while int_val > 0:
            quo, rem = divmod(int_val, 10)
            list.append(rem)
            int_val = quo
        return list

    return int2list(list2int(l1) + list2int(l2))


print(addTwoNumbers([1, 8], [0, 4]))
