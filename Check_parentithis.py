def check(exp):
    stk = []
    for char in exp:
        if char == '[' or char == '(':
            stk.append(char)
        if char == ']' or char == ')':
            if len(stk) > 0:
                stk.pop(-1)
            else:
                return False
    return True

exp = '[((a+b)*d)-e]'
print(check(exp))