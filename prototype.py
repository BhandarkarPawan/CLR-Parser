#grammar = ['P->SaD','S->a','D->b']

file = open("grammar.txt", "r")
for line in file:
    line = line.rstrip()
    grammar.append(line)
#non_terminals = ['S','D']
def closure(I):
    productions, look_ahead = zip(*I)
    productions = list(productions)
    look_ahead = list(look_ahead)
    for item in productions:
        lhs, rhs = 0, 0
        lhs, rhs = item.split('.')
        nextProduction = rhs[0]
        lhs, rhs = 0, 0
        lhs, rhs = item.split(nextProduction)
        tempString = ""
        tempString = tempString.join(look_ahead)
        firstVariables = rhs + tempString
        if nextProduction in non_terminals:
            lhs, rhs = 0, 0
            for eachGrammar in grammar:
                lhs, rhs = eachGrammar.split('->')
                if lhs == nextProduction:
                    rhs = '.' + rhs
                    eachGrammar = "->".join([lhs,rhs])
                    productions.append(eachGrammar)
                    look_ahead.append(first(firstVariables))

        # firstofproduction = first()
        # productions.append("->".join([lhs, rhs]))

    return list(zip(productions, look_ahead))

dictionary = {'I0': [('P->.SaD', '$')]}
I = dictionary['I0']
closure(I)
