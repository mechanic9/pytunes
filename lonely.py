''' Singleton Helper '''

class Singleton:
    #Helper class for implementing singletons.

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        #Returns old singleton instance or creates new one of first call.
        try:
            return self._instance

        except AttributeError: #if first call
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.') #Restricts singleton initialization

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)