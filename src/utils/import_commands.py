import importlib


def import_commands() -> None:
    importlib.import_module("src.factorial.factorial_command")
