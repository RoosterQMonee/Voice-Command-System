import plugins

import wikipedia


class WikipediaPlugin(plugins.Base):
    def __init__(self):
        self.command = "wikipedia"
        self.aliases = ["search", "who is"]

    def process(self, text):
        info = wikipedia.summary(text, 1)

        return "Here's what i found... " + info