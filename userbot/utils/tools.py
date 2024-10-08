# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# CatUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by TgCatUB@Github.

# This file is part of: https://github.com/xmtscf/catuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/xmtscf/catuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

from telethon.tl import functions


async def create_supergroup(group_name, client, botusername, descript):
    try:
        result = await client(
            functions.channels.CreateChannelRequest(
                title=group_name,
                about=descript,
                megagroup=True,
            )
        )
        created_chat_id = result.chats[0].id
        result = await client(
            functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            )
        )
        await client(
            functions.channels.InviteToChannelRequest(
                channel=created_chat_id,
                users=[botusername],
            )
        )
    except Exception as e:
        return "error", str(e)
    if not str(created_chat_id).startswith("-100"):
        created_chat_id = int(f"-100{str(created_chat_id)}")
    return result, created_chat_id
