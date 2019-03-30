SYMBOLS = ['(',
           ')',
           ';',
           ',',
           ':',
           '\'']

KEYWORDS = {'t': ['int', 'char'],
            'm': ['main'],
            'w': ['switch'],
            'b': ['begin'],
            'c': ['case'],
            'p': ['printf'],
            'k': ['break'],
            'd': ['end'],
            'r': ['return'],
            's': [' '],
            'o': ['+', '-', '='],
            'n': ['\n'],
            'q': ['do'],
            'l': ['while']}

OPERATORS = ['+', '-', '=']
line_count = 0


def getIndex(word):
    keys = list(KEYWORDS.keys())
    values = list(KEYWORDS.values())
    for value in values:
        if word in value:
            i = values.index(value)
            return keys[i]


def get_tokens(filename):
    tokens = []
    F = open(filename, "r")
    for line in F:
        for word in line.split():
            # Check if it's an isolated keyword
            token = getIndex(word)
            if token in KEYWORDS:
                tokens.append(token)
            else:
                # Check if it's a keyword followed by a symbol
                buffer = []
                for character in word:
                    if character.isalnum():
                        # Serves a string builder
                        buffer.append(character)
                        current_word = "".join(buffer)
                        token = getIndex(current_word)
                        if token in KEYWORDS:
                            # A fully formed keyword has been detected
                            tokens.append(token)
                            buffer = []
                    elif character in SYMBOLS or character in OPERATORS:
                        if len(buffer) != 0:
                            tokens.append('v')
                            buffer = []
                        # If it's a special operator
                        if character in SYMBOLS:
                            tokens.append(character)
                        else:
                            tokens.append("o")
    return tokens
