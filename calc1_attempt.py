# https://ruslanspivak.com/lsbasi-part1/
# This is my attempt at the first exercise 
# They give a walkthrough of how to complete
# the exercise, but I wanted to try it on
# my own first. I just saw that their solution
# used these class/function names.
# And I set up the repl the same way they did.

class Token(object):
    def __init__(self, string):
        self.string = string


class Interpreter(object):
    def __init__(self, string):
        self.string = string

    def add(self, n1, n2):
        return int(n1) + int(n2)
    def sub(self, n1, n2):
        return int(n1) - int(n2)
    def mul(self, n1, n2):
        return int(n1) * int(n2)
    def div(self, n1, n2):
        return int(n1) / int(n2)
    def pow(self, n1, n2):
        return int(n1) ** int(n2)
    OPERATORS = {'+':add,
                 '-':sub,
                 '*':mul,
                 '/':div,
                 '^':pow,}

    def expr(self):
        result = 'invalid operation'
        for i in self.string:
            if i in self.OPERATORS:
                index = self.string.index(i)
                func = self.OPERATORS[i]
                num1 = self.string[:index].strip()
                num2 = self.string[index+1:].strip()
                result = func(self, num1, num2)
        return result


def main():
    while True:
        try:
            text = input('user> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
