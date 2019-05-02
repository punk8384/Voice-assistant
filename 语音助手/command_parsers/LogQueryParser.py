from 语音助手.command_parsers.IParser import IParser


class LogQueryParser(IParser):

    def __init__(self, text):
        self.__text = text

    def getName(self):
        return 'log'

    def isSatisfied(self):
        if '日志' in self.__text and '查' in self.__text:
            return True

        return False

    def confirmAction(self):
        return '查看日志'

    def doAction(self):
        print('<<querying log>>')