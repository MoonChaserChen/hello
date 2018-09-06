def priv_com(a, b):
    mul_dev = ['*', '/']
    add_sub = ['+', '-']
    if (a in mul_dev and b in mul_dev) or (a in add_sub and b in add_sub):
        return 0
    elif a in mul_dev and b in add_sub:
        return 1
    elif a in add_sub and b in mul_dev:
        return -1


def is_operation(ope):
    operation = ['+', '-', '*', '/']
    if ope in operation:
        return 1
    else:
        return 0


def transfer(notation):
    le = len(notation)
    stack = []
    for x in notation:
        if not is_operation(x):
            if x == '(':
                stack.append(x)
            elif x == ')':
                while len(stack) != 0 and stack[-1] != '(':
                    print stack.pop(),
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
            else:
                print x,
        else:
            while len(stack) != 0 and is_operation(stack[-1]) and (
                    priv_com(stack[-1], x) == 1 or priv_com(stack[-1], x) == 0):
                print stack.pop(),
            stack.append(x)
    while len(stack) != 0:
        print stack.pop(),


test = ['a', '+', 'b', '*', 'c', '+', '(', 'd', '*', 'e', '+', 'f', ')', '*', 'g']
transfer(test)
