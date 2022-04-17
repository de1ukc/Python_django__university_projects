import json
import re

from lib.Serializers.Factory.SerializerFactory import factory
from lib.Serializers.JSONSerializer import JSONHelper
# from pathology.path import Path
# cript_dir = Path.script_dir()

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def main() -> None:

    serializer = factory("Json")

    a = '1.21'
    print(a.isdecimal())
    print(is_float(a))

    dictionary = {}
    dictionary["leh"] = 1
    # simple objects
    a = (1, 2, "KOLYA", True, False, ("Hi", "MARK"), [True, "Kenobi", [(69, 420), ["VALAKAS", 228]]], None)
    print("STANDART:")
    standart = json.dumps(a)
    print(standart)
    print("MY:")
    mine = serializer.dumps(a)
    print(mine)
    print("\nIs equals?")
    print(standart == mine)

    print("STANDART LOAD:")
    standart_load = json.loads(standart)
    print(standart_load)

    print("MY_LOAD:")
    mine_load = serializer.loads(mine)
    print(mine_load)

    print("\nIs equals?")
    print(standart_load == mine_load)

    print(type(standart_load))



    simple = dict(int_list=[1, 2, 3],

                  text='string',

                  number=3.44,

                  boolean=True,

                  none=None,

                  arguments=['Avada', ("Kolya", 15)]
                  )

    ####################################################################################

    #a = (1,3)
    #new_graph = {}
    #new_graph[1] = "abacaba"
    #new_graph[2] = simple

    #print(json.dumps(simple))

    #print(serializer.dumps(simple))

    #print("STANDART:")
    #standart = json.dumps(new_graph)
    #print(standart)
    #print("MY:")
    #mine = serializer.dumps(new_graph)
    #print(mine)
    #print("\nIs equals?")
    #print(standart == mine)


if __name__ == "__main__":
    main()
