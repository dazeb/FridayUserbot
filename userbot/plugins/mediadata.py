import asyncio
import os
import time
from datetime import datetime
from userbot.uniborgConfig import Config
from userbot.utils import friday_on_cmd, sudo_cmd
import subprocess
from telegraph import Telegraph, exceptions, upload_file
telegraph = Telegraph()
tgnoob = telegraph.create_account(short_name="Friday 🇮🇳")
@friday.on(friday_on_cmd(pattern="mediainfo$"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if reply_message is None:
        await event.edit(
            "Reply To a Media."
        )
    file_path = await borg.download_media(reply_message, Config.TMP_DOWNLOAD_DIRECTORY)
    proc = subprocess.Popen(["mediainfo '{file_path}'"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    media_info = f"<b> MediaInfo </b> \n"
    media_info += f"<code>{out}</code>"
    title_of_page = "MediaInfoByFridayUserbot"
    response = telegraph.create_page(title_of_page, html_content=media_info)
    km = response["path"]
    await event.edit(f"**MediaInfo** https://telegra.ph/{km}")
    if os.path.exists(file_path):
            os.remove(file_path)
