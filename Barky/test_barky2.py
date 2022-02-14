## using Pytest to test the barky.py module while using the -s switch for user input
import os, commands, barky, pytest, conftest

from numpy import require
from barky import (
    Option,
    get_bookmark_id_for_deletion,
    get_github_import_options,
    get_new_bookmark_info,
    get_user_input,
)


@pytest.fixture
def label():
    label = "Title: "
    return label

@pytest.fixture()
def bookmark():
    bookmark = {        
        "id": 1,
        "title": "first bookmark",
        "url": "www.1stbm.com",
        "notes": "notes for 1 bm",
        "date_added": "today"
        }
    return bookmark 

@pytest.fixture()
def options():
    options = {
        "A": Option(
            "Add a bookmark",
            commands.AddBookmarkCommand(),
            prep_call=get_new_bookmark_info,
        ),
        "B": Option("List bookmarks by date", commands.ListBookmarksCommand()),
        "T": Option(
            "List bookmarks by title", commands.ListBookmarksCommand(order_by="title")
        ),
        "E": Option(
            "Edit a bookmark",
            commands.EditBookmarkCommand(),
            prep_call=get_new_bookmark_info,
        ),
        "D": Option(
            "Delete a bookmark",
            commands.DeleteBookmarkCommand(),
            prep_call=get_bookmark_id_for_deletion,
        ),
        "G": Option(
            "Import GitHub stars",
            commands.ImportGitHubStarsCommand(),
            prep_call=get_github_import_options,
        ),
        "Q": Option("Quit", commands.QuitCommand()),
    }
    return options


# test the ProductTestCase Class
class Test_ProductTestCase:
    def test_working(self):
        pass

# begin function testing
def test_clear_screen():
    clear = "cls" if os.name == "nt" else "clear"
    assert clear == "cls"


@pytest.mark.skip(
    reason="i don't understand how to input the options to the test and then store the output sdtout in a variable to compare"
)
def test_get_user_input(capfd, options):
    out, err = capfd.readouterr(barky.print_options(options))
    # output = barky.print_options(options)
    outOptions = str(options)
    print(outOptions)
    assert out == outOptions


@pytest.mark.skip(
    reason="i don't understand how to input the options to the sys test and then store the output sdtout in a variable to compare"
)
def test_get_user_input(label):
    value = input(f"{label}: ") or None
    while require and not value:
        value = input(f"{label}: ") or None
    return value


def test_get_bookmark_id_for_deletion(capfd,bookmark):
    get_user_input("Enter a bookmark ID to delete")
    choiceSelected = capfd.readouterr()
    assert choiceSelected == bookmark.get("id")


"""
    def get_github_import_options():
    return {
        "github_username": get_user_input("GitHub username"),
        "preserve_timestamps": get_user_input(
            "Preserve timestamps [Y/n]", required=False
        )
        in {"Y", "y", None},
    }
"""

"""
def get_new_bookmark_info():
    bookmark_id = get_user_input("Enter a bookmark ID to edit")
    field = get_user_input("Choose a value to edit (title, URL, notes)")
    new_value = get_user_input(f"Enter the new value for {field}")
    return {
        "id": bookmark_id,
        "update": {field: new_value},
"""
