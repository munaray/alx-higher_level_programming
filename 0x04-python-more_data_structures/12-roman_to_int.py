#!/usr/bin/python3
def toSubtract(lastNum):
    toSub = 0
    maxList = max(lastNum)

    for n in lastNum:
        if maxList > n:
            toSub += n

    return (maxList - toSub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    romNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    listKeys = list(romNum.keys())

    num = 0
    lastRom = 0
    lastNum = [0]

    for ch in roman_string:
        for rNum in listKeys:
            if rNum == ch:
                if romNum.get(ch) <= lastRom:
                    num += toSubtract(lastNum)
                    lastNum = [romNum.get(ch)]
                else:
                    lastNum.append(romNum.get(ch))

                lastRom = romNum.get(ch)

    num += toSubtract(lastNum)

    return (num)
