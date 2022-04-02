import pathlib
from pathology.path import Path
from Factory import SerializerFactory
from TerminalArguments.AddArguments import add_arguments

script_dir = Path.script_dir()


def main() -> None:
    
    # print(type(serializer))
    print(script_dir)
    pass


if __name__ == "__main__":
    main()
