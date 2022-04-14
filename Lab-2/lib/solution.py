from lib.Serializers.Factory.SerializerFactory import factory
# from pathology.path import Path
# cript_dir = Path.script_dir()


def main() -> None:

    serializer = factory("Json")


if __name__ == "__main__":
    main()
