# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# CatUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by TgCatUB@Github.

# This file is part of: https://github.com/xmtscf/catuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/xmtscf/catuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import requests
from bs4 import BeautifulSoup

from userbot import catub

from ..core.managers import edit_or_reply

plugin_category = "utils"


@catub.cat_cmd(
    pattern="filext(?:\s|$)([\s\S]*)",
    command=("filext", plugin_category),
    info={
        "header": "Shows you the detailed information of given extension type.",
        "usage": "{tr}filext <extension>",
        "examples": "{tr}filext py",
    },
)
async def _(event):
    "Shows you the detailed information of given extension type."
    sample_url = "https://www.fileext.com/file-extension/{}.html"
    input_str = event.pattern_match.group(1).lower()
    response_api = requests.get(sample_url.format(input_str))
    status_code = response_api.status_code
    if status_code == 200:
        raw_html = response_api.content
        soup = BeautifulSoup(raw_html, "html.parser")
        ext_details = soup.find_all("td", {"colspan": "3"})[-1].text
        await edit_or_reply(
            event,
            f"**File Extension**: `{input_str}`\n**Description**: `{ext_details}`",
        )
    else:
        await edit_or_reply(
            event,
            f"https://www.fileext.com/ responded with {status_code} for query: {input_str}",
        )
