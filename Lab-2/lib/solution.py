import json
import re

from lib.Serializers.Factory.SerializerFactory import factory


def main() -> None:
    serializer = factory("Json")


if __name__ == "__main__":
    main()
