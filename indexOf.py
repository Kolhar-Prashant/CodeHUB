def indexOf(src,tar):
    def Find(src, tar):
        char_indx = 0
        Found_indx = -1
        while char_indx < len(src):
            if src[char_indx] == tar[0]:
                Found_indx = char_indx
                temp_str = "".join(src[char_indx:len(tar) + char_indx])
                if temp_str == tar:
                    return Found_indx
                else:
                    temp = list(src)
                    temp[Found_indx] = "#"  # Masking logic.
                    src = "".join(temp)
                    char_indx = Found_indx
                    Found_indx = -1
            char_indx += 1
        return Found_indx
    
    if len(tar) > len(src):
        return -1
    if src == "" and tar == "":
        return 0
    if src == "":
        return -1
    if tar == "":
        return 0
    if src == tar:
        return 0
    return Find(src, tar)

src = "Hellpxhllox"
tar = "llo"
print(indexOf(src,tar))