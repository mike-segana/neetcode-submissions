class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #array of strings (tokens) represents a valid arithmetic expression in reverse polish notation
        stack = []
        for string in tokens:
            if string not in ["+", "-", "*", "/"]:
                stack.append(int(string))
            elif string == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a + b))
            elif string == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a - b))
            elif string == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a * b))
            elif string == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
        return stack[0]