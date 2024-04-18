class Config:
    HostName: str = "Nami" # your name (you pick)
    AssistantPrefix: str = "helper" # what to respond to (e.g "alexa")
    PluginsDirectory: str = "Plugins"

    DisplayTime: bool = True # log time

    AudioAdjustTime: float = 0.5 # how long to test surrounding audio for
    CommandChainTime: float = 15.0 # how long to wait until forgetting coversation

    DefaultGreetings = ["How can i help?", "Hello, " + HostName, "Hello there!"]

    class APIs:
        OpenWeatherMapAPI: str = "API-KEY"