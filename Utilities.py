# ===================== Importing library and classes we will use =========================
from Classes.Stack import Stack

# ===================== Infix to Postfix converting ========================================


def infix_to_postfix(infixexpr):
    prec = {}

    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []

    tokenList = infixexpr.split()  # default seperator is white space

    for token in tokenList:
        if token in "+-*/^":
            # Don't swap the conditions
            # while (prec[opStack.peek()] >= prec[token]) and (not opStack.isEmpty()):
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()

        else:
            postfixList.append(token)

    while not opStack.isEmpty():  # aligned to for-loop
        postfixList.append(opStack.pop())

    return " ".join(postfixList)  # Here, seperator is space
