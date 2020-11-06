def romanToInt(s):
    number = 0
    romans = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
    }
    skip = False
    for i in range(len(s)):
        if skip:
            skip = False
            continue
        if i < len(s)-1:
            if romans[s[i]] >= romans[s[i+1]]:
                number += romans[s[i]]
            else:
                skip = True
                number += (romans[s[i+1]] - romans[s[i]])
        else:
            number += romans[s[i]]
    return number
