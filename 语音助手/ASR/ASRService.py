from aip import AipSpeech
import speech_recognition as sr
import pygame
import os
import time

APP_ID = '15892841'
API_KEY = 'T509tEyGrlgbPQW40WZaZGvy'
SECRET_KEY = 'GwehcW0qc9zl4EHOqXEr8lKYbuS66Adg'
WAV_NAME = 'recording.wav'
DIR = 'temp'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
pygame.mixer.init()


class ASRService:

    def __rec(self, rate=16000):
        r = sr.Recognizer()
        with sr.Microphone(sample_rate=rate) as source:
            print("请说：")
            audio = r.listen(source)

        with open(DIR+'/'+WAV_NAME, "wb") as f:
            f.write(audio.get_wav_data())

    def __convert_asr(self):
        with open(DIR+'/'+WAV_NAME, 'rb') as f:
            audio_data = f.read()

        result = client.asr(audio_data, 'wav', 16000, {
            'dev_pid': 1536,
        })

        result_text = result["result"][0]

        print("您说: " + result_text)

        return result_text

    def get_user_voice_and_convert2text(self, prefix_debug):
        self.wait_audio_done()

        while True:
            try:
                print(prefix_debug)
                self.__rec()
                return self.__convert_asr()
            except Exception as ex:
                print(prefix_debug, 'something wrong')
                print(prefix_debug, ex)
                pass

    def say(self, str):
        fileName = str+'-audio.mp3'
        if os.path.exists(DIR+'/'+fileName):
            self.__play_until_done(DIR+'/'+fileName)
            return

        result = client.synthesis(
            str,  # text:合成的文本,使用UTF-8编码,请注意文本长度必须小于1024字节
            'zh',  # lang:语言,中文:zh,英文:en
            1,  # ctp:客户端信息这里就写1,写别的不好使,至于为什么咱们以后再解释
            {
                'vol': 5,  # 合成音频文件的准音量
                'spd': 4,  # 语速取值0-9,默认为5中语速
                'pit': 8,  # 语调音量,取值0-9,默认为5中语调
                'per': 1  # 发音人选择,0为女声,1为男生,3为情感合成-度逍遥,4为情感合成-度丫丫,默认为普通女
            }  # options:这是一个dict类型的参数,里面的键值对才是关键.
        )

        if not isinstance(result, dict):
            with open(DIR+'/'+fileName, 'wb') as f:
                f.write(result)

        self.__play_until_done(DIR+'/'+fileName)

    def __play_until_done(self, fileName):
        pygame.mixer.music.load(fileName)
        pygame.mixer.music.play()

        time.sleep(0.5)
        self.wait_audio_done()


    def wait_audio_done(self):
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)