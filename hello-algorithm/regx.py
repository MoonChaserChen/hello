# coding:utf-8
def match(reg, ori_str):
    # 结尾条件
    if reg == '' or ori_str == '':
        return reg == ori_str
    le = len(reg)
    # 正则太长，直接返回0
    if le > len(ori_str):
        return False
    for i in range(le):
        if reg[i] == '.' or reg[i] == ori_str[i]:
            return match(reg[i + 1:], ori_str[i + 1:])
        elif reg[i] == '*':
            if i == le - 1:
                return True
            for j in range(i + 1, len(ori_str)):
                if match(reg[i + 1:], ori_str[j:]):
                    return True
        elif reg[i] != ori_str[i]:
            return False

print(match('ab.d*gh*', 'abcdefghi'))
print(match('aaa', 'aaa'))
print(match('aa', 'aaa'))
print(match('aaa', 'aa'))
print(match('.aa', 'aaa'))
print(match('*a', 'aaa'))
print(match('ab*ab', 'abababab'))
