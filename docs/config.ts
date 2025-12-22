//https://github.com/sennett-lau/readme-project-structure-generator.git
export const projectStructure = {

        src: {
            benchmarking: {
                "benchmark.py": "Функции: `timeit_once` и `benchmark_sorts`",
                "generators.py": "Генераторы рандомных списков с числами",
                "run_benchmark.py": "Запуск бенчмарков, описание сценариев",
            },
            "cli": "CLI из лр2 (вырезана работа с файлами)",
            "formulas": "Факториал и Фибоначчи",
            "sorts": "Директория с реализациями сортировок (+ команды)",
            structures:{
                'queue_on_stacks.py': 'Очередь на стеках',
            },
            utils: {
                'commands_abc.py': 'Дефолтные команды для этого проекта',
                'consts.py': 'Константы (строки с ошибками)',
                '...': ''
            },
            'main.py': 'Входная точка в программу',
        },
        'tests': 'Тесты сортировок, факториала и Фибоначчи, структуры'


}
