
class Base_node(object):
    pass

class Operator_node(Base_node):
    def __init__(self, left, operator, right):
        self.left=left
        self.token = self.operator = operator
        self.right = right

