from src.cli.terminal import Terminal
from src.utils.import_commands import import_commands


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    import_commands()
    terminal = Terminal()
    terminal.cycle_input()


if __name__ == "__main__":
    main()
