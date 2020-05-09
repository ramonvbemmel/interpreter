

#token datatype
class Token:
    def __init__(self, type, value,line):
        self.type:str = type
        self.value:str = value
        self.line: int = line

    def __str__(self):
        return '{Token:  Type: '+repr(self.type).upper()+',\tValue: '+repr(self.value)+',\tLine: '+repr(self.line)+'}'
    __repr__ = __str__

operators= {}