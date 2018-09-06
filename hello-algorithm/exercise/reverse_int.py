def rewrite(x):
    result = 0
    flag = 1 if x > 0 else -1
    x = abs(x)
    while x != 0:
        quo, rem = divmod(x, 10)
        result = result * 10 + rem
        x = quo
    return flag * result


print(rewrite(1020))
print(rewrite(321))
print(rewrite(-1020))
print(rewrite(0))
