#/usr/bin/env python
# -*- coding: utf-8 -*-
class Token:
    LEFT_BRACKETS = 'LEFT_BRACKETS'
    RIGHT_BRACKETS = 'RIGHT_BRACKETS'
    SYMBOL = 'SYMBOL'
    EXPRESSION = 'EXPRESSION'
    SYMBOLS = '&|!'
    def __init__(self,value,type):
        self.value = value
        self.type = type
    def __str__(self):
        return '{0} {1}'.format(self.value,self.type)
    def __repr__(self):
        return self.__str__()


def tokenize(origin):
    tokens = []
    is_expr = False
    expr = []
    for c in origin:
        if c == '#':
            if not is_expr:
                is_expr = True
            else:
                is_expr =False
                token = Token(''.join(expr), Token.EXPRESSION)
                tokens.append(token)
                expr = []
        elif is_expr:
            expr.append(c)
        elif c in Token.SYMBOLS:
            token = Token(c, Token.SYMBOL)
        elif c == '(':
            token = Token(c, Token.LEFT_BRACKETS)
            tokens.append(token)
        elif c == ')':
            token = Token(c, Token.RIGHT_BRACKETS)
            tokens.append(token)
    return tokens


if __name__ == "__main__":
    e = '#test# & #abc#|(!#123# |#456#)'
    print(tokenize(e))