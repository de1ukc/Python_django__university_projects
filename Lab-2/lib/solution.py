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

    #a = [1, 2.424, ("str", 'str2', (7, 6, 5, 3, 2, 1)),
     #    ['arr', ['barr', ['darr', ['marr', 'jarr', ['varr'], 22], 55], 66],
      #    [234, [7, 5, '44432']], 'aristokrat'], 'second first']
    #print("HERE")
    #print(serializer.dumps(a))
    #print(a.isdecimal())
    #print(is_float(a))

    #dictionary = {}
    #dictionary["leh"] = 1
    # simple objects
    #a = (1, 2, "KOLYA", True, False, ("Hi", "MARK"), [True, "Kenobi", [(69, 420), ["VALAKAS", 228]]], None)
    #print("STANDART:")
    #standart = json.dumps(a)
    #print(standart)
    #print("MY:")
    #mine = serializer.dumps(a)
    #print(mine)
    #print("\nIs equals?")
    #print(standart == mine)

    # print("STANDART LOAD:")
    # standart_load = json.loads(standart)
    # print(standart_load)

    # print("MY_LOAD:")
    # mine_load = serializer.loads(mine)
    # print(mine_load)

    #print("\nIs equals?")
    #print(standart_load == mine_load)

    #print(type(standart_load))



    simple = dict(int_list=[1, 2, 3],

                  text='string',

                  number=3.44,

                  boolean=True,

                  none=None,

                  arguments=['Avada', ("Kolya", 15)],

                  d={"a": 1, "b": 2}
                  )

    ####################################################################################

    #a = (1,3)
    #new_graph = {}
    #new_graph[1] = "abacaba"
    #new_graph[2] = simple

    #print(json.dumps(simple))

    #print(serializer.dumps(simple))

    #bind = [1, 2, (3, 4), simple]
    #print("STANDART:")
    #standart = json.dumps(bind)
    #print(standart)
    #print("MY:")
    #mine = serializer.dumps(bind)
    #print(mine)
    #print("\nIs equals?")
    #print(standart == mine)
    #print(json.loads(json.dumps(bind)))

    my_obj = [11, 12.43, {"sd":{12:[34, 64, 24, "Suka"]}}, (123, 42, 123, "__init__"), {3:{2:{2:{3:{1:{1:{2:{1: 111},2: 121},2: "121"},2: "321"},2: "+++"},2: "121@"},2: ";lkjuytrewsa"},2: ["jhgfgh", 5434543, ("fdgdf", 424)]},1]
    my_ser = serializer.dumps(my_obj)
    print(my_obj)
    serializer.dump(my_obj, "../Files/JSONSerialize")
    print("TRY LOAD")
    objjj = serializer.load("../Files/JSONSerialize")
    print(objjj)
    print(objjj == json.load(open("../Files/JSONSerialize")))
    print("My ser:")
    print(my_ser)

    print("Json ser")
    print(json.dumps(my_obj))

    print(my_ser == json.dumps(my_obj))
    my_deser = serializer.loads(my_ser)


    print("My deser:")
    print(my_deser)

    print("Json deser")
    print(json.loads(json.dumps(my_obj)))

    print(my_deser == json.loads(json.dumps(my_obj)))

    d = {'__closure__': None, '__code__': {'TYPE': 'code',
                                           'VALUE': {'__doc__': 'Create a code object.  Not for the faint of heart.',
                                                     'co_argcount': 2, 'co_cellvars': {'TYPE': 'tuple', 'VALUE': []},
                                                     'co_code': {'TYPE': 'bytes',
                                                                 'VALUE': [124, 0, 124, 1, 23, 0, 83, 0]},
                                                     'co_consts': {'TYPE': 'tuple', 'VALUE': [None]},
                                                     'co_filename': '/home/de1ukc/Programming/OtherProjects/MyPython/serializer/main.py',
                                                     'co_firstlineno': 182, 'co_flags': 67,
                                                     'co_freevars': {'TYPE': 'tuple', 'VALUE': []},
                                                     'co_kwonlyargcount': 0,
                                                     'co_linetable': {'TYPE': 'bytes', 'VALUE': [8, 1]},
                                                     'co_lnotab': {'TYPE': 'bytes', 'VALUE': [0, 1]}, 'co_name': 'sm',
                                                     'co_names': {'TYPE': 'tuple', 'VALUE': []}, 'co_nlocals': 2,
                                                     'co_posonlyargcount': 0, 'co_stacksize': 2,
                                                     'co_varnames': {'TYPE': 'tuple', 'VALUE': ['a', 'b']}}},
         '__globals__': {}, '__defaults__': None, '__name__': 'sm'}

    aba = serializer.dumps(d)
    baba = serializer.loads(aba)
    print("HERE")
    print(d)
    "SER"
    print(aba)
    print("DESER")
    print(baba)
    print(baba == d)  # исходнный словарь ( разобраная функция) совпал с джсоном при сериализации и совпал с исходным объектом(словарём) при десериализзации.
    caba = json.dumps(d)
    print(caba)
    print(aba == caba)

if __name__ == "__main__":
    main()
