import operator
first_operators=['*',':']
second_operators= ['+','-']
all_operators= first_operators + second_operators

#used to get the write operator
get_operator= {
    '*' : operator.mul,
    ':' : operator.truediv,
    '+' : operator.add,
    '-' : operator.sub,



}