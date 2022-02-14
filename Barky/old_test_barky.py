## using Pytest to test the barky.py module

from asyncio.windows_events import NULL
import os, commands, barky, pytest
from random import choice



# test the ProductTestCase Class
class Test_ProductTestCase():
    def test_working(self):
        pass

def test_clear_screen():
    clear = "cls" if os.name == "nt" else "clear"
    assert clear == 'cls'
    
def test_get_user_input(monkeypatch):
    uInput = 'Title'
    monkeypatch.setattr('sys.stdin', uInput)
    assert barky.get_user_input() == 'A'



