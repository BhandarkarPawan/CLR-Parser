grammar = []
file = open("grammar.txt", "r")
for line in file:
    line = line.rstrip()
    grammar.append(line)


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
        rhs = rhs + tempString

        # firstofproduction = first()
        # productions.append("->".join([lhs, rhs]))

    return list(zip(productions, look_ahead))


dictionary = {'I0': [('P->.SaD', '$')]}
I = dictionary['I0']
closure(I)
