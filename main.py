from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        elif len(self.stack) > 0:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        element = self.stack[-1]
        self.stack.pop()
        return element

    def peek(self):
        if len(self.stack) == 0:
            return None
        element = self.stack[-1]
        return element


def balanced(str_):
    stack = Stack()
    balance = True
    index = 0
    while index < len(str_) and balance:
        parenthesis = str_[index]
        if parenthesis in "([{":
            stack.push(parenthesis)
        else:
            if stack.is_empty():
                balance = False
            else:
                top = stack.pop()
                if not match(top, parenthesis):
                    balance = False
        index += 1
    if balance and stack.is_empty():
        return "сбалансировано"
    else:
        return "несбалансировано"


def match(open_, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open_) == closers.index(close)


#сбалансированные
string_1 = '(((([{}]))))'
string_2 = '[([])((([[[]]])))]{()}'
string_3 = '{{[()]}}'

#несбалансированные
string_4 = '}{}'
string_5 = '{{[(])]}}'
string_6 = '[[{())}]'


print(balanced(string_6))