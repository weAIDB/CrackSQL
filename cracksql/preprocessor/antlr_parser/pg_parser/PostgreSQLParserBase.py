from antlr4 import *
from antlr4.CommonTokenStream import CommonTokenStream

from preprocessor.antlr_parser.pg_parser.LexerDispatchingErrorListener import LexerDispatchingErrorListener
from preprocessor.antlr_parser.pg_parser.ParserDispatchingErrorListener import ParserDispatchingErrorListener
from PostgreSQLLexer import PostgreSQLLexer
from PostgreSQLParser import PostgreSQLParser


class PostgreSQLParserBase(Parser):

    def __init__(self, input_stream: TokenStream):
        super().__init__(input_stream)

    def parse_routine_body(self, _localctx: PostgreSQLParser.Createfunc_opt_listContext):
        lang = None
        for coi in _localctx.createfunc_opt_item():
            if coi.LANGUAGE() is not None:
                if coi.nonreservedword_or_sconst() is not None:
                    if coi.nonreservedword_or_sconst().nonreservedword() is not None:
                        if coi.nonreservedword_or_sconst().nonreservedword().identifier() is not None:
                            if coi.nonreservedword_or_sconst().nonreservedword().identifier().Identifier() is not None:
                                lang = coi.nonreservedword_or_sconst().nonreservedword().identifier().Identifier().getText()
                                break

        if lang is None:
            return

        func_as = None
        for a in _localctx.createfunc_opt_item():
            if a.func_as() is not None:
                func_as = a
                break

        if func_as is not None:
            txt = self.get_routine_body_string(func_as.func_as().sconst(0))
            postgreSQL_parser = self.get_postgresql_parser(txt)
            if lang == "plpgsql":
                func_as.func_as().Definition = postgreSQL_parser.plsqlroot()
            elif lang == "sql":
                func_as.func_as().Definition = postgreSQL_parser.root()

    def trim_quotes(self, s: str) -> str:
        return s[1:-1] if s and len(s) > 1 else s

    def unquote(self, s: str) -> str:
        slength = len(s)
        r = []
        i = 0
        while i < slength:
            c = s[i]
            r.append(c)
            if c == '\'' and i < slength - 1 and s[i + 1] == '\'':
                i += 1
            i += 1
        return ''.join(r)

    def get_routine_body_string(self, rule: PostgreSQLParser.SconstContext) -> str:
        anysconst = rule.anysconst()
        string_constant = anysconst.StringConstant()
        if string_constant is not None:
            return self.unquote(self.trim_quotes(string_constant.getText()))
        unicode_escape_string_constant = anysconst.UnicodeEscapeStringConstant()
        if unicode_escape_string_constant is not None:
            return self.trim_quotes(unicode_escape_string_constant.getText())
        escape_string_constant = anysconst.EscapeStringConstant()
        if escape_string_constant is not None:
            return self.trim_quotes(escape_string_constant.getText())
        result = ''
        dollar_text = anysconst.DollarText()
        for s in dollar_text:
            result += s.getText()
        return result

    