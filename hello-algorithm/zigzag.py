def zigzag(string, rows):
    L = ["" for i in range(rows)]
    index, step = 0, 1
    for x in string:
        L[index] += x
        index += step
        if index == 0 or index == rows - 1:
            step = -step
    return "".join(L)


str = "PAYPALISHIRING"
print(zigzag(str, 3))
