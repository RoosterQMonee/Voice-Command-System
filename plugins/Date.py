import plugins

import datetime


class DatePlugin(plugins.Base):
    def __init__(self):
        self.command = "date"
        self.aliases = ["date now", "current date", "date right now", "date today"]

    def process(self, text):
        return "Today is: " + datetime.datetime.today().strftime("%B %d, %Y")