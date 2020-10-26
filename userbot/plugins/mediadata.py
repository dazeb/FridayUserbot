# Originally By @DeletedUser420
# Ported - @StarkxD

import asyncio
import os
import time
from datetime import datetime
from userbot.uniborgConfig import Config
from userbot.utils import friday_on_cmd, sudo_cmd
import subprocess
import os
import re
import html 
import shlex
import asyncio
from os.path import basename
from typing import Tuple, List, Optional
from telegraph import Telegraph, exceptions, upload_file
telegraph = Telegraph()
tgnoob = telegraph.create_account(short_name="Friday 🇮🇳")

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """ run command in terminal """
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(*args,
                                                   stdout=asyncio.subprocess.PIPE,
                                                   stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    return (stdout.decode('utf-8', 'replace').strip(),
            stderr.decode('utf-8', 'replace').strip(),
            process.returncode,
            process.pid)

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
    output = await runcmd(f"mediainfo '{file_path}'")
    sedput = f"{output}"
    media_info = f"""<b> 🔔 MediaInfo </b> 
    <code> {sedput} </code>"""
    title_of_page = "MediaInfoByFridayUserbot"
    response = telegraph.create_page(title_of_page, html_content=media_info)
    km = response["path"]
    await event.edit(f"**MediaInfo** https://telegra.ph/{km}")
    if os.path.exists(file_path):
            os.remove(file_path)
