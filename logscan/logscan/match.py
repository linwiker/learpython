#/usr/bin/env python
# -*- coding: utf-8 -*-

from queue import Queue
import re

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


#创建虚拟语法树(AST)
class ASTree:

    def __init__(self, token):
        self.root = token
        self.left = None
        self.right = None

#所有数据压倒栈里面
    def visit(self):
        ret = []
        q = Queue()
        q.put(self)
        while not q.empty():
            t = q.get()
            ret.append(t.root)
            if t.left:
                q.put(t.left)
            if t.right:
                q.put(t.right)
        return ret



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
        elif is_expr:  #直接是表达式情况,会字符都输入到expr列表内
            expr.append(c)
        elif c in Token.SYMBOLS: #如果在符号表里面，而且不是表达式
            token = Token(c, Token.SYMBOL)
            tokens.append(token)
        elif c == '(': #左括号的情况
            token = Token(c, Token.LEFT_BRACKETS)
            tokens.append(token)
        elif c == ')': #右括号的情况
            token = Token(c, Token.RIGHT_BRACKETS)
            tokens.append(token)
    return tokens


#子函数实现语法解析
def make_sub_ast(stack, t):
    current = t
    while stack and stack[-1].root.type != Token.LEFT_BRACKETS:  #语法树不为空而且栈顶现在不是左括号
        node = stack.pop()
        if node.root.type != Token.SYMBOL: #如果不是符号的话，那证明已经有问题了，抛出错误
             raise Exception('parse error, excepted {0} but {1}'.format(Token.SYMBOL, node.root))
        node.right = current  #那证明当前表达式就是node的左节点
        if node.root.value == "&" or node.root.value == "|":
            left = stack.pop()
            if left.root.type != Token.SYMBOL and left.root.type != Token.EXPRESSION: #如果left的节点类型不是符号和表达式则抛出报错
                raise Exception("parse error excepted {0} and {1} but {2}".format(Token.SYMBOL, Token.EXPRESSION,
                                                                                  left.root.type))
            node.left = left  #则left是node的右节点
        current = node
    stack.append(current)

#语法解析
def make_ast(tokens):
    stack = []
    for t in tokens:
        tree = ASTree(t)
        if tree.root.type == Token.SYMBOL or tree.root.type == Token.LEFT_BRACKETS: #如果ast节点类型是符号或者是左括号，则压到栈里面
            stack.append(tree)
        elif tree.root.type == Token.EXPRESSION: #如果节点是表达式则调用子函数来处理
            make_sub_ast(stack, tree)
        else:
            sub_tree = stack.pop()
            if sub_tree.root.type != Token.SYMBOL and sub_tree.root.type != Token.EXPRESSION:
                raise Exception("parse error excepted {0} and {1} but {2}".format(Token.SYMBOL, Token.EXPRESSION,
                                                                                 sub_tree.root.type))
            tmp = stack.pop()
            if tmp.root.type != Token.LEFT_BRACKETS:
                raise Exception('paser error,excepted {0} but {1}'.format(Token.LEFT_BRACKETS, tmp.root.type))
            make_sub_ast(stack, sub_tree)
    return stack.pop()


#全序遍历(使用递归进行运算)
def cacl(ast, line):
    #只有两种情况，表达式和符号
    if ast.root.type != Token.EXPRESSION:
        if ast.root.value == '!': #如果是!情况
            return not cacl(ast.right, line)
        if ast.root.value == '&':
            return cacl(ast.left, line) and cacl(ast.right, line)
        if ast.root.value == '|':
            return cacl(ast.left, line) or cacl(ast.right, line)
    else: #表达式的情况
        return re.search(ast.root.value, line) is not None


class Matcher:

    def __init__(self, origin):
        self.origin = origin
        self.ast = make_ast(tokenize(origin))

    def match(self, line):
        return cacl(self.ast, line)

if __name__ == '__main__':
    e = '#test# & #abc# | (!#123# | #456#)'
    s = 'test cdg 123 456'
    m = Matcher(e)
    t = m.match(s)
    print(t)


