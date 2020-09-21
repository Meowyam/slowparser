#!/usr/bin/python

# define token types

NUMS = "0123456789"
INT = "INT"
FLOAT = "FLOAT"
PLUS = "+"
MINUS = "-"
MULT = "*"
DIV = "/"
LPAR = "("
RPAR = ")"


class Token:
    def __init__(self, tokenType, value=None):
        self.tokenType = tokenType
        self.value = value

    def __repr__(self):
        # return the value if there's a value
        if self.value:
            return f"{self.value}"
        # else just return the type
        else:
            return f"{self.tokenType}"


class Lexer:
    def __init__(self, toParse):
        self.toParse = toParse
        # starting position
        self.pos = -1
        # current charAtPosacter
        self.charAtPos = None
        self.move()

    # move through the toParse
    def move(self):
        self.pos += 1
        self.charAtPos = (
            self.toParse[self.pos] if self.pos < len(self.toParse) else None
        )

    def makeNum(self):
        isFloat = False
        getNum = ""
        while self.charAtPos is not None and self.charAtPos in NUMS + ".":
            # if has dot then is float
            if self.charAtPos == ".":
                isFloat = True
                getNum += "."
            else:
                getNum += self.charAtPos
            self.move()

        if isFloat is True:
            return Token(FLOAT, float(getNum))
        else:
            return Token(INT, int(getNum))

    def tokenise(self):
        tokens = []
        while self.charAtPos is not None:
            if self.charAtPos in NUMS:
                tokens.append(self.makeNum())
            elif self.charAtPos == "+":
                tokens.append(Token(PLUS))
                self.move()
            elif self.charAtPos == "-":
                tokens.append(Token(MINUS))
                self.move()
            elif self.charAtPos == "*":
                tokens.append(Token(MULT))
                self.move()
            elif self.charAtPos == "/":
                tokens.append(Token(DIV))
                self.move()
            elif self.charAtPos == "(":
                tokens.append(Token(LPAR))
                self.move()
            elif self.charAtPos == ")":
                tokens.append(Token(RPAR))
                self.move()
            # else just read past it
            else:
                self.move()
        return tokens


def parse(toParse):
    lexer = Lexer(toParse)
    tokens = lexer.tokenise()

    return tokens


string = "2 + 1"
print(parse(string))
