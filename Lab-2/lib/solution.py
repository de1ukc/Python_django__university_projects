import json
import math
import pprint

from lib.Serializers.Factory.SerializerFactory import factory
from lib.Serializers.JSONSerializer import JSONHelper


c = 42


#def f(x = 1, y = 2):
    #return math.sin(x * y * c)

#def f(a = 1, b = 1):
   # return a + b


#class mycls:
  #  example = f


def main() -> None:
    serializer = factory("Json")

   # print(JSONHelper.ser_func(f))

    #print(serializer.dumps(f))
    #ser_func = serializer.dumps(f)

  #  print(f.__getattribute__("__globals__"))
   # pprint.pprint(ser_func)


    #pprint.pprint(deser_func_dict)

    #pprint.pprint(f)



    fc = {'__closure__': None,
 '__code__': {'__doc__': 'Create a code object.  Not for the faint of heart.',
              'co_argcount': 2,
              'co_cellvars': [],
              'co_code': [124, 0, 124, 1, 23, 0, 83, 0],
              'co_consts': [None],
              'co_filename': '/home/de1ukc/Programming/GitReps/Python-Labs/Lab-2/lib/solution.py',
              'co_firstlineno': 15,
              'co_flags': 67,
              'co_freevars': [],
              'co_kwonlyargcount': 0,
              'co_linetable': [8, 1],
              'co_lnotab': [0, 1],
              'co_name': 'f',
              'co_names': [],
              'co_nlocals': 2,
              'co_posonlyargcount': 0,
              'co_stacksize': 2,
              'co_varnames': ['a', 'b']},
 '__defaults__': [1, 1],
 '__globals__': {'JSONHelper': '<class '
                               "'lib.Serializers.JSONSerializer.JSONHelper'>",
                 '__annotations__': {},
                 '__builtins__': "<module 'builtins' (built-in)>",
                 '__cached__': None,
                 '__doc__': None,
                 '__file__': '/home/de1ukc/Programming/GitReps/Python-Labs/Lab-2/lib/solution.py',
                 '__loader__': '<_frozen_importlib_external.SourceFileLoader '
                               'object at 0x7f6197d014e0>',
                 '__name__': '__main__',
                 '__package__': None,
                 '__spec__': None,
                 'c': 42,
                 'f': '<function f at 0x7f6197e43d90>',
                 'factory': '<function factory at 0x7f61922f4940>',
                 'json': "<module 'json' from "
                         "'/usr/lib64/python3.10/json/__init__.py'>",
                 'main': '<function main at 0x7f61922f6560>',
                 'math': "<module 'math' from "
                         "'/usr/lib64/python3.10/lib-dynload/math.cpython-310-x86_64-linux-gnu.so'>",
                 'mycls': "<class '__main__.mycls'>",
                 'pprint': "<module 'pprint' from "
                           "'/usr/lib64/python3.10/pprint.py'>"},
 '__module__': '__main__',
 '__name__': 'f'}

   # deser_func_dict = serializer.loads(fc)
    deser_func = JSONHelper.deser_func(fc)

    f = 1

    print(deser_func())
    print(deser_func.__getattribute__("__name__"))
    print(f)



if __name__ == "__main__":
    main()
