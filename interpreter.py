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

    #check if a var is passed so the value comes from programstate
    if tokens[head-1].type == 'ID':
        lhs = program_stat[tokens[head-1].value]
    else:
        lhs = tokens[head-1].value
    # check if a var is passed so the value comes from programstate
    if tokens[head - 1].type == 'ID':
        rhs = program_stat[tokens[head - 1].value]
    else:
        rhs = tokens[head+1].value

    # voor numeric operatons the type has to be int.
    if tokens[head].value in first_operators or tokens[head].value in second_operators:
        lhs = int(lhs)
        rhs = int(rhs)

    if len(op_index)==1:
        tokens[head].type= str(type(get_operator[tokens[head].value](lhs,rhs))).upper().strip("<CLASS> ")
        tokens[head].value= get_operator[tokens[head].value](lhs,rhs)
        tokens.pop(head-1)
        tokens.pop(head)
        return tokens
    else:
        tokens[head].type= str(type(get_operator[tokens[head].value](lhs,rhs))).upper().strip("<CLASS> ")
        tokens[head].value= get_operator[tokens[head].value](lhs,rhs)
        tokens.pop(head-1)
        tokens.pop(head)
        return operator_calc(tokens,op_to_check)

def operator_calc_tess(tokens: List[Token],op_to_check:str)->List[Token]:
    op_index = list(i for i, x in enumerate(tokens) if x.value == op_to_check)

    if len(op_index) == 0:
        return tokens
    head, *tail = op_index

    # check if a var is passed so the value comes from programstate
    if tokens[head - 1].type == 'ID':
        lhs = program_stat[tokens[head - 1].value]
    else:
        lhs = tokens[head - 1].value
    # check if a var is passed so the value comes from programstate
    if tokens[head - 1].type == 'ID':
        rhs = program_stat[tokens[head - 1].value]
    else:
        rhs = tokens[head + 1].value

    # voor numeric operatons the type has to be int.
    if tokens[head].value in first_operators or tokens[head].value in second_operators:
        lhs = int(lhs)
        rhs = int(rhs)

    if len(op_index) == 1:
        tokens[head].type = str(type(get_operator[tokens[head].value](lhs, rhs))).upper().strip("<CLASS> ")
        tokens[head].value = get_operator[tokens[head].value](lhs, rhs)
        tokens.pop(head - 1)
        tokens.pop(head)
        return tokens
    else:
        tokens[head].type = str(type(get_operator[tokens[head].value](lhs, rhs))).upper().strip("<CLASS> ")
        tokens[head].value = get_operator[tokens[head].value](lhs, rhs)
        tokens.pop(head - 1)
        tokens.pop(head)
        return operator_calc_tess(tokens, op_to_check)


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

def loop_operator(tok: List[Token], op:List[str]=all_operators )->List[Token]:
    head, *tail = op
    if len(op) == 1:
        operator_calc_tess(tok,head)
        return operator_calc_tess(tok, head)
    else:

        operator_calc_tess(tok, head)
        loop_operator(tail)
        return operator_calc_tess(tok, head)


# runs the interperter
def interper(list_of_tokens: List[List[Token]], index:int=0):
    first = list(map(lambda op: operator_calc_tess(list_of_tokens[index], op), all_operators))
    assigned = operate_assigns(first[-1])
    evaluate_print(assigned)
    if index >= len(list_of_tokens)-1:
        return
    else:
        return interper(list_of_tokens,index+1)
