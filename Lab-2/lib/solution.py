import json
import re

from lib.Serializers.Factory.SerializerFactory import factory
from lib.Serializers.JSONSerializer import JSONHelper
# from pathology.path import Path
# cript_dir = Path.script_dir()


def main() -> None:

    serializer = factory("Json")


    simple = dict(int_list=[1, 2, 3],

                  text='string',

                  number=3.44,

                  boolean=True,

                  none=None)

    print(json.dumps(simple))






if __name__ == "__main__":
    main()
