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

    def add(self, string):
        return int(string[0]) + int(string[2])
    def sub(self, string):
        return int(string[0]) - int(string[2])
    def mul(self, string):
        return int(string[0]) * int(string[2])
    def div(self, string):
        return int(string[0]) / int(string[2])
    def pow(self, string):
        return int(string[0]) ** int(string[2])
    OPERATORS = {'+':add,
                 '-':sub,
                 '*':mul,
                 '/':div,
                 '^':pow,}

    def expr(self):
        result = 'invalid operation'
        for i in self.string:
            if i in self.OPERATORS:
                func = self.OPERATORS[i]
                result = func(self, self.string)
        if result:
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
