from aiogram import types
from db.db_connector import Database
import const.phrases as phrases
from const.const import *
from . import markups


class Controller:
    def __init__(self):
        self.db = Database()

    async def command_start(self, message):
        id = message.from_user.id
        name = message.from_user.first_name
        username = message.from_user.username
        user = self.db.get_user(tg_id=id)

        if not user:
            self.db.save_user(
                tg_id=id,
                tg_name=name,
                tg_username=username
            )
            text = phrases.phrase_for_start_first_greeting(
                data=dict(
                    user_name=name
                )
            )
        else:
            text = phrases.phrase_for_start_regular_greeting(
                data=dict(
                    user_name=name
                )
            )

        markup = markups.user_main_markup()
        return dict(text=text, markup=markup)

    async def message_main_menu_buttons_click(self, message):
        text = phrases.phrase_for_answer_to_main_menu_buttons(
            data=dict(
                button_title=message.text
            )
        )
        return dict(text=text)
