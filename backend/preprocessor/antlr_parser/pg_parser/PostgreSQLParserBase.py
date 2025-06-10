from antlr4 import *
from antlr4.CommonTokenStream import CommonTokenStream


from PostgreSQLLexer import PostgreSQLLexer
from PostgreSQLParser import PostgreSQLParser

class PostgreSQLParserBase(Parser):

    def __init__(self, input_stream: TokenStream):
        super().__init__(input_stream)
    