from tokenize import run_tokenizer
from token_type import *
from typing import List
from operators import *
from program_state import program_stat
from function_call_counter import function_call_counter

# function to evaluate math operations. The operator is passed in the second parameter.
def operator_calc(tokens: List[Token],op_to_check:str)->List[Token]:
    op_index = list(i for i, x in enumerate(tokens) if x.value == op_to_check)
    if len(op_index) == 0:
        return tokens
    head, *tail = op_index

    # check if a var is passed so the value comes from programstate
    if isinstance(tokens[head-1],IdToken):
        lhs = program_stat[tokens[head - 1].value]
    else:
        lhs = tokens[head - 1].value
    # check if a var is passed so the value comes from programstate
    if isinstance(tokens[head + 1], IdToken):
        rhs = program_stat[tokens[head + 1].value]
    else:
        rhs = tokens[head + 1].value

    # voor numeric operatons the type has to be int.
    if tokens[head].value in first_operators or tokens[head].value in second_operators:
        lhs = int(lhs)
        rhs = int(rhs)

    if len(op_index) == 1:
        tmp_line= tokens[head].line
        tokens[head]= ResultToken(get_operator[tokens[head].value](lhs, rhs), tmp_line)
        tokens.pop(head - 1)
        tokens.pop(head)
        return tokens
    else:
        tmp_line= tokens[head].line
        tokens[head]= ResultToken(get_operator[tokens[head].value](lhs, rhs), tmp_line)
        tokens.pop(head - 1)
        tokens.pop(head)
        return operator_calc(tokens, op_to_check)

def operator_ifs(tokens: List[Token],op_to_check:List[str])->List[Token]:
    op_index = list(i for i, x in enumerate(tokens) if x.value in op_to_check)
    if len(op_index) == 0:
        return tokens
    head, *tail = op_index

    # check if a var is passed so the value comes from programstate
    if isinstance(tokens[head - 1],IdToken) :
        lhs = program_stat[tokens[head - 1].value]
    else:
        lhs = tokens[head - 1].value
    # check if a var is passed so the value comes from programstate
    if isinstance(tokens[head - 1],IdToken) :
        rhs = program_stat[tokens[head - 1].value]
    else:
        rhs = tokens[head + 1].value

    # voor numeric operatons the type has to be int.
    if tokens[head].value in first_operators or tokens[head].value in second_operators:
        lhs = int(lhs)
        rhs = int(rhs)

    if len(op_index) == 1:
        tmp = tokens[head].line
        tokens[head] = ResultToken(get_operator[tokens[head].value](lhs, rhs), tmp)
        tokens.pop(head - 1)
        tokens.pop(head)
        return tokens
    else:
        tmp = tokens[head].line
        tokens[head] = ResultToken(get_operator[tokens[head].value](lhs, rhs), tmp)
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
    if isinstance(head,KeyToken) and str(head.value)== 'toon':
        if isinstance(tail[0], IdToken) :
            print(program_stat[tail[0].value])
        else:
            try:
                index = tokens.index(next(filter(lambda x: isinstance(x, ResultToken), tokens)))
            except:
                index=0
            if index:
                print(tokens[index].value )
            else:
                print(tail[0].value)
    return evaluate_print(tail)

def get_index_keyword(tokens: List[Token], keyword: str):
    return tokens.index(next(filter(lambda x: x.value == keyword, tokens)))

def find_jumps(tokens: List[Token]):

    if len(tokens) != 0  and tokens[0].value == 'als':
        end_statement= get_index_keyword(tokens,'eind_als')
        result = operator_ifs(list(tokens[1:end_statement]), bin_operators)
        if  result[0].value == True:
            first = list(map(lambda op: operator_calc(tokens[end_statement+1:], op), first_operators +second_operators))
            second=operate_assigns(first[-2])
            evaluate_print(second)
            return True
        else:
            return False
    return None

@function_call_counter
def evaluate_loop_statement(tokens: List[Token]):
    if len(tokens)==1:
        return bool(tokens[0].value)
    if isinstance(tokens[0],IdToken):
        lhs = program_stat[tokens[0].value]
    else:
        lhs = tokens[0].value
    if isinstance(tokens[2],IdToken):
        rhs = program_stat[tokens[2].value]
    else:
        rhs=  tokens[2].value
    return get_operator[tokens[1].value](int(lhs),int(rhs))

def find_loop(tokens: List):

    if len(tokens) != 0  and tokens[0].value == 'zolang':
        end_statement= get_index_keyword(tokens,'eind_zolang')

        result= evaluate_loop_statement(tokens[1:end_statement])
        if  result == True:
            first = list(map(lambda op: operator_calc(tokens[end_statement+1:], op), first_operators +second_operators))
            second=operate_assigns(first[-2])
            evaluate_print(second)
            return True
        else:
            return False
    return None


# runs the interperter
def interper(list_of_tokens: List[List[Token]], index:int=0):
    loop_state = find_loop(list(list_of_tokens[index]))
    if loop_state == True:
        return interper(list_of_tokens, index)
    elif loop_state == False:
        return interper(list_of_tokens, index+1)

    jumped=find_jumps(list_of_tokens[index])
    #statement was true and executed
    if jumped==True:
        #checks if there is no new statement then execute next line.
        if index+1 < len(list_of_tokens) :
            #if anders presented skip the else.
            if len(list_of_tokens[index+1]) > 0 and list_of_tokens[index+1][0].value == 'anders':
                index+=1

    #statement was false so line not executed.
    elif jumped==False :
        #when else of if else  is detected excute this
        if index+1 < len(list_of_tokens) and len(list_of_tokens[index+1]) < 0  and list_of_tokens[index+1][0].value == 'anders':
           # print("verwijder anders ")
            list_of_tokens[index + 1].pop(0)


    #no if or else in line
    elif jumped==None:
       # print("geen ifs gevonden")
        first = list(map(lambda op: operator_calc(list_of_tokens[index], op), all_operators))
        assigned = operate_assigns(first[-1])
        evaluate_print(assigned)

    if index >= len(list_of_tokens)-1:
        return
    else:
        return interper(list_of_tokens,index+1)
