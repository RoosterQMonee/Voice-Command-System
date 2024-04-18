import plugins

import datetime


class TimePlugin(plugins.Base):
    def __init__(self):
        self.command = "time"
        self.aliases = ["time now", "current time", "time right now"]

    def process(self, text):
        return "The current time is: " + datetime.datetime.now().strftime("%H:%M")