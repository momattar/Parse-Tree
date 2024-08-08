<div align="center">
  
  # Parse Tree
</div>

## Project purpose
To try to find a way to build and evaluate a parse tree if the expression has no parentheses at all.

## Main points
First converted the given infix expression to a postfix one, postfix cancels this using precedence as it encodes the operation from the new way it’s written, with no need of parenthesis.

If we encounter any arithmetic operators, we create a new binary tree with a root equals to this operator and then we pop twice from the stack to right and left children respectively push this tree to a Stack.

If we encounter operands , we create a new binary tree with a root equals to those operands and push this tree to a Stack.

## Presentation
Here's a powerpoint presentation contains idea, code and running example

[Drive link](https://drive.google.com/drive/folders/179Sxg-qJLCuNZxKAqSfmBHPJqMyEYBY2?usp=sharing)
