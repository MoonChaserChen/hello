# coding:utf-8
# 7
# 3，8
# 8，1，0
# 2，7，4，4
# 4，5，2，6，5

data_last = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
data_all = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def dp_last(ori_data):
    le = len(ori_data)
    for i in reversed(range(le - 1)):
        for j in range(i + 1):
            # 把所有结果放到最后一行
            ori_data[-1][j] = max(ori_data[-1][j], ori_data[-1][j + 1]) + ori_data[i][j]
    print(ori_data[-1][0])
    print(ori_data)


def dp_all(ori_data):
    le = len(ori_data)
    for i in reversed(range(le - 1)):
        for j in range(i + 1):
            # 把结果放到原数组，这样可以算出路径
            ori_data[i][j] += max(ori_data[i + 1][j], ori_data[i + 1][j + 1])
    print(ori_data[0][0])


def trace(ori_data):
    result = (0, 0)
    while result:
        result = trace_next(ori_data, result[0], result[1])


def trace_next(ori_data, line, current):
    print (line, current)
    if line == len(ori_data) - 1:
        return None
    else:
        next_current = current if ori_data[line + 1][current] > ori_data[line + 1][current + 1] else current + 1
        return line + 1, next_current


# dp_last(data_last)
dp_all(data_all)
trace(data_all)
