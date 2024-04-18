from console import *
import plugins

import speech_recognition as sr
import traceback
import random
import time
import os


recognizer = sr.Recognizer()
last_command = time.time()


def main():
    global last_command

    # Load Plugins

    path = os.path.abspath(__name__)
    dirpath = os.path.join(os.path.dirname(path), Config.PluginsDirectory)

    Console.Log("Loading Plugins...", True)

    for fname in os.listdir(dirpath):
        if not fname.startswith('.') and not fname.startswith('__') and fname.endswith('.py'):
            try:
                Console.Log(f"{colorama.Fore.GREEN}>{colorama.Fore.RESET} Loading: {fname}") # not the best looking lmao
                plugins.load_module(os.path.join(dirpath, fname))

            except Exception:
                traceback.print_exc()

    # Begin Audio
                
    Console.Log("Starting Assistant!", True)

    while(1):
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=Config.AudioAdjustTime)

                audio = recognizer.listen(source)

                text = recognizer.recognize_google(audio)
                text = text.lower()
    
                Console.Log("Heard: " + text)

                if (Config.AssistantPrefix in text) or (time.time() - last_command < Config.CommandChainTime):
                    last_command = time.time()
                    text = text.replace(Config.AssistantPrefix, "")
                    found = False

                    for plug in plugins.Base.plugins:
                        if found:
                            break

                        inst = plug()

                        if inst.command in text:
                            result = inst.process(text)
                            found = True

                            Console.Log(f"({inst.command}) {result}")
                            Console.TTS(result)

                            break

                        for ail in inst.aliases:
                            if ail in text:
                                found = True
                                result = inst.process(text)

                                Console.Log(f"({inst.command}) {result}")
                                Console.TTS(result)

                                break

                    if (not found) and (Config.AssistantPrefix in text):
                        Console.Log("Unknown command!")
                        Console.TTS(random.choice(Config.DefaultGreetings)) # you can change this if you want


        except sr.exceptions.UnknownValueError as e:
            Console.Log("Cannot detect speech: " + e, True) # note: this can be triggered by no audio
        
        except sr.RequestError as e:
            Console.Log("Service Error occured, quitting...")
            Console.Log(e, True)
            quit(1)

        except KeyboardInterrupt as e:
            Console.Log("(Ctrl+C) Stopping Assistant...")
            quit(1)


if __name__ == "__main__":
    main()
