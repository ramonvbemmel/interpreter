from tokenize import run_tokenizer
from token_type import Token
from typing import List
from operators import *
from program_state import program_stat

# function to evaluate math operations. usable for first and second predence.
# With the second parameter a list of first or second operators
def operator_calc(tokens: List[Token],op_to_check:List[str])->List[Token]:
    op_index = list(i for i, x in enumerate(tokens) if x.value in op_to_check)

    if len(op_index)==0:
        return tokens
    head, *tail = op_index

    
    if tokens[head-1].type == 'ID':
        lhs = program_stat[tokens[head-1].value]
    else:
        lhs = tokens[head-1].value

    if tokens[head - 1].type == 'ID':
        rhs = program_stat[tokens[head + 1].value]
    else:
        rhs = tokens[head+1].value
    if tokens[head].value in first_operators or tokens[head].value in second_operators:
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
            return operator_calc(tokens,op_to_check)
    elif tokens[head].value in bin_operators:
        if len(op_index)==1:
            tokens[head].type= 'BOOL'
            tokens[head].value= get_operator[tokens[head].value](int(lhs),int(rhs))
            tokens.pop(head-1)
            tokens.pop(head)
            return tokens
        else:
            tokens[head].type= 'BOOL'
            tokens[head].value= get_operator[tokens[head].value](bool(lhs),bool(rhs))
            tokens.pop(head-1)
            tokens.pop(head)
            return operator_calc(tokens,op_to_check)


# function to handle assign operations
def operate_assigns(tokens: List[Token])->List[Token]:
    op_index = list(i for i, x in enumerate(tokens) if x.value in ['is'])
    if len(op_index)==0:
        return tokens
    head, *tail = op_index
    identifer = str(tokens[head-1].value)
    rhs = tokens[head+1].value

    if len(op_index)==1:
        program_stat[identifer]= rhs
        tokens.pop(head)
        tokens.pop(head)
        return tokens
    else:
        program_stat[identifer]= rhs
        tokens.pop(head)
        tokens.pop(head)
        return operate_assigns(tokens)

# function to print
def evaluate_print(tokens: List[Token]):
    if len(tokens)<1:
        return
    head, *tail = tokens
    #print(head.type, head.value)
    if head.type == "KEYWORD" and str(head.value)== 'toon':
        if tail[0].type== "ID":
            print(program_stat[tail[0].value])
        else:
            print(tail[0].value)
    return evaluate_print(tail)

# runs the interperter
def interper(list_of_tokens: List[List[Token]], index:int=0):
    first = operator_calc(list_of_tokens[index], first_operators)
    #print(first)
    second = operator_calc(first, second_operators)
    #print(second)
    third= operator_calc(second,bin_operators)
    assigned = operate_assigns(second)
    #print(assigned)
    evaluate_print(assigned)
    if index >= len(list_of_tokens)-1:
        return
    else:
        return interper(list_of_tokens,index+1)
