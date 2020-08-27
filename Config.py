import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
  else:
    BOT_TOKEN = "1350548924:AAHIH92qD6u5vDY25hFxcdXo9qdRCP6IzOE"
    DATABASE_URL = "mongodb+srv://sachink4s:sachink4s@cluster0.stwrx.mongodb.net/cluster0?retryWrites=true&w=majority"
    APP_ID = "1001799"
    API_HASH = "7e72902823d3ffa3ed58e36b1d24687d"


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe by SK4S**\n\nForce group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.",
        
        "**Setup**\nFirst of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.",
        
        "**Commmands**\n__/ForceSubscribe__ - To get the current settings.\n__/ForceSubscribe no/off/disable__ - To turn of ForceSubscribe.\n__/ForceSubscribe {channel username}__ - To turn on and setup the channel.\n__/ForceSubscribe clear__ - To unmute all members who muted by me__.\n\n*Note:* /FSub is an alias of /ForceSubscribe",
        
        "**Developed by @SACHINK4S**"
      ]

      START_MSG = "**Hey [{}](tg://user?id={})**\nI can force members to join a specific channel before writing messages in the group.\nLearn more at /help"
