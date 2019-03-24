import pandas as pd

EPSILON = "e"


def get_productions(X):
    productions = []
    for prod in grammar:
        lhs, rhs = prod.split('->')
        if lhs == X:
            rhs = '.'+rhs
            productions.append('->'.join([lhs, rhs]))
    return productions


def closure(I):
    for production, a in I:
        if production.endswith("."):
            continue
        # look_ahead = '|'.split(look_ahead)
        lhs, rhs = production.split('->')
        alpha, B_beta = rhs.split('.')
        B = B_beta[0]
        beta = B_beta[1:]
        # for a in look_ahead:
        beta_a = beta + a
        first_beta_a = first(beta_a)
        for b in first_beta_a:
            B_productions = get_productions(B)
            for gamma in B_productions:
                new_item = (gamma, b)
                if (new_item not in I):
                    I.append(new_item)
    return I


def get_symbols(grammar):
    # Check the grammar and get the set of terminals and non_terminals
    terminals = set()
    non_terminals = set()
    for production in grammar:
        lhs, rhs = production.split('->')
        # Set of non terminals only
        non_terminals.add(lhs)
        for x in rhs:
            # Add add symbols to terminals
            terminals.add(x)
    # Remove the non terminals
    terminals = terminals.difference(non_terminals)
    terminals.add('$')
    return terminals, non_terminals


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


def shift_dot(production):
    # This function shifts the dot to the right
    lhs, rhs = production.split('->')
    x, y = rhs.split(".")
    if(len(y) == 0):
        # TODO: Improve this part.
        print("Dot at the end!")
        return
    elif len(y) == 1:
        y = y[0]+"."
    else:
        y = y[0]+"."+y[1:]
    rhs = "".join([x, y])
    return "->".join([lhs, rhs])


def goto(I, X):
    # Function to calculate GOTO
    J = []
    for production, look_ahead in I:
        lhs, rhs = production.split('->')
        if "."+X in rhs and not rhs[-1] == '.':
            # Check if the production ends with a dot, else shift dot
            new_prod = shift_dot(production)
            J.append((new_prod, look_ahead))
    return closure(J)


def set_of_items():
    # Function to construct the set of items
    # TODO: Change it to return a dictionary
    C = closure([('P->.S', '$')])
    for I in C:
        # For each items I in C
        for X in symbols:
            # For each grammar symbol X
            goto_I_X = goto(I, X)
            if not len(goto_I_X) == 0:
                # If Goto(I,X) is not empty and not in C
                if goto_I_X not in C:
                    # Add Goto(I,X) to C
                    C.extend(goto_I_X)
    return C


def CLR_construction(grammar):
    C = set_of_items()
    # Construction ACTION function
    pass


if __name__ == "__main__":

    # Demo grammars
    grammar = ['E->TX', 'X->+TX', 'X->e', 'T->FY', 'Y->*FY', 'Y->e', 'F->(E)', 'F->i']
    grammar = ['S->Cc', 'C->cC', 'C->d']
    grammar = ['S->L=R', 'S->R', 'L->*R', 'L->i', 'R->L']

    terminals, non_terminals = get_symbols(grammar)
    symbols = terminals.union(non_terminals)

    ACTION = pd.DataFrame(columns=terminals)
    GOTO = pd.DataFrame(columns=non_terminals)

    I = [('P->.S', '$')]
    I0 = closure(I)
