
def mask_letter(index,s):
    L = []
    for e in s:
        L.append(e)
    L[index] = "-"
    s = "".join(L)
    return s

s=input("Enter the string : ")
sub_str=input("Enter the substring to know how many time did it appear in string : ")
c=0
l=0
while l != len(s):
    index=s.find(sub_str)
    l+=1
    if (index != -1):
        c+=1
    s=mask_letter(index,s)

print("Substring",sub_str,"appeared",c,"times in the given string")
