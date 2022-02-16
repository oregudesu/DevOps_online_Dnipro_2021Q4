import unittest
import os
import sys

from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, os.getcwd())
from logic.controller import Controller
from logic.utils import Dict
from db.db_connector import Database


class TestTelegramBot(unittest.IsolatedAsyncioTestCase):
    async def test_command_start(self):
        controller = Controller()
        test_data = Dict(
            message_id=13,
            from_user=Dict(
                id=1,
                is_bot=False,
                first_name="test_name",
                username="test_username",
                language_code="en"
            ),
            chat=Dict(
                id=1,
                first_name="test_name",
                username="test_username",
                type="private"
            ),
            date=1644846697,
            text="/start",
            entities=[
                Dict(
                    type="bot_command",
                    offset=0,
                    length=6
                )
            ]
        )
        result = await controller.command_start(message=test_data)
        expected_result = "Hello, test_name!"
        self.assertEqual(result["text"], expected_result)

    async def test_command_start_second_case(self):
        controller = Controller()
        test_data = Dict(
            message_id=13,
            from_user=Dict(
                id=1,
                is_bot=False,
                first_name="test_name",
                username="test_username",
                language_code="en"
            ),
            chat=Dict(
                id=1,
                first_name="test_name",
                username="test_username",
                type="private"
            ),
            date=1644846697,
            text="/start",
            entities=[
                Dict(
                    type="bot_command",
                    offset=0,
                    length=6
                )
            ]
        )
        result = await controller.command_start(message=test_data)
        expected_result = "Hello again, test_name! It's good to see ya back!"
        self.assertEqual(result["text"], expected_result)
        # remove test data from db
        db = Database()
        db.remove_user(tg_id=1)


if __name__ == "__main__":
    unittest.main()
