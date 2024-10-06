eps = 'e'

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

class RPN:
    

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
            elif s in operation_priority.keys():
                if operation_valency[s] == 1:
                    answer += s
                else:
                    while len(stack) > 0 and operation_priority[stack[-1]] >= operation_priority[s]:
                        answer += stack.pop()
                    stack.append(s)
            else:
                answer += s
        while len(stack) > 0:
            answer += stack.pop()
        return answer


    def __init__(self, expression: str) -> None:
        self.str = RPN.ExprToRPN(expression)

def IncreaseDictKeys(dic: dict, k: int) -> None:
    new_dict = dict()
    for key, val in dic.items():
        new_dict[key + k] = val
    dic = new_dict.copy()


class NFA:
    __init__(self):
        self.verts = list()
        self.terminal = [0]
        self.size = 1
        verts.append(dict())

    @staticmethod
    def BuildElementary(variable: str):
        nfa = NFA()
        nfa.verts.append(dict())
        nfa.verts[0][1] = variable
        nfa.terminal[0] = 1
        nfa.size = 2

    @staticmethod
    def CombineOperation(operation: str, arg_1: NFA, arg_2=""):
        nfa = NFA()

        if operation == '*':
            for i in range(0, arg_1.size):
                IncreaseDictKeys(arg_1[i], 1)

            nfa.size += arg_1.size
            nfa.verts += arg_1.verts
            nfa.verts[0][1] = eps

            for x in arg_1.terminal:
                nfa.verts[x + 1][0] = eps

            return nfa

        elif operation == '+' or operation == '.':
            for i in range(0, arg_1.size):
                IncreaseDictKeys(arg_1[i], 1)

            k = arg_1.size + 1
            for i in range(0, arg_2.size):
                IncreaseDictKeys(arg_2[i], k)

            nfa.size += arg_1.size
            nfa.size += arg_2.size
            nfa.size += 1

            nfa.verts += arg_1.verts
            nfa.verts += arg_2.verts
            nfa.verts.append(dict())

            nfa.verts[0][1] = eps

            if operation == '+':
                nfa.verts[0][k] = eps
     
                for x in arg_1.terminal:
                    nfa.verts[x + 1][nfa.size - 1] = eps
     
            else:
                for x in arg_1.terminal:
                    nfa.verts[x + 1][k] = eps
     

            for x in arg_2.terminal:
                nfa.verts[x + k][nfa.size - 1] = eps

            nfa.terminal[0] = nfa.size - 1
            return nfa

        else:
            print("ERROR: WRONG OPERATION")


    @staticmethod
    def BuildFromRegex(expression: str):
        rpn = RPN(expression).str
        print(rpn)
        nfa = NFA()


    @staticmethod
    def BuildFromText(text: str):
        pass

    # def ToString():
        
     

"""
s_inp = input()

NFA.BuildFromRegex(s_inp)
"""

