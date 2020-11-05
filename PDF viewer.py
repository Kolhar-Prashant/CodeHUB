def designerPdfViewer(h, word):
    s = "the quick brown fox jumps over the lazy dog"
    s = s.replace(" ","")
    s = sorted(set(s))

    indx = 0
    Dict = {}
    for num in h:
        Dict[s[indx]] = num
        indx+=1

    maxx = 0
    for alpha in word:
        height = Dict[alpha]
        if height > maxx:
            maxx = height
    return maxx * len(word)
