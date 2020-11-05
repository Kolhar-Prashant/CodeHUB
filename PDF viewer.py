h = [1, 3, 1, 3, 1, 4, 1, 3 ,2 ,5, 5, 5, 5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,7]
word = "zaba"
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

print(maxx * len(word))