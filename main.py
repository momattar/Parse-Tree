# ===================== Importing library and classes we will use =========================
import operator
from Classes.Stack import Stack
from Classes.BinaryTree import BinaryTree
import Utilities

# ===================== Building parse tree ================================================


def buildtree(nfpexp):
    Postexp = Utilities.infix_to_postfix(nfpexp)  # In order to maintain the order of calculations
    pStack = Stack()
    nfpexpList = Postexp.split()
    for token in nfpexpList:
        # If it is an operator we will build subtree and push it into stack
        if token in "+-*/^":
            acc_binaryTree = BinaryTree(token)
            acc_binaryTree.rightChild = pStack.pop()
            acc_binaryTree.leftChild = pStack.pop()
            pStack.push(acc_binaryTree)
            # If it is an operand we will push it into the stack
        else:
            pStack.push(BinaryTree(int(token)))
    # Last tree in the stack is our tree
    return pStack.pop()

# ===================== parse tree evaluation ===============================================


def evaluate(parsetree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow}
    leftc = parsetree.getLeftChild()
    rightc = parsetree.getRightChild()

    if leftc and rightc:
        fn = opers[parsetree.getRootVal()]
        return fn(evaluate(leftc), evaluate(rightc))
    else:
        return parsetree.getRootVal()

# ===================== trying our functions ================================================


# print("Enter the Expression : ") # If we want the user to enter the expression
# MyExp = input()
MyExp = "3 * 5  +  4 - 2 ^ 2"
MyTree = buildtree(MyExp)
OutPut = evaluate(MyTree)
print("The result of the expression is: ", OutPut)