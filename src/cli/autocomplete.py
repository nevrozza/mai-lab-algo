import readline

from src.cli.command import BashCommand


class Autocomplete:
    """Автодополнение команд и путей при вводе в терминале"""

    # I f****d this API
    # TODO: add support for files started/ended with commas

    _current_suggestions: list[str]

    cur_dir = ""

    @classmethod
    def enable(cls):
        """Включает автодополнение по нажатию Tab, инициализирует класс"""
        readline.parse_and_bind('tab: complete')
        readline.parse_and_bind('bind ^I rl_complete')  # MacOS...
        readline.set_completer_delims('/ ;')  # По умолчанию там есть другие знаки (!~*...)

        readline.set_completer(cls._autocompleter)

        cls._current_suggestions = []

        # Чуток пояснений (почему пришлось костылять):
        # В Ubuntu (или в терминале MacOS) в ситуации где у нас есть 2 файла в директории [p1, p2],
        # и мы вводим команду (например catman), но с автокомплитом:
        # 'catma' -> 'catman ' -> 'catman p' -> 'catman p'+подсказки
        # Т.е. Подсказки выводятся после второго таба,
        # но что важно: отсчёт табов начинается после `развилки`
        #
        # В текущей реализации программы это не так, а вот так:
        # 'catma' -> 'catman ' -> 'catman p'+подсказки
        # Причём: 'catman ' -> 'catman p' -> 'catman p'+подсказки (нет единообразия((
        # Т.е. отсчёт табов введёт себя по-другому(
        #
        # Можно было бы написать свою реализацию вывода подсказок, но, к сожалению,
        # Из-за особенностей MacOS функция (ниже), которая позволяет это сделать, игнорится =)))
        # https://github.com/oils-for-unix/oils/pull/235
        # readline.set_completion_display_matches_hook()
        #
        # Double `Tab` workaround:
        # readline.get_completion_type() -> 63 # ord("?") if doubleTab
        # readline.get_completion_type() -> 9 # ord("\t") if singleTab
        # print(readline.get_completion_type())

    @staticmethod
    def _get_completion_word(line: str) -> tuple[bool, str]:
        """
        Определяет, находится ли курсор в позиции команды или аргумента, и возвращает текущее слово для дополнения

        :return: `tuple[bool, str]` – (редачим команду?; слово, которое дополняем)
        """
        line = line.lstrip()

        # parenthesis_stack: list[str] = [] not yet implemented =/

        opened_double_quote = None
        opened_single_quote = None
        space = 0

        is_command = True
        is_command_entered = False

        words: list[str] = []

        # TODO: refactor
        for index, char in enumerate(line):
            if char != ' ':
                is_command_entered = True

            if char == "'":
                if opened_single_quote:
                    words.append(line[opened_single_quote:index])
                    opened_single_quote = None
                else:
                    opened_single_quote = index
            elif char == '"':
                if opened_double_quote:
                    words.append(line[opened_double_quote:index])
                    opened_double_quote = None
                else:
                    opened_double_quote = index
            elif char == '\\' and not opened_double_quote and not opened_single_quote:
                if (index + 1 < len(line)) and line[index + 1] == ' ':
                    opened_single_quote = space
            elif char == ' ':
                if is_command_entered:
                    is_command = False

                if space == 0:
                    words.append(line[space:index])
                    space = index
                elif not opened_double_quote and not opened_single_quote:
                    words.append(line[space:index])
                    space = index
            elif char == ';' and not opened_single_quote and not opened_double_quote:
                is_command = True
                is_command_entered = False
                words = []
                space = index + 1
        end_el = line[space:].lstrip()
        if end_el == ";":
            end_el = ""
        words.append(end_el)
        return is_command, words[-1]

    @classmethod
    def _autocompleter(cls, completion_scope: str, state: int) -> str | None:
        """
        !!! Используется для `readline.set_completer` !!!

        :param completion_scope: Кусок текста, который мы сейчас дополняем (со стороны автокомплита)
        :param state: Итерация прохода по suggestions
        :return: Одно из предложений или None
        """

        # Эта функция вызывается после нажатия `Tab` до тех пор, пока не получит None
        # Иначе происходит инкремент state
        # Поэтому делаем проверку state == 0
        if not state:

            # Текст, который мы сейчас дополняем. Включая те слова, которые не входят в completion_scope
            line = readline.get_line_buffer()[:readline.get_endidx()]
            is_command, being_completed = cls._get_completion_word(line)
            # elif '\\' in being_completed:
            #     quoting_type = QuotingType.ESCAPING_TYPE
            # else:
            #     quoting_type = QuotingType.SINGLE_QUOTE

            if is_command:
                # Предлагаем команды
                suggestions = [cmd for cmd in BashCommand.get_all_commands()
                               if cmd.startswith(being_completed)]
                cls._current_suggestions = suggestions

            else:
                # Предлагаем содержимое директории
                cls._current_suggestions = []

        if state < len(cls._current_suggestions):
            if len(cls._current_suggestions) == 1:
                return cls._current_suggestions[0]
            return cls._current_suggestions[state]
        else:
            return None
