#!/usr/bin/python3
for firstDigit in range(0, 10):
    for secondDigit in range(firstDigit + 1, 10):
        if firstDigit == 8 and secondDigit == 9:
            print("{}{}".format(firstDigit, secondDigit))
        else:
            print("{}{}".format(firstDigit, secondDigit), end=", ")
