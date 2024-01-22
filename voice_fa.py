from gtts import gTTS
import os


def voice(txt):
    tts = gTTS(txt, lang='ar')
    tts.save("output.mp3")
    #os.system("start output.mp3")  # برای پخش فایل صوتی در سیستم عامل ویندوز
