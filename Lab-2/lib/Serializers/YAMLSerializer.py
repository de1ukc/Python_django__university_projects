import inspect
from .Serializer import Serializer
import yaml
import json
import dill


class YAMLSerializer(Serializer):

    @staticmethod
    def dump(obj, file_name):
        ans = YAMLSerializer.dumps(obj)
        with open(file_name, 'w') as wfile:
            wfile.write(ans)

    @staticmethod
    def dumps(obj):
        def to_dict(obj):
            if inspect.isroutine(obj):
                ans = {"function": json.dumps(list(dill.dumps(obj)))}
            if inspect.isclass(obj):
                ans = {"class": json.dumps(list(dill.dumps(obj)))}
            if isinstance(obj, (list, dict)):
                ans = obj
            return ans

        return yaml.safe_dump(to_dict(obj))

    @staticmethod
    def load(file_name):
        with open(file_name, 'r') as rfile:
            string = rfile.read()

        return YAMLSerializer.loads(string)

    @staticmethod
    def loads(obj_in_str):
        if obj_in_str.find("function", 0, 10) != -1:
            obj_in_str = obj_in_str[11:-2]
            return dill.loads(bytes(json.loads(obj_in_str)))
        if obj_in_str.find("class", 0, 10) != -1:
            obj_in_str = obj_in_str[8:-2]
            return dill.loads(bytes(json.loads(obj_in_str)))
        else:
            return yaml.safe_load(obj_in_str)

# Разрешено использование встроенных реализаций YAML