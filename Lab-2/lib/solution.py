import toml
from Serializers.Factory.SerializerFactory import factory
import argparse
import files_paths
from fun import f
from cls import mycls


def add_arguments() -> None:
    """
    Функция добавляет к программе возможность использования аргументов командной строки.
    :rtype: None
    """
    parser = argparse.ArgumentParser(description="Аргументы командной строки для работы с программой "
                                                 "сериализации/ десериализации")

    #невзаимные аргументы
  #  group1 = parser.add_mutually_exclusive_group(required=False)

    parser.add_argument("--source", type=str, dest="from_file", required=True,
                        help="Файл, из которого будет производиться десериализация")

    parser.add_argument("--destination", type=str, dest="to_file",
                        help="Путь к файлу, куда будем сериализовывать")

    parser.add_argument("--mode", type=str, choices=["Serialize", "Deserialize"],default="Deserialize", dest="mode",
                        help="Режим работы: сериализация/десериализация")

    parser.add_argument("--type", default="JSON", type=str, choices=["JSON", "YAML", "TOML"], dest="type_of_ser",
                        help="Тип, в который будет сериализованы данные")

    parser.add_argument("--destination_type", type=str, required=True, choices=["File", "String"], dest="file_or_string",
                        help="Выбор сериализации в файл или в строку. Из файла/строки")

    args = parser.parse_args()
    #print(args.file_or_string)
    return args


def what_to_do(args) -> None:
    if files_paths.JSON_PATH.find(args.from_file) != -1:
        deser_type = "JSON"
        from_file = files_paths.JSON_PATH
    elif files_paths.TOML_PATH.find(args.from_file) != -1:
        deser_type = "TOML"
        from_file = files_paths.TOML_PATH
    else:
        deser_type = "YAML"
        from_file = files_paths.YAML_PATH

    serializer = factory(deser_type)
    obj = serializer.load(from_file)
    dumper = factory(args.type_of_ser)

    if args.file_or_string == "File":
        dumper.dump(obj, args.to_file)
    elif args.file_or_string == "String":
        if args.mode == "Deserialize":
            print(obj)
        else:
            print(dumper.dumps(obj))



def main() -> None:
    args = add_arguments()
    what_to_do(args)


if __name__ == "__main__":
    main()
