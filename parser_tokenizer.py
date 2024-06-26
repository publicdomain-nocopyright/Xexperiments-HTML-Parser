
from parser_library import *
# Single pass parser, but for simplicity a multipass parser might be better.
#INFO: HTML Tag: <somename> Consist of: <> tag markers and tag-name: somename
#INFO: HTML Tag can have a HTML Attribute with <somename attribute=""> and without <somename attribute> value assignment
#TODO: Match Tag with another Tag by Tag-Nesting-level.

def tokenizer():
    token = ''
    tokens = []
    htmltag = False

    for letter in htmltostring("example.html"):
        
        if letter == '<': htmltag = True; continue
        if letter == '>': htmltag = False; tokens.append(token); token=''; continue
        if htmltag:
            token += letter
            
        #print(letter, end="")
        pass
    print(tokens)


#DONE: capture text in <text> tags
def tokenizer():
    token = ''
    tokens = []
    htmltag = False
    text = ''
    start_text = False  

    #htmlfile().loadtostring()
    for letter in htmltostring("example.html"):

        if text != '' and letter == '<':
            tokens.append('<text>' + text + '</text>')
            text = ''

        if letter == '<': htmltag = True;  token = ''; continue
        if letter == '>': htmltag = False; tokens.append(token); continue

        if htmltag:
            token += letter
        if not htmltag: 
            if not start_text: start_text = True; text = ''
            text += letter


    print(tokens)

#TODO: Improve start_text

def tokenizer():
    token = ''
    tokens = []
    htmltag = False
    text = ''
    start_text = False  

    def start_text():
        nonlocal text
        nonlocal start_text
        start_text = True
        text = ''

    #htmlfile().loadtostring()
    for letter in htmltostring("example.html"):

        if text != '' and letter == '<':
            tokens.append('<htmltext>' + text + '</htmltext>')
            text = ''

        if letter == '<': htmltag = True;  token = ''; continue
        if letter == '>': htmltag = False; tokens.append(token); continue

        if htmltag:
            token += letter
        if not htmltag: 
            if not start_text: 
                start_text()
            if start_text:
                text += letter


    print(tokens)

#TODO: Nested level counting. Associate html tag with nest level.

def tokenizer():
    token = ''
    tokens = []
    htmltag = False
    text = ''
    start_text = False  

    def start_text():
        nonlocal text
        nonlocal start_text
        start_text = True
        text = ''

    nesting_level = 0 

    #htmlfile().loadtostring()
    for letter in htmltostring("example.html"):

        if letter == '/':
            nesting_level -= 1 
        if text != '' and letter == '<':
            tokens.append('<htmltext>' + text + '</htmltext>')
            text = ''

        if letter == '<': htmltag = True;  token = ''; continue
        if letter == '>': 
            htmltag = False; 
            tokens.append(token)

            nesting_level += 1 
            continue

        if htmltag:
            token += letter
        if not htmltag: 
            if not start_text: 
                start_text()
            if start_text:
                text += letter


    print(tokens)
    print(nesting_level)




def simplestatemachine():
    pass



#Latest TODO: Improve start_text


@execute
def tokenize():
    string = "Hel<test>lo!</test>"
    index = 0
    tokenOn = False
    tokens = []
    token = ''
    while index < len(string):
        if string[index] == '<': tokenOn = True 
        if tokenOn:
            token += string[index]
        if string[index] == '>': 
            tokenOn = False 
            tokens.append(token)
            token = ''

        #print(string[index], end="")

        index += 1
    print(tokens)
    
    pass