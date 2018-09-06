# coding: utf-8
string = 'dabcba'


def max_reverse_equal(ori_str):
    start = 0
    max_len = 0
    le = len(ori_str)
    dp = [([0] * le) for i in range(le)]
    for i in range(le):
        for j in range(le - i):
            k = i + j
            if ori_str[j] == ori_str[k] and (i < 2 or dp[j + 1][k - 1]):
                dp[j][k] = 1
                if i > max_len:
                    max_len = i
                    start = j
    print(ori_str[start:start + max_len + 1])
    print(start, max_len)


max_reverse_equal(string)
