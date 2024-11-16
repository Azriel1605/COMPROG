def differentiate(equation, point):
    result = 0
    word = ''

    digit = False
    passing = False
    current = ''
    for char in equation:
        if passing:
            if char in '1234567890':
                digit = True
            if digit:
                if char in '-':
                    digit = False
                    passing = False
                    word += current + '+'
                    current = char
                    continue
                    
        if char in 'x^':
            passing = True
            
        current += char

    word += current
    word = word.split(sep='+')
    
    for eq in word:
        if 'x^' in eq:
            coef, power = eq.split(sep='x^')
            if not coef:
                coef = 1
            elif coef == '-':
                coef = -1
            result += int(coef) * int(power) * (point**(int(power)-1))
            continue
        if 'x' in eq:
            coef, _ = eq.split(sep='x')
            if not coef:
                coef = 1
            elif coef == '-':
                coef = -1
            result += int(coef)
    
    return result

print(differentiate("-5x^2+10x+4", 3))