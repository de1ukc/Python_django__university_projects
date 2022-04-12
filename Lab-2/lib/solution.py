import pathlib
from pathology.path import Path
from Factory import SerializerFactory
import json

script_dir = Path.script_dir()

a = dict()
a["Aleh"] = "Oleg"

def main() -> None:
    
    print(json.dumps(a))


if __name__ == "__main__":
    main()
