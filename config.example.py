# General
TOKEN: str = ""  # discord bot token
PREFIX: str = "!"
MEMBER_ROLE: str = "member"
MUTE_ROLE: str = "muted"

# Paste
PASTE_API_KEY: str = ""  # paste.gg | register & create API key

# LOGGING
LOGS_CHANNEL_ID: int = 000000  # discord ID of logs channel
MOD_LOGS_CHANNEL_ID: int = 000000  # discord ID of mod logs channel

# Other
LOGO: str = "https://i.imgur.com/8mKjoAA.png"  # Logo URL
MOD_LOGS_CHANNEL_ID: int = 000000  # discord ID of verify-here

# DB (postgresql)

DATABASE = "MCsniperBOT"  # DB name
HOST = "localhost"
PORT = "5432"
USER = ""
PASSWORD = ""
SSLMODE = "allow"


RULES = {
    "a": "dont be rude"
}


# EXAMPLE | CHANGE THIS FOR ACTUAL USE
MOD_RULES = [
    {
        "l": lambda c: "mean" in c.lower(),
        "m": "calling someone mean is rude :("
    }
]
