# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# CatUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by TgCatUB@Github.

# This file is part of: https://github.com/xmtscf/catuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/xmtscf/catuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

from sqlalchemy import Column, String

from . import BASE, SESSION


class GBan(BASE):
    __tablename__ = "gban"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(String(127))

    def __init__(self, chat_id, reason=""):
        self.chat_id = chat_id
        self.reason = reason


GBan.__table__.create(checkfirst=True)


def is_gbanned(chat_id):
    try:
        return SESSION.query(GBan).filter(GBan.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_gbanuser(chat_id):
    try:
        return SESSION.query(GBan).get(str(chat_id))
    finally:
        SESSION.close()


def catgban(chat_id, reason):
    adder = GBan(str(chat_id), str(reason))
    SESSION.add(adder)
    SESSION.commit()


def catungban(chat_id):
    if rem := SESSION.query(GBan).get(str(chat_id)):
        SESSION.delete(rem)
        SESSION.commit()


def get_all_gbanned():
    rem = SESSION.query(GBan).all()
    SESSION.close()
    return rem
