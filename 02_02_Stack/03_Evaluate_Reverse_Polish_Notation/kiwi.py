class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        op = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in op:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(eval(f"{num1}{token}{num2}")))
        return stack[0]
