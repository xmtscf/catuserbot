# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# CatUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by TgCatUB@Github.

# This file is part of: https://github.com/xmtscf/catuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/xmtscf/catuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

from sqlalchemy import Column, Numeric

from . import BASE, SESSION


class NOLogPMs(BASE):
    __tablename__ = "no_log_pms"
    chat_id = Column(Numeric, primary_key=True)

    def __init__(self, chat_id, reason=""):
        self.chat_id = chat_id


NOLogPMs.__table__.create(checkfirst=True)


def is_approved(chat_id):
    try:
        return SESSION.query(NOLogPMs).filter(NOLogPMs.chat_id == chat_id).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def approve(chat_id):
    adder = NOLogPMs(chat_id)
    SESSION.add(adder)
    SESSION.commit()


def disapprove(chat_id):
    if rem := SESSION.query(NOLogPMs).get(chat_id):
        SESSION.delete(rem)
        SESSION.commit()
