from 语音助手.command_parsers.IParser import IParser


class LEDParser(IParser):

    def __init__(self, text):
        self.__text = text

    def getName(self):
        return 'led'

    def isSatisfied(self):
        if '灯' in self.__text:
            return True

        return False

    def confirmAction(self):
        return '开灯或关灯'

    def doAction(self):
        print('<<开关灯操作>>')