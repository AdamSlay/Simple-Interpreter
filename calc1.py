"""
This is the Author's Version of the Code
However, I will be attempting the unguided exercises
in this file, so many of the functions are my own.
The skeleton are the Author's.
"""
INTEGER, OPERATOR, SPACE, EOF = 'INTEGER', 'OPERATOR', 'SPACE', 'EOF'

class Token(object):
    def __init__(self, type, value):
        # Token Type(INTEGER, OPERATOR, EOF)
        self.type = type
        # Token Value [0-9], '+', or None
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {repr(self.value)})'
    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        self.text = text
        # pos is the index of text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """
        This is the Lexical Analyser
        It's where we parse the input into
        individual tokens, one at a time
        """
        text = self.text

        """
        Check if self.pos is past the end of the self.text
        if so, return EOF because there is no more
        input left to convert
        """
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        """
        Get char at current pos and determine
        what token to assign it to.
        """
        current_char = text[self.pos]
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token
        if current_char == '+' or current_char == '-':
            token = Token(OPERATOR, current_char)
            self.pos += 1
            return token
        if current_char == ' ':
            token = Token(SPACE, current_char)
            self.pos += 1
            return token
        self.error()

    def eat(self, token_type):
        """
        If current token type matches previoius
        token type, 'eat' the current token and
        assign the next token to self.current_token,
        otherwise, raise an Exception.
        """
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        # Finding the left number
        # the while loop goes until whitespace or operator
        # it appends each new digit to a string version of the old 
        # digit then converts it to an int
        # the 'l' value is just because you don't want to append the 
        # init digit to the left number or else it will count it twice
        # ie. You init left with a val of 2 then enter the while loop
        # and now the value is 4.
        left = self.current_token
        l = 0
        while (self.current_token.type != OPERATOR and self.current_token.type != SPACE):
            if l > 0:
                left.value = int(str(left.value) + str(self.current_token.value))
            l += 1
            self.eat(INTEGER)

        # checking if there is a whitespace after left number
        # if so, eat it
        if self.current_token.type == SPACE:
            self.eat(SPACE)

        # Here is our operator
        op = self.current_token
        self.eat(OPERATOR)

        #checking for space again
        if self.current_token.type == SPACE:
            self.eat(SPACE)

        # Same as above for the left value except this time we 
        # are looking for EOF rather than the OPERATOR
        right = self.current_token
        r = 0
        while (self.current_token.type != EOF and self.current_token.type != SPACE):
            if r > 0:
                right.value = int(str(right.value) + str(self.current_token.value))
            r += 1
            self.eat(INTEGER)

        # Returning the result based on which operator was inputed 
        result = 'Invalid Operator'
        if op.value == '+':
            result = left.value + right.value
        elif op.value == '-':
            result = left.value - right.value
        return result

def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
