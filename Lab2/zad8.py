class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def parChecker(symbolString):
    opening_symbols = {'(', '[', '{', '<'}
    closing_symbols = {')', ']', '}', '>'}
    symbol_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in opening_symbols:
            s.push(symbol)
        elif symbol in closing_symbols:
            if s.isEmpty() or symbol_pairs[s.peek()] != symbol:
                balanced = False
            else:
                s.pop()
        index += 1

    return balanced and s.isEmpty()


print(parChecker('((()))'))
print(parChecker('(((()))))'))
print(parChecker('((()()()))'))
print(parChecker('[{()}]'))
print(parChecker('{[()]}'))
print(parChecker('({[)]}'))
print(parChecker('<html><body></body></html>'))
