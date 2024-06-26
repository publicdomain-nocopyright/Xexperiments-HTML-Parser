import parser_library

# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 
def htmltotokens(htmlstring, token = "", starttokenization = False, closingtag = False):
    for letter in htmlstring:
        if starttokenization and not letter == '>': token += letter
        if starttokenization and letter == "/": closingtag = True
        if starttokenization == False and not token == "": print(token)

        if letter == '<': starttokenization = True
        if letter == '>': starttokenization = False

        if letter == '>':
            print(token)
            token = ""

        if letter == '>' and closingtag: 
            print("It's a closing tag!")
            closingtag = False


htmltotokens(parser_library.htmltostring("example.html"))
print()
print("Tokenization")