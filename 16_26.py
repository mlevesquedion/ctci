import operator


class Lexer:

    def __init__(self, source):
        self.i = 0
        self.source = source
        self.tokens = []

    def get_tokens(self):
        self._lex()
        return self.tokens

    def _lex(self):
        while self.i < len(self.source):
            char = self.source[self.i]
            if char.isdigit():
                self._read_digit()
            else:
                self.tokens.append(char)
                self.i += 1

    def _read_digit(self):
        number = 0
        while self.i < len(self.source) and self.source[self.i].isdigit():
            number = number * 10 + int(self.source[self.i])
            self.i += 1
        self.tokens.append(number)


def lex(equation):
    return Lexer(equation).get_tokens()


class Parser:

    token_to_op = {'+': operator.add, '-': operator.sub,
                   '*': operator.mul, '/': operator.truediv}

    def __init__(self, tokens):
        self.i = 0
        self.tokens = tokens
        self.numbers = [t for t in tokens if isinstance(t, int)]
        self.operations = [t for t in tokens if isinstance(t, str)]

    def get_value(self):
        self.muldiv()
        self.addsub()
        return self.numbers[0]

    def muldiv(self):
        number_i = 0
        operation_i = 0
        while operation_i < len(self.operations):
            if self.operations[operation_i] in '*/':
                left, right = self.numbers[number_i], self.numbers[number_i + 1]
                self.numbers[number_i] = self.token_to_op[self.operations[operation_i]](
                    left, right)
                del self.numbers[number_i + 1]
                del self.operations[operation_i]
            else:
                number_i += 1
                operation_i += 1

    def addsub(self):
        number_i = 0
        operation_i = 0
        while operation_i < len(self.operations):
            operation = self.operations[operation_i]
            left, right = self.numbers[number_i], self.numbers[number_i + 1]
            self.numbers[number_i] = self.token_to_op[operation](
                left, right)
            del self.numbers[number_i + 1]
            operation_i += 1


def parse(equation):
    return Parser(lex(equation)).get_value()


print(parse('2*3+5/6*3+15'))
