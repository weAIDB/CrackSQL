from antlr4.error.ErrorListener import ErrorListener


class ParserDispatchingErrorListener(ErrorListener):
    def __init__(self, parent):
        self._parent = parent

    def syntaxError(self, recognizer, offending_symbol, line, char_position_in_line, msg, e):
        # In Python, the error listeners are stored in a list, so we iterate over them.
        for listener in self._parent.getErrorListeners():
            if isinstance(listener, ErrorListener):
                listener.syntaxError(recognizer, offending_symbol, line, char_position_in_line, msg, e)

    def reportAmbiguity(self, recognizer, dfa, start_index, stop_index, exact, ambig_alts, configs):
        for listener in self._parent.getErrorListeners():
            if isinstance(listener, ErrorListener):
                listener.reportAmbiguity(recognizer, dfa, start_index, stop_index, exact, ambig_alts, configs)

    def reportAttemptingFullContext(self, recognizer, dfa, start_index, stop_index, conflicting_alts, configs):
        for listener in self._parent.getErrorListeners():
            if isinstance(listener, ErrorListener):
                listener.reportAttemptingFullContext(recognizer, dfa,
                                                     start_index, stop_index, conflicting_alts, configs)

    def reportContextSensitivity(self, recognizer, dfa, start_index, stop_index, prediction, configs):
        for listener in self._parent.getErrorListeners():
            if isinstance(listener, ErrorListener):
                listener.reportContextSensitivity(recognizer, dfa, start_index, stop_index, prediction, configs)
