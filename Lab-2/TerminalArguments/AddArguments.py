import argparse


def add_arguments() -> None:
    """
    Функция добавляет к программе возможность использования аргументов командной строки.
    :rtype: None
    """
    parser = argparse.ArgumentParser(description="Аргументы командной строки для работы с программой "
                                                 "сериализации/ десериализации")


    #невзаимные аргументы
    group1 = parser.add_mutually_exclusive_group(required=False)

    group1.add_argument("--source", type=str, dest="from_file",
                        help="Файл, из которого будет производиться десериализация")

    group1.add_argument("--destination", type=str, dest="to_file",
                        help="Путь к файлу, куда будем сериализовывать")

    parser.add_argument("--mode", type=str, required=True, choices=["Serialize", "Deserialize"], dest="mode",
                        help="Режим работы: сериализация/десериализация")

    parser.add_argument("--type", default="JSON", type=str, choices=["JSON", "YAML", "TOML"], dest="type_of_ser",
                        help="Тип, в который будет сериализованы данные")

    parser.add_argument("--destination_type", type=str, required=True, choices=["File", "String"], dest="file_or_string",
                        help="Выбор сериализации в файл или в строку. Из файла/строки")


    args = parser.parse_args()

    return args
