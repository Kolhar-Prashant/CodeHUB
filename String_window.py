def str_win(s,t):
    st,ed=0,len(t)
    mem = []
    char_dict = {}
    for char in t:
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict[char]=1    
    while ed != len(s)+1:
        temp = s[st:ed]
        valid = True
        for char, char_cnt in char_dict.items():
            if temp.count(char) != char_cnt:
                valid = False
        if valid == True:
            mem.append(temp)                        
        st += 1
        ed += 1 
    return mem
s = "hellxolollo"
t = "llo"
print(str_win(s,t))
