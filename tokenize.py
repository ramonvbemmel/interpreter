import token_type as token
from typing import List, Callable
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
        if ' ' in words:
            return remove_empty_str(words)
    if '' in words:
        words.remove('')
        if '' in words:
            return remove_empty_str(words)
    return words

keywords = {'getal', 'zin', 'voor', 'als', 'anders', 'zolang', '='}

def get_token(words: List[str], line: int=1)-> List[token.Token]:
    head, *tail = words
    if len(words) ==1:
        if head.isdigit():
            return [token.Token('int', head, line)]
        elif head =='\n':
            return get_token(tail,line+1)
        elif head in keywords:
            return [token.Token('keyword', head, line)]
        elif '\"' in head:
            return [token.Token('string',head, line)]
        else:
            return token.Token[('id', head, line)]
    else:
        if head.isdigit():
            return [token.Token('int', head, line)] + get_token(tail)
        elif head =='\n':
            return get_token(tail,line+1)
        elif head in keywords:
            return [token.Token('keyword', head, line)] + get_token(tail)
        elif head == '\"':
            end_str=tail.index('"')
            tmp=(str(','.join(tail[:end_str])))
            complete= remove_comma(tmp)
            if len(tail[end_str+1:])== 0:
                return [token.Token('string',complete, line)]
            return [token.Token('string',complete, line)] + get_token(tail[end_str+1:])
        else:
            return [token.Token('id', head, line)] + get_token(tail)


def remove_comma(string: str)-> str:
    if ',' in string:
        return remove_comma(string.replace(',', ' '))
    else:
        return string



# print(remove_list_chars(str("hallo '[],")))

print(get_keyword_string_from_file("source.txt"))
with_space=split_on_space(get_keyword_string_from_file('source.txt'))
print(with_space)
print(get_token(remove_empty_str(with_space)))







