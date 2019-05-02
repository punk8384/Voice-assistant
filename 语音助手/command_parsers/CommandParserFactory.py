from 语音助手.command_parsers.LEDParser import LEDParser
from 语音助手.command_parsers.LogQueryParser import LogQueryParser
from 语音助手.command_parsers.NullParser import NullParser

class CommandParserFactory:

    def __init__(self, text):
        self.parsers = []

        parser = LEDParser(text)
        self.parsers.append(parser)

        parser = LogQueryParser(text)
        self.parsers.append(parser)

        parser = NullParser(text)
        self.parsers.append(parser)

    def getParsers(self):

        return self.parsers