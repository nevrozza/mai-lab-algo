import importlib


def import_commands() -> None:
    importlib.import_module("src.factorial.factorial_command")
    importlib.import_module("src.fibo.fibo_command")
