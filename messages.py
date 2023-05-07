"""
In messages.py all bot's messages are stored and can be edited. You can also use html tags here.
"""

from config import *

start_msg = f"""
<b>Hello! Send us news you've got, we will check them and post to our chanel!</b>

Send here news, one message - one event, minimal amount of symbols is <b>{min_symbols}</b> and maximum is <b>{max_symbols}</b>!

You can also add some <b>attechments</b>! IMPORTANT: 1) Add all attachments to 1 message! 2) Attachments must be added as files!

And remember, we collect such data as your telegram id and you agree with it if you use this bot!

/start to start a bot
/checkadmin to check if you are an admin
/checkid to get your tg id
"""

admin_msg = """
Congrats! You <b>are</b> an admin!
"""

not_admin_msg = """
Unfortunately, you <b>are not</b> an admin!
"""

too_short_news_msg = """
Sorry, your news too <b>short</b>! You need make it longer for <b>
"""

too_long_news_msg = """
Sorry, your news too <b>long</b>! You need make it shorter for <b>
"""

news_sent_msg = """
You news <b>successfully</b> sent to admins! They will check it and post to chanel!
"""

devider = "----------END/START----------END/START----------END/START----------"