import operator
first_operators=['maal','deel']
second_operators= ['plus','min']
all_operators= first_operators + second_operators

#used to get the write operator
get_operator= {
    'maal' : operator.mul,
    'deel' : operator.truediv,
    'plus' : operator.add,
    'min' : operator.sub,



}