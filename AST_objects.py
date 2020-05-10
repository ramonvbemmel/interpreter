from token_type import Token


#abstract AST node
class Base_node(object):
    pass

#Node wich hold operators
class Operator_node(Base_node):
    def __init__(self, left, operator, right):
        self.left=left
        self.token = self.operator = operator
        self.right = right

#node for numberic values.
class Constant_node(Base_node):
    def __init__(self,Token):
        self.Token=Token
        self.value=Token.value




