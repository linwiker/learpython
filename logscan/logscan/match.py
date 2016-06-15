#/usr/bin/env python
# -*- coding: utf-8 -*-
class Token:
    LEFT_BRACKETS = "LEFT_BRACKETS"
    RIGHT_BRACKETS = "RIGHT_BRACKETS"  #定义左右括号
    SYMBOL = "SYMBOL"  #符号
    EXPRESSION = "EXPRESSION"  #表达式
    SYMBOLS = '&|!'

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __str__(self):
        return "{0}:{1}".format(self.value,self.type)

    def __repr__(self):
        return self.__str__()


def tokenize(origin):
    tokens = []
    is_expr = False
    expr = []
    for c in origin:
        if c == '#':  #如果字符等于#(表达式规则需要首先进行协商使用那种类型),等于#号有两种情况，开始和结束
            if not is_expr:  #当不是一个表达式，那么#是表达式开始
                is_expr = True
            else:  #是一个表达式的情况，既是#号是结束
                is_expr = False #后续他就不是表达式了
                token = Token(''.join(expr), Token.EXPRESSION)   #把expr的字符连接起来，然后把解析的结果追加到tokens里面，然后清空expr
                tokens.append(token)
                expr = []
        elif c == Token.SYMBOLS and not is_expr: #如果在符号表里面，而且不是表达式
            token = Token(c, Token.SYMBOL)
            tokens.append(token)
        elif c == '(' and not is_expr: #左括号的情况
            token = Token(c, Token.LEFT_BRACKETS)
            tokens.append(token)
        elif c == ')' and not is_expr: #右括号的情况
            token = Token(c, Token.RIGHT_BRACKETS)
            tokens.append(token)
        elif is_expr:  #直接是表达式情况,会字符都输入到expr列表内
            expr.append(c)
    return tokens

if __name__ == '__main__':
    e = '#test# & #abc# | (!#123# | #456#)'
    print(tokenize(e))


