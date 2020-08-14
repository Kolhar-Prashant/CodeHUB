def intToRoman(num) -> str:
    d = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',
         900: 'CM', 1000: 'M'}
    rom = []
    while num != 0:
        if num in d:
            rom.append(d[num])
            num -= num
        else:
            minn = 5000
            val = 0
            for k, v in d.items():
                if k > num:
                    break
                sum = abs(num - k)
                if sum < minn:
                    minn = sum
                    val = k
            num -= val
            rom.append(d[val])
    rom = "".join(rom)
    return (rom)
n = 1194
x = intToRoman(n)
print(n,"Integer to Roman number :",x)