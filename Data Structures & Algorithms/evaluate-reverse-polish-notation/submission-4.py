class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in {"+","/","*","-"}:
                stack.append(int(tokens[i]))
            if tokens[i] == "+":
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(a1+a2)
            elif tokens[i] == "/":
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(int(a2/a1))
            if tokens[i] == "-":
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(a2-a1)
            if tokens[i] == "*":
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(a1*a2)
        return stack.pop()