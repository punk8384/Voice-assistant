from 语音助手.command_parsers.IParser import IParser


class NullParser(IParser):

    def __init__(self, text):
        self.__text = text

    def getName(self):
        return 'Null'

    def isSatisfied(self):
        return True

    def confirmAction(self):
        return ''

    def doAction(self):
        print('no action')
        pass