from config import Config

import colorama
import datetime
import pyttsx3


colorama.init()
engine = pyttsx3.init()


class Console:
    @staticmethod
    def TTS(command):
        engine.say(command)
        engine.runAndWait()
        
    @staticmethod
    def Log(text: str, warning: bool = False):
        message = "[*]" if not warning else "[!]"

        if Config.DisplayTime:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            message += f"({colorama.Fore.CYAN}{time}{colorama.Fore.RESET})"

        print(message, text)