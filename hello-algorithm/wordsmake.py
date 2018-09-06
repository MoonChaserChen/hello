# coding:utf-8
string = 'leetcode'
dic = ['le', 'leet', 'code']
solution = []


def place_line(i):
    for x in dic:
        # solution[i] = x
        solution.insert(i, x)
        sum = ''.join(solution)
        if sum == string:
            print 'yes'
            return
        elif string.startswith(sum):
            place_line(i + 1)
    print 'no'
place_line(0)
