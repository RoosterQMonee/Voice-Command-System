import plugins

import random


class YoutubePlugin(plugins.Base):
    def __init__(self):
        self.command = "thanks"
        self.aliases = ["thank you"]

    def process(self, text):
        return random.choice(["No problem!", "You're welcome"])