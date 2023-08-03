class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        oper = ["+", "-", "*", "/"]
        stack = []
        for t in tokens:
            if t not in oper:
                stack.append(t)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(eval(f"{num2} {t} {num1}")))
        return int(stack[0])
