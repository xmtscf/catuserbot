# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# CatUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by TgCatUB@Github.

# This file is part of: https://github.com/xmtscf/catuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/xmtscf/catuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

from sqlalchemy import Column, Numeric, UnicodeText

from . import BASE, SESSION


class Note(BASE):
    __tablename__ = "catsnip"
    keyword = Column(UnicodeText, primary_key=True, nullable=False)
    reply = Column(UnicodeText)
    f_mesg_id = Column(Numeric)

    def __init__(self, keyword, reply, f_mesg_id):
        self.keyword = keyword
        self.reply = reply
        self.f_mesg_id = f_mesg_id


Note.__table__.create(checkfirst=True)


def get_note(keyword):
    try:
        return SESSION.query(Note).get(keyword)
    finally:
        SESSION.close()


def get_notes():
    try:
        return SESSION.query(Note).all()
    finally:
        SESSION.close()


def add_note(keyword, reply, f_mesg_id):
    to_check = get_note(keyword)
    if not to_check:
        adder = Note(keyword, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    rem = SESSION.query(Note).get(keyword)
    SESSION.delete(rem)
    SESSION.commit()
    adder = Note(keyword, reply, f_mesg_id)
    SESSION.add(adder)
    SESSION.commit()
    return False


def rm_note(keyword):
    to_check = get_note(keyword)
    if not to_check:
        return False
    rem = SESSION.query(Note).get(keyword)
    SESSION.delete(rem)
    SESSION.commit()
    return True
