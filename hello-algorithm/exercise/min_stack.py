# coding: utf-8
class Element:
    def __init__(self, value, min_value):
        self.value = value
        self.min_value = min_value


class MinStack:
    def __init__(self):
        self.stack = []

    def pop(self):
        self.stack.pop()

    def get_min(self):
        return self.stack[-1].min_value if len(self.stack) > 0 else None

    def push(self, value):
        min_before = self.get_min()
        ele = Element(value, min(value, min_before) if min_before else value)
        self.stack.append(ele)


class MinStack1:
    def __init__(self):
        self.ele_stack = []
        self.min_stack = []

    def pop(self):
        if self.ele_stack[-1] == self.min_stack[-1]:
            self.ele_stack.pop()
            self.min_stack.pop()
        else:
            self.ele_stack.pop()

    def push(self, val):
        if len(self.min_stack) < 1 or val <= self.min_stack[-1]:
            self.min_stack.append(val)
            self.ele_stack.append(val)
        else:
            self.ele_stack.append(val)

    def get_min(self):
        return self.min_stack[-1]


st = MinStack()
st.push(7)  # ---> 7
print(st.get_min())
st.push(8)  # ---> 7
print(st.get_min())
st.push(5)  # ---> 5
print(st.get_min())
st.push(5)  # ---> 5
print(st.get_min())
st.pop()  # ---> 5
print(st.get_min())
st.pop()  # ---> 7
print(st.get_min())
