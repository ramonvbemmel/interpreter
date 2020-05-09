import token_type as token
from typing import List
import re

#read lines from file and put them in a list.
def get_keyword_string_from_file(filename: str)->List[str]:
    return list(open(filename))

#Split al words on spaces into a list.
def split_on_space(lines: List[str])->List[str]:
    if len(lines)==1:
        return re.split('(\W)', lines[0])
    else:
        head, *tail = lines
        return re.split('(\W)', head) + split_on_space(tail)

#removes whitespaces and empty strings out of list
def remove_empty_str(words: List[str])-> List[str]:
    if ' ' in words:
        words.remove(' ')
        return remove_empty_str(words)
    if '' in words:
        words.remove('')
        return remove_empty_str(words)
    return words

#Returns a list of token objects. Conaining Type, value and line number.
def get_token(words: List[str], line: int=1)-> List[token.Token]:
    keywords = {'getal', 'zin', 'voor', 'als', 'anders', 'zolang', '='}
    head, *tail = words
    if len(words) ==1:
        if head.isdigit():
            return [token.Token('INT', head, line)]
        elif head =='\n':
            return get_token(tail,line+1)
        elif head in keywords:
            return [token.Token('KEYWORD', head, line)]
        elif '\"' in head:
            return [token.Token('STRING',head, line)]
        else:
            return token.Token[('ID', head, line)]
    else:
        if head.isdigit():
            return [token.Token('INT', head, line)] + get_token(tail,line)
        elif head =='\n':
            return get_token(tail,line+1)
        elif head in keywords:
            return [token.Token('KEYWORD', head, line)] + get_token(tail,line)
        elif head == '\"':
            end_str=tail.index('"')
            joined_list=(str(' '.join(tail[:end_str])))
            if len(tail[end_str+1:])== 0:
                return [token.Token('STRING',joined_list, line)]
            return [token.Token('STRING',joined_list, line)] + get_token(tail[end_str+1:],line)
        else:
            return [token.Token('ID', head, line)] + get_token(tail,line)



with_space=split_on_space(get_keyword_string_from_file('source.txt'))
print(with_space)
print(get_token(remove_empty_str(with_space)))







