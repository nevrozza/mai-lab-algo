import importlib


def import_commands() -> None:
    # TODO
    importlib.import_module("src.factorial.factorial_command")
    importlib.import_module("src.fibo.fibo_command")
    importlib.import_module("src.sorts.bubble")
    importlib.import_module("src.sorts.quick")
