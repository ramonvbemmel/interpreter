#from typing import NamedTuple
import re

class token:
    def __init__(self, type, value,line,column):
        self.type:str = type
        self.value:str = value
        self.line: int = line
        self.column:int = column

    def __str__(self):
        return 'Token:  Type: '+repr(self.type).upper()+',\tValue: '+repr(self.value)+',\tLine: '+repr(self.line)+',\tColumn: '+repr(self.column)+''

def tokenize(code):
    keywords = {'getal', 'zin', 'voor', 'als', 'anders', 'zolang'}
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',   r'='),           # Assignment operator
        ('END',      r'\n'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-*/]'),      # Arithmetic operators
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    tmp =[]
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        tmp.append(token(kind, value, line_num, column))
    return tmp

file = open("source.txt")
lines = list(file)
tmp =[]
for line in lines:

    tmp.append(tokenize(line))

for i in tmp:
    for j in i:
        print(j)
