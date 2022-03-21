from Factory import SerializerFactory


def main() -> None:
    serializer = SerializerFactory.factory("JSON")


if __name__ == "__main__":
    main()
