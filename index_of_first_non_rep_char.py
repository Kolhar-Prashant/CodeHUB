def index_of_first_non_rep_char(string):
    Dict = {}
    for char in string:
        if char in Dict:
            Dict[char]+=1
        else:
            Dict[char]=1
    for char, freq in Dict.items():
        if freq == 1:
            return string.index(char)
            
string = 'loveleetcode'
print(index_of_first_non_rep_char(string))