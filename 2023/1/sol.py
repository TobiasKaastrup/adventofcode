f = open("1-input.txt", "r")
lines = f.readlines()

digits = []
result = 0
counter = 1

def replacer(numstring):
    numstring = numstring.replace('one','one1one')
    numstring = numstring.replace('two','two2two')
    numstring = numstring.replace('three','three3three')
    numstring = numstring.replace('four','four4four')
    numstring = numstring.replace('five','five5five')
    numstring = numstring.replace('six','six6six')
    numstring = numstring.replace('seven','seven7seven')
    numstring = numstring.replace('eight','eight8eight')
    numstring = numstring.replace('nine','nine9nine')
    return numstring

for line in lines:
    strippedLine = ''
    for char in replacer(line):
        if char.isdigit():
            strippedLine += char
    two_digit_string = strippedLine[0] + strippedLine[-1]
    digits.append(int(two_digit_string))
    print(f"{counter}) {int(two_digit_string)}")
    counter += 1

for digit in digits:
    result += digit

print(result)