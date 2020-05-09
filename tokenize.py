from token_type import Token
from typing import List
from re import split

#read lines from file and put them in a list.
def get_keyword_string_from_file(filename: str)->List[str]:
    return list(open(filename))

#Split al words on spaces into a list.
def split_on_space(lines: List[str])->List[str]:
    if len(lines)==1:
        return split('(\W)', lines[0])
    else:
        head, *tail = lines
        return split('(\W)', head) + split_on_space(tail)

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
def get_token(words: List[str], line: int=1)-> List[Token]:
    keywords = {'getal', 'zin', 'voor', 'als', 'anders', 'zolang', '='}
    head, *tail = words
    if len(words) ==1:
        if head.isdigit():
            return [Token('INT', head, line)]
        elif head =='\n':
            return get_token(tail,line+1)
        elif head in keywords:
            return [Token('KEYWORD', head, line)]
        elif '"' in head:
            return [Token('STRING',head, line)]
        elif head.isalpha():
            return Token[('ID', head, line)]
        #else:
            #exception
    else:
        if head.isdigit():
            return [Token('INT', head, line)] + get_token(tail,line)
        elif head =='\n':
            return get_token(tail,line+1)
        elif head in keywords:
            return [Token('KEYWORD', head, line)] + get_token(tail,line)
        elif head == '"':
            end_str=tail.index('"')
            joined_list=(str(' '.join(tail[:end_str])))
            if len(tail[end_str+1:])== 0:
                return [Token('STRING',joined_list, line)]
            return [Token('STRING',joined_list, line)] + get_token(tail[end_str+1:],line)
        elif head.isalpha():
            return [Token('ID', head, line)] + get_token(tail,line)
        #else:
            #exception


#print(get_keyword_string_from_file('source.txt'))

with_space=split_on_space(get_keyword_string_from_file('source.txt'))
#print(with_space)
print(get_token(remove_empty_str(with_space)))







