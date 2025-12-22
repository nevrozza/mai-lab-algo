from colorama import init, Fore

from src.cli.errors import BashSyntaxError, BashError
from src.cli.autocomplete import Autocomplete
from src.cli.command import BashCommand
from src.cli.get_command_raw_params import get_command_raw_params


# https://docs-python.ru/standart-library/modul-readline-python/
class Terminal:
    """Основной цикл терминала: обработка ввода, разбор и выполнение команд, логгирование"""

    def __init__(self):
        # Enable autocomplete
        Autocomplete.enable()

    def cycle_input(self):
        """Бесконечный цикл ввода команд"""
        init()  # Colorama

        print("=== Double `Tab` to show all commands ===")
        while True:
            try:
                input_line = input(
                    f"{Fore.LIGHTBLUE_EX}>>>{Fore.RESET} "
                )
                commands = self._parse_commands(input_line)
                self._execute_commands(commands)
            except KeyboardInterrupt:
                print("\nBye!")
                break
            except Exception as e:  # meow
                print(e)

    @staticmethod
    def _execute_commands(commands: list[BashCommand]):
        """Выполняет список команд, логгирует и добавляет их в историю"""
        for command in commands:
            try:
                not_critical_validation_errors, (not_critical_exec_errors, output) = command.execute()
                not_critical_errors = (not_critical_validation_errors or []) + (not_critical_exec_errors or [])
                if not_critical_errors:
                    for error in not_critical_errors:
                        print(error)
                output and print(output)
            except BashError as output:
                print(output)

    @classmethod
    def _parse_commands(cls, input_line: str) -> list[BashCommand]:
        """Разбирает строку ввода на отдельные команды (разделённые ';'),
        парсит `сырые` параметры (вместе с флагами). Возвращает список BashCommand
        :return: list[BashCommand] – список команд"""
        commands: list[BashCommand] = []
        try:
            for command_line in input_line.split(";"):
                if command_line.strip():
                    name, raw_params = get_command_raw_params(command_line)
                    try:
                        bash_command = BashCommand.get_command(name)
                        commands.append(bash_command(raw_params, command_line))
                    except KeyError:
                        print(f"'{name}' command not found")
        except BashSyntaxError as e:
            print(e)
        return commands
