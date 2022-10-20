def build_teens(num,indx,temp,place_val=''):
    if num[indx] == '1':  # To check if the ten's place contain no from 11 to 19
        t = num[indx] + num[indx + 1]
        temp += doubles[str(t)] + place_val
        indx += 1
    elif num[indx] == '0':
        temp += ''
    else:
        if num[indx+1] == '0':
            temp += doubles[num[indx]] + ' ' + place_val
        else:
            temp += doubles[num[indx]]
    return num,indx,temp

def build_sentence(s):
    teens = ['one', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
            'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    word = ''
    list = s.split(' ')
    if len(list) > 2:
        if list[-2] in teens:
            list[-3] += ' and'
        else:
            list[-2] += ' and'
        return " ".join(list)
    return " ".join(list)

def convert_num(num):
    indx = 0
    word = ''
    while indx != len(num):
        Len = len(num[indx:len(num)])
        temp = ''
        if num[indx] == '0':
            indx += 1
            continue
        if Len == 1:
            temp += singles[num[indx]]
        elif Len == 2:
            num, indx, temp = build_teens(num,indx,temp)
        elif Len == 3:
            temp = singles[num[indx]] + ' hundred '
        elif Len == 4:
            temp = singles[num[indx]] + ' thousand '
        elif Len == 5:
            num, indx, temp = build_teens(num,indx,temp,' thousand')
        elif Len == 6:
            temp = singles[num[indx]] + ' lacs '
        elif Len == 7:
            num, indx, temp = build_teens(num, indx, temp, ' Lacs')
        elif Len == 8:
            temp = singles[num[indx]] + ' crore '
        elif Len == 9:
            num, indx, temp = build_teens(num, indx, temp, ' crore')
        word += ' ' + temp
        indx += 1
    return word

singles = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten'}
doubles = {'0':'zero','1':'ten','2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety',
        '10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen',
           '18':'eighteen','19':'nineteen','20':'twenty'}

no = '998734135'
if len(no) > 9:
    print("Number out of range !!")
    exit(0)
if no == '0':
    print('zero')
else:
    str_repr = convert_num(no).replace('  ',' ')
    str_repr = str_repr.strip()
    print(build_sentence(str_repr).capitalize())
