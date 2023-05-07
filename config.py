"""
Config file, all preferences can be edited.
"""

image_folder = "images/" # Image folder if needed
logs_folder = "logs/" # Logs folder

bot = { # All bot data (register it using https://t.me/BotFather)
	"show_name": "",
	"usernname": "",
	"token": "",
    "discription": """  News bot manager and checker.

                        Send news and we will check and post them!

                        You can also add any attachments (important to add in same message)!

                        /start to start and follow the instructions!""",
    "about": "News bot manager and checker. Send news and we will check and post them!",
}
commands = { # All available commands, it's just a list and changing it will cause nothing
    "start": "/start",
    "check_id": "/checkid",
    "check_admin": "/checkadmin",
}
admin_users = { # Admin users, "@admin_nick": telegram_id,
    "": 0,
}


min_symbols = 100
max_symbols = 1000