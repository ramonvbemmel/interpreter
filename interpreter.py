import re
from typing import Iterator
from typing import List
import token_type

#keywords and token specifications
class Keywords:
    keywords = {'getal', 'zin', 'voor', 'als', 'anders', 'zolang'}
    token_specification = {
        ('NUMBER', r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN', r'='),  # Assignment operator
        ('END', r'\n'),  # Statement terminator
        ('ID', r'[A-Za-z]+'),  # Identifiers
        ('OP', r'[+\-*/]'), # Arithmetic operators
        ('SKIP', r'[ \t]+'),  # Skip over spaces and tabs
        ('MISMATCH', r'.')  # Any other character
    }

# def tokenize(regex_it: Iterator, line_start: int= -1, line_num: int =1 )-> List[Token]:
#
#     mo = re.finditer(tok_regex,code)
#     kind = mo.lastgroup
#     value = mo.group()
#     column = mo.start() - line_start
#     if kind == 'NUMBER':
#         value = float(value) if '.' in value else int(value)
#     elif kind == 'ID' and value in Keywords.keywords:
#         kind = value
#     elif kind == 'NEWLINE':
#         line_start = mo.end()
#         line_num += 1
#         return tokenize(code, next(tok_regex))
#     elif kind == 'SKIP':
#         return tokenize(code, next(tok_regex))
#     elif kind == 'MISMATCH':
#         raise RuntimeError(f'{value!r} unexpected on line {line_num}')
#     #yield (kind,value,line_num,column)
#     return [Token(kind,value,line_num,column)] + tokenize(code, next(tok_regex))

def tokenize(regex_iterator: Iterator, line_start: int = -1, line_num: int = 1) -> List[token_type.Token]:
    try:
        match = next(regex_iterator)
    except StopIteration:
        return
        # Error

    kind = match.lastgroup
    value = match.group()
    column = match.start() - line_start

    if kind == 'SKIP':
        return tokenize(regex_iterator, line_start, line_num)

    if kind == 'NUMBER':
        value = float(value) if '.' in value else int(value)

    elif kind == 'ID' and value in Keywords.keywords:
        kind = value

    elif kind == 'NEWLINE':
        return tokenize(regex_iterator, match.end(), line_num + 1)

    elif kind == 'MISMATCH':
        #Raise error
        pass
    return token_type.Token(kind, value, line_num, column) + tokenize(regex_iterator, line_start, line_num)



tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in Keywords.token_specification)
file = open("source.txt")
lines = list(file)
print(lines)

tmp =[]
#print(type(lines))
#tokenize(lines)
for line in lines:
    tokenize(tok_regex)
    # for token in tokenize(line,tok_regex):
    #     print(token)
