import inspect
import json
import math
import pprint
from lib.Serializers.Factory.SerializerFactory import factory
from lib.Serializers.JSONSerializer import JSONHelper


c = 42

def pupa_lupa(x = 1, y = 2):
    s = json.dumps("ABACABA")
    return math.sin(x + y + c), s

class mycls:
    name = "Valery Albertych"
    age = 54
    pupa_lupa = pupa_lupa


def main() -> None:
    serializer = factory("Json")

    class_str = serializer.dumps(mycls)
    deser_class = serializer.loads(class_str)

    print(deser_class.pupa_lupa())


if __name__ == "__main__":
    main()
