import json
import math
import pprint

from lib.Serializers.Factory.SerializerFactory import factory
from lib.Serializers.JSONSerializer import JSONHelper


c = 42


def pupa_lupa(x = 1, y = 2):
    s = json.dumps("ABACABA")
    return math.sin(x + y + c), s

#def f(a = 1, b = 1):
   # return a + b


#class mycls:
  #  example = f


def main() -> None:
    serializer = factory("Json")

   # print(JSONHelper.ser_func(f))

    #print(serializer.dumps(f))
    #ser_func = serializer.dumps([1, pupa_lupa])
    ser_func = serializer.dumps(pupa_lupa)
    deser_func_dict = serializer.loads(ser_func)
    print(deser_func_dict)
    deser_func = JSONHelper.deser_func(deser_func_dict)

    print("HERE")
    print(deser_func())
    print(deser_func.__getattribute__("__name__"))
    print(pupa_lupa())

    lst = [1,pupa_lupa]
    aaa = serializer.dumps(lst)
    ans2 = serializer.loads(aaa)
    print(ans2[1]())





if __name__ == "__main__":
    main()
