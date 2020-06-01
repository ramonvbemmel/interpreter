import operator
first_operators=['maal','deel','plus','min', 'groter']
second_operators= ['plus','min']
bin_operators= ['groter','kleiner', 'groterOfgelijk', 'kleinerOfgelijk', 'gelijk', 'nietGelijk']
all_operators= first_operators + second_operators + bin_operators
keywords = ['als','eind_als', 'anders', 'zolang','eind_zolang', 'toon']

#used to get the write operator
get_operator= {
    'maal' : operator.mul,
    'deel' : operator.truediv,
    'plus' : operator.add,
    'min' : operator.sub,
    'groter': operator.gt,
    'kleiner': operator.lt,
    'groterOfgelijk': operator.ge,
    'kleinerOfgelijk': operator.le,
    'gelijk': operator.eq,
    'nietGelijk': operator.ne,

}