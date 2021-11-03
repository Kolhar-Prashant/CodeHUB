def tokenizer(s):
    token = []
    t = []
    for c in s:
        if c != " ":
            t.append(c)
        else:
            token.append("".join(t))
            t.clear()
    token.append("".join(t))
    return token

s = "Hello i am here"
print(tokenizer(s))