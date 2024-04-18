import plugins

from youtubesearchpython import VideosSearch
import pywhatkit
import random


class YoutubePlugin(plugins.Base):
    def __init__(self):
        self.command = "youtube"
        self.aliases = ["play", "watch", "turn on"]

    def process(self, text):
        cleaned = text.replace("turn on", "")

        customSearch = VideosSearch(cleaned, limit = 5)
        name = random.choice(customSearch.result()['result'])['title']

        pywhatkit.playonyt(name)

        return "Now playing: " + name