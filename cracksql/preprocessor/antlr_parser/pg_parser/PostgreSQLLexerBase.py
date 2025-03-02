from antlr4 import *


class PostgreSQLLexerBase(Lexer):

    def __init__(self, input, output):
        super().__init__(input, output)
        self.tags = []

    def pushTag(self):
        self.tags.append(super().text)

    def isTag(self):
        return super().text == self.tags[-1] if self.tags else False

    def popTag(self):
        if self.tags:
            self.tags.pop()

    def checkLA(self, c):
        return super().inputStream.LA(1) != c

    def charIsLetter(self):
        return super().inputStream.LA(-1).isalpha()

    def HandleNumericFail(self):
        super().inputStream.seek(super().inputStream.index() - 2)
        super().type(658)

    def HandleLessLessGreaterGreater(self):
        text = super().text
        if text == "<<":
            super().type(18)
        elif text == ">>":
            super().type(19)

    def UnterminatedBlockCommentDebugAssert(self):
        # Debug.Assert(InputStream.LA(1) == -1 /*EOF*/)
        pass

    def CheckIfUtf32Letter(self):
        code_point = super().inputStream.LA(-2) << 8 + super().inputStream.LA(-1)
        if code_point < 0x10000:
            c = [chr(code_point)]
        else:
            code_point -= 0x10000
            c = [chr(code_point // 0x400 + 0xd800),
                 chr(code_point % 0x400 + 0xdc00)]
        return c[0].isalpha()
