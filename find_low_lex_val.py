def find_low_lex_val(s,t):
    indx = 0
    while indx != max(len(s),len(t)):
        if ord(s[indx]) < ord(t[indx]):
            return s
        elif ord(s[indx]) == ord(t[indx]):
            indx+=1
        else:
            return t
    return "same"

L = ["c",cb","cba"]
print(find_low_lex_val(a,b))


    