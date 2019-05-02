
class IParser:

    def __init__(self):
        self.__text = None

    def getName(self):
        pass

    def setText(self, text):
        self.__text = text

    def isSatisfied(self):
        pass

    def confirmAction(self):
        pass

    def doAction(self):
        pass