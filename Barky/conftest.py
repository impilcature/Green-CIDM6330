import pytest

from barky import Option, commands, get_bookmark_id_for_deletion, get_github_import_options, get_new_bookmark_info

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