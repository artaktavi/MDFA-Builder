
class RPN:
    operation_priority = {
        '(' : 0,
        '+' : 1,
        '.' : 2,
        '*' : 3
    }

    operation_valency = {
        '(' : 0,
        '+' : 2,
        '.' : 2,
        '*' : 1
    }

    @staticmethod
    def ExprToRPN(expression: str) -> str:
        stack = list()
        answer = ""
        for s in expression:
            if s == '(':
                stack.append(s)
            elif s == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    answer += stack.pop()
                stack.pop()
            elif s in RPN.operation_priority.keys():
                if RPN.operation_valency[s] == 1:
                    answer += s
                else:
                    while len(stack) > 0 and RPN.operation_priority[stack[-1]] >= RPN.operation_priority[s]:
                        answer += stack.pop()
                    stack.append(s)
            else:
                answer += s
        while len(stack) > 0:
            answer += stack.pop()
        return answer


    def __init__(self, expression: str) -> None:
        self.str = RPN.ExprToRPN(expression)
 
"""
s_inp = input()
a = RPN(s_inp)
print(a.str)
"""

