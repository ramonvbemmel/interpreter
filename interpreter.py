from AST_objects import *
from tokenize import run_tokenizer
from token_type import Token
from typing import List
from operators import *


def operator_calc(tokens: List[Token],op_to_check:List[str])->List[Token]:
    op_index = list(i for i, x in enumerate(tokens) if x.value in op_to_check)
    if len(op_index)==0:
        return tokens
    head, *tail = op_index
    lhs = int(tokens[head-1].value)
    rhs = int(tokens[head+1].value)

    if len(op_index)==1:
        tokens[head].type= 'INT'
        tokens[head].value= get_operator[tokens[head].value](int(lhs),int(rhs))
        tokens.pop(head-1)
        tokens.pop(head)
        return tokens
    else:
        tokens[head].type= 'INT'
        tokens[head].value= get_operator[tokens[head].value](int(lhs),int(rhs))
        tokens.pop(head-1)
        tokens.pop(head)
        return operator_calc(tokens)

mylist=run_tokenizer("source.txt")
print((mylist[0]))
print(operator_calc(operator_calc(mylist[0],first_operators),second_operators))





