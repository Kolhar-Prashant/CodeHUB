def longestSubstringWithoutRepeat(s):
    if len(set(s)) == len(s):
        return len(s)
    mem,indx,max_len,max_word = '',0,0,''
    while indx != len(s):
        if s[indx] not in mem:
            mem += s[indx]
        else:
            if len(mem) > max_len:
                max_len = len(mem)
                max_word = mem
            mem = ''
            continue
        indx+=1
    return max_word,len(max_word)
s="prashant"
print(longestSubstringWithoutRepeat(s))

    
    