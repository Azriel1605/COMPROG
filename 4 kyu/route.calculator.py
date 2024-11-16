def calculate(expression):
    try:
        if '+' not in expression and '-' not in expression and '*' not in expression and '$' not in expression:
            return float(expression)
        operator = '+-'
        equation = []
        text = ''
        current = ''
        for i in expression:
            # print(i)
            if i in operator:
                current += f' {i} '
                # print(i)
                continue
            current += i
            
        current = current.split()
        partial = []
        operator = []
        print(current)
        for eq in current:
            if '*' in eq or '$' in eq:
                this_number = []
                this_operator = []
                this_current = ''
                for i in eq:
                    if i in '*$':
                        this_operator.append(i)
                        this_number.append(this_current)
                        this_current = ''
                        continue
                    this_current += i
                this_number.append(this_current)
                # print(this_number)
                # print(this_operator)
                # print(this_number[0])
                start = int(this_number[0])
                for number, calculation in zip(this_number[1:], this_operator):
                    if calculation == '*':
                        start = start * float(number)
                    if calculation == '$':
                        start = start / float(number)
                partial.append(start)
                continue
                
                
            if '-' in eq or '+' in eq:
                operator.append(eq)
                continue
            
            partial.append(int(eq))
            print('AKHIR')
            
        print(partial)
        print(operator)
        
        result = partial[0]
        for i, j in zip(partial[1:], operator):
            if j == '+':
                result += i
            if j == '-':
                result -= i
                
        return result
    except:
        return "400: Bad request"
    
print(calculate('5+8-8*2$4'))