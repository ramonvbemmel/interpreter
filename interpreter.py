from AST_objects import *
from tokenize import run_tokenizer
from token_type import Token
from typing import List

operators = {'+', ':', '*', '-', '='}
def test(tokens: List[Token]):
    first_precedence = list(i for i, x in enumerate(tokens) if x.value in operators)
    print(tokens[first_precedence[0]+1].value)




mylist=run_tokenizer("source.txt")
print(test(mylist[0]))






