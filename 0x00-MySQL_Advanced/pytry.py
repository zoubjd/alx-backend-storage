#!/usr/bin/python3

def plusOne(digits):
        sum = 0
        for digit in digits:
                sum = sum*10 + digit

        sum += 1
        retvalue = []

        while sum > 0:
            value = sum % 10
            sum = sum // 10
            retvalue.append(value)

        retvalue = retvalue [::-1]

        return retvalue

print(plusOne([9,9]))
        