from 语音助手.command_parsers.CommandParserFactory import CommandParserFactory
from 语音助手.ASR.ASRService import ASRService


asrService = ASRService()


def parseCommand(text):
    factory= CommandParserFactory(text)
    parsers=factory.getParsers()
    selected_parser = None
    for parser in parsers:
        if parser.isSatisfied():
            selected_parser = parser
            break

    return selected_parser


def confirmCommand(parser):
    asrService.say('请确认 '+parser.confirmAction())
    user_response = asrService.get_user_voice_and_convert2text('---confirm---')
    if user_response in ['是','确定','确认','对','对的','好','好的']:
        return 'OK'

    return 'STOP'


def sayDone():
    asrService.say('已完成')


def sayCancelled():
    asrService.say('指令未识别，已取消')


while True:
    text = asrService.get_user_voice_and_convert2text('---session---')
    cmd = parseCommand(text)

    if cmd.getName() == 'Null':
        print('未识别处理器...')
        continue

    response = confirmCommand(cmd)
    if response == "OK":
        cmd.doAction()
        sayDone()
    else:
        sayCancelled()