EPSILON = "e"

# Temporary data
terminals = ['+', 'e', '*', '(', ')', 'i', '$']
grammar = ['E->TX', 'X->+TX', 'X->e', 'T->FY', 'Y->*FY', 'Y->e', 'F->(E)', 'F->i']


def find_look_ahead(beta_a):
    first_beta_a = []
    for symbol in beta_a:
        first_beta_a.extend(first(symbol))
    return first_beta_a


def first(symbols):
    # Find the first of the symbol 'X' w.r.t the grammar
    final_set = []
    for X in symbols:
        first_set = []  # Will contain the final set first(X)
        if isTerminal(X):
            return [X]
        else:
            for production in grammar:
                # For each production in the grammar
                lhs, rhs = production.split('->')
                if lhs == X:
                    # Check if the LHS is 'X'
                    for i in range(len(rhs)):
                        # To find the first of the RHS
                        y = rhs[i]
                        # Check one symbol at a time
                        first_y = first(y)
                        first_set.extend(first_y)
                        # Check next symbol only if first(current) contains EPSILON
                        if EPSILON in first_y:
                            first_set.remove(EPSILON)
                            continue
                        else:
                            # No EPSILON. Move to next production
                            break
                    else:
                        # All symbols contain EPSILON. Add EPSILON to first(X)
                        first_set.extend(EPSILON)
        final_set.extend(first_set)
    return list(set(final_set))


def isTerminal(symbol):
    # This function will return if the symbol is a terminal or not
    return symbol in terminals


def shift_dot(rhs):
    # This function shifts the dot to the right
    print(rhs)
    x, y = rhs.split(".")
    if(len(y) == 0):
        # TODO: Improve this part.
        print("Dot at the end!")
        return
    elif len(y) == 1:
        y = y[0]+"."
    else:
        y = y[0]+"."+y[1:]
    return "".join([x, y])


def goto(I, X):
    productions, look_aheads = zip(*I)
    for i in len(I):


first('XY')

production = "X->e"
production
lhs, rhs = production.split('->')
rhs = "."+rhs
production = "->".join([lhs, rhs])
production
