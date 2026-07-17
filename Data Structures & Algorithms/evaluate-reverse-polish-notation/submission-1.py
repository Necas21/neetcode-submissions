class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # Iterate over tokens
        for t in tokens:
            # If value is operator, pop 2 values from stack, perform operation, push result back onto stack
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 - val2)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(val1 / val2))
            else:
                stack.append(int(t))
        return stack[0]