

#token datatype
class Token:
    def __init__(self, value,line:int):
        self.value:str = value
        self.line: int = line

    def __str__(self):
        return '{Token:\tValue: '+repr(self.value)+',\tLine: '+repr(self.line)+'}'
    __repr__ = __str__


class NumToken(Token):
    def __init__(self, value: int, line):
        super().__init__(value,line)
    def __str__(self):
        return '{NUMBER: '+repr(self.value)+',\tLine: '+repr(self.line)+'}'
    __repr__ = __str__

class OpToken(Token):
    def __init__(self, value:str, line):
        super().__init__(value,line)
    def __str__(self):
        return '{OPERATOR: '+ repr(self.value) + ',\tLine: ' + repr(self.line) + '}'
    __repr__ = __str__

class StrToken(Token):
    def __init__(self, value:str, line):
        super().__init__(value,line)
    def __str__(self):
        return '{STRING: '+ repr(self.value) + ',\tLine: ' + repr(self.line) + '}'
    __repr__ = __str__

class IdToken(Token):
    def __init__(self, value:str, line):
        super().__init__(value,line)
    def __str__(self):
        return '{ID: '+ repr(self.value) + ',\tLine: ' + repr(self.line) + '}'
    __repr__ = __str__

class KeyToken(Token):
    def __init__(self, value:str, line):
        super().__init__(value,line)
    def __str__(self):
        return '{KEYWORD: '+ repr(self.value) + ',\tLine: ' + repr(self.line) + '}'
    __repr__ = __str__

class EofToken(Token):
    def __init__(self, value:str, line):
        super().__init__(value,line)
    def __str__(self):
        return '{END of File: '+ repr(self.value) + ',\tLine: ' + repr(self.line) + '}'
    __repr__ = __str__
    
class ResultToken(Token):
    def __init__(self, value, line):
        super().__init__(value,line)
    def __str__(self):
        return '{RESULT: '+ repr(self.value) + ',\tLine: ' + repr(self.line) + '}'
    __repr__ = __str__