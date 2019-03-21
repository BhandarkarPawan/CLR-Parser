KEYWORDS = ['int', 'main', 'char', 'switch', 'begin', 'case', 'printf', 'break', 'end', 'return']
SYMBOLS = {'(': "open_bkt", ')': "close_bkt", ';': "semi_colon", '\'': "quote",
           ':': "colon", ',': "comma", '-': "minus", '+': "plus"}

line_count = 0
tokens = []

F = open("Prog", "r")
for line in F:
    word_count = 0
    line_count += 1
    for word in line.split():
        # Check if it's an isolated keyword
        if word in KEYWORDS:
            tokens.append("keyword " + word)
        else:
            # Check if it's a keyword followed by a symbol
            buffer = []
            for character in word:
                if character.isalnum():
                    # Serves a string builder
                    buffer.append(character)
                    current_word = "".join(buffer)
                    if current_word in KEYWORDS:
                        # A fully formed keyword has been detected
                        tokens.append("keyword " + current_word)
                        buffer = []
                elif character in SYMBOLS:
                    if len(buffer) != 0:
                        if current_word.isdigit():
                            tokens.append("number " + current_word)
                        else:
                            tokens.append("identifier " + current_word)
                        buffer = []
                    # If it's a special operator
                    tokens.append("operator " + SYMBOLS[character])

for token in tokens:
    print(token)
