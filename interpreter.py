from tokenize import run_tokenizer
from token_type import Token
from typing import List
from operators import *
from program_state import program_stat

# function to evaluate math operations. The operator is passed in the second parameter.
def operator_calc(tokens: List[Token],op_to_check:str)->List[Token]:
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
        tokens[head].type =   "RESULT"              #str(type(get_operator[tokens[head].value](lhs, rhs))).upper().strip("<CLASS> ")
        tokens[head].value = get_operator[tokens[head].value](lhs, rhs)
        tokens.pop(head - 1)
        tokens.pop(head)
        return tokens
    else:
        tokens[head].type =    "RESULT"   #          str(type(get_operator[tokens[head].value](lhs, rhs))).upper().strip("<CLASS> ")
        tokens[head].value = get_operator[tokens[head].value](lhs, rhs)
        tokens.pop(head - 1)
        tokens.pop(head)
        return operator_calc(tokens, op_to_check)

def operator_ifs(tokens: List[Token],op_to_check:List[str])->List[Token]:
    op_index = list(i for i, x in enumerate(tokens) if x.value in op_to_check)
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
        tokens[head].type =  "RESULT"                   #str(type(get_operator[tokens[head].value](lhs, rhs))).upper().strip("<CLASS> ")
        tokens[head].value = get_operator[tokens[head].value](lhs, rhs)
        tokens.pop(head - 1)
        tokens.pop(head)
        return tokens
    else:
        tokens[head].type = "RESULT"                        #str(type(get_operator[tokens[head].value](lhs, rhs))).upper().strip("<CLASS> ")
        tokens[head].value = get_operator[tokens[head].value](lhs, rhs)
        tokens.pop(head - 1)
        tokens.pop(head)
        return operator_ifs(tokens, op_to_check)

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
            try:
                index = tokens.index(next(filter(lambda x: x.type == 'RESULT', tokens)))
            except:
                index=0
            if index:
                print(tokens[index].value )
            else:
                print(tail[0].value)
    return evaluate_print(tail)

def find_jumps(tokens: List[Token]):

    if len(tokens) != 0 and tokens[0].type == 'KEYWORD' and tokens[0].value == 'als':
        end_statement= get_index_keyword(tokens,'eind_als')

        result = operator_ifs(list(tokens[1:end_statement]), bin_operators)
        if result[0].value == True:
            first = list(map(lambda op: operator_calc(tokens[end_statement+1:], op), all_operators))
            second=operate_assigns(first[-1])
            evaluate_print(second)
            return True
        else:
            return False
    return

def get_index_keyword(tokens: List[Token], keyword:str):
        return tokens.index(next(filter(lambda x: x.value == keyword, tokens)))

# runs the interperter
def interper(list_of_tokens: List[List[Token]], index:int=0):
    if  find_jumps(list_of_tokens[index]):
        if index+2 < len(list_of_tokens):
            first = list(map(lambda op: operator_calc(list_of_tokens[index+2], op), all_operators))
            assigned = operate_assigns(first[-1])
            evaluate_print(assigned)
        else:
            index= len(list_of_tokens)
    else:
        if index+1 < len(list_of_tokens):
            first = list(map(lambda op: operator_calc(list_of_tokens[index+1], op), all_operators))
            assigned = operate_assigns(first[-1])
            evaluate_print(assigned)
        else:
            index = len(list_of_tokens)

    if index >= len(list_of_tokens)-1:
        return
    else:
        return interper(list_of_tokens,index+1)
