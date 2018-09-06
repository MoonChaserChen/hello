# coding:utf-8
def length_of_longest_substring(string):
    le = len(string)
    # [i, j]表示滑动窗口
    # window_content表示当前窗口中已有元素
    # start,max_len储存结果
    window_content = {}
    i = j = start = max_len = 0
    # 算法思想：
    # 先移动右窗口，
    # 若右窗口元素已存在于window_content中，（再移动右窗口已无意义）移动左窗口（需要移除元素），移动左窗口后右窗口位置不变（因为较左位置的右窗口肯定不是结果）
    # 若右窗口元素未存在于window_content中，继续移动右窗口（window_content加入新元素），并对结果进行判断
    while j < le:
        if string[j] not in window_content:
            window_content[string[j]] = j
            j += 1
            if max_len < j - i:
                max_len = j - i
                start = i
        else:
            window_content.pop(string[i])
            i += 1
    return start, max_len


def length_of_longest_substring(s):
    i = max_len = start = 0
    used_char = {}
    for j in range(len(s)):
        if s[j] in used_char:
            i = max(used_char[s[j]] + 1, i)
        if j - i + 1 > max_len:
            max_len = j - i + 1
            start = i
        used_char[s[j]] = j
    return start, max_len


str = "abcabhijkcbbhijk"
# str = "aaaaaaaa"
print(length_of_longest_substring(str))
