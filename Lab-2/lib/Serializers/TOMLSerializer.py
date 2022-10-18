import inspect
import json
from .Serializer import Serializer
import toml
import dill


class TOMLSerializer(Serializer):
    @staticmethod
    def dump(obj: object, file_name: str):
        ans = TOMLSerializer.dumps(obj)

        with open(file_name, "w") as file:
            file.write(ans)


    @staticmethod
    def dumps(obj: object):
        def to_dict(obj):
            if inspect.isroutine(obj):
                ans = {"function": json.dumps(list(dill.dumps(obj)))}
            if inspect.isclass(obj):
                ans = {"class": json.dumps(list(dill.dumps(obj)))}
            if isinstance(obj, list):
                ans = {"list": json.dumps(obj)}
                if "null" in ans["list"]:
                   ans["list"] = ans["list"].replace("null", 'None,', ans["list"].count('null'))
            if isinstance(obj, dict):
                ans = obj

            return ans

        return toml.dumps(to_dict(obj))


    @staticmethod
    def load(file_name):
        with open(file_name, 'r') as file:
            s = file.read()
            ans = TOMLSerializer.loads(s)
        return ans

    @staticmethod
    def loads(obj_in_str):
        if obj_in_str.find("function", 0, 10) != -1:
            obj_in_str = obj_in_str[12:-2]
            return dill.loads(bytes(json.loads(obj_in_str)))
        if obj_in_str.find("class", 0, 10) != -1:
            obj_in_str = obj_in_str[9:-2]
            return dill.loads(bytes(json.loads(obj_in_str)))
        if obj_in_str.find("list", 0, 10) != -1:
            obj_in_str = obj_in_str[8:-2]
            obj_in_str = obj_in_str.replace('None,', 'null', obj_in_str.count("None"))
            return json.loads(obj_in_str)
        else:
            return toml.loads(obj_in_str)

# Разрешено использование встроенных реализаций TOML