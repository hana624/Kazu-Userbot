from telethon import Button
from AyiinXd import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    STRING_SESSION,
    blacklistayiin,
    bot,
    tgbot,
)

async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/bb72f6bd45a8f23dcdae5.jpg",
                caption="ᴅᴀʏ ᴜsᴇʀʙᴏᴛ.\n     **status : Active\n     ketik `.ping` untuk cek bot!**",
                buttons=[(Button.url("Channel", "https://t.me/day_support")),
                         (Button.url("Support", "https://t.me/lpmdayy"))]
            )
    except Exception as e:
        LOGS.error(e)
        return None
