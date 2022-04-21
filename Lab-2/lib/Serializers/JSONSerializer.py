import inspect
import modulefinder
import re
from importlib import import_module
from pprint import pprint
from types import FunctionType, CodeType

from lib.Serializers.Attributes import FUNCTION_ATTRIBUTES
from lib.Serializers.Attributes import CODE_ARGUMENTS


from lib.Serializers.Serializer import Serializer


class JSONSerializer(Serializer):

    @staticmethod
    def dump(obj: object, file_name: str):
        string = JSONSerializer.dumps(obj)

        with open(file_name, "w") as file:
            file.write(string)


    @staticmethod
    def dumps(obj) -> str:
        serialized = []
        keys = []

        response = ""

        if isinstance(obj, (list, tuple)):
            for item in obj:
                serialized.append(JSONHelper.help_dumps(item))

            response = ", ".join(serialized)
            response = "[" + response + "]"
        elif isinstance(obj, (float, int, bool, str)):
            response = JSONHelper.help_dumps(obj)

        elif isinstance(obj, dict):
            if not obj:  # если пустой
                return "{}"

            response = "{" + response

            for key in obj:
                if isinstance(key, (int, float, bool)) or key is None: # оборчиваю численные аргументы в ковычки
                    response += "\"" + JSONHelper.help_dumps(key) + "\"" + ": " + JSONHelper.help_dumps(obj[key]) + ", "
                else:
                    response += JSONHelper.help_dumps(key) + ": " + JSONHelper.help_dumps(obj[key])+", "
            response = response[:len(response) - 2] + "}" # убираю последнюю запятую с пробелом
        elif inspect.isclass(obj):
            pass
        elif inspect.isroutine(obj):  # объект, определяемый пользователем

            ans = JSONHelper.ser_func(obj)

            resp = JSONSerializer.dumps(ans)
            response  = resp

        return response

    @staticmethod
    def load(file_name) -> object:
        with open(file_name, "r") as file:
            obj = JSONSerializer.loads(file.read())
        return obj

    @staticmethod
    def loads(serialized_str: str) -> object:
        obj = JSONHelper.loads(serialized_str)

        return obj


class JSONHelper:

    @staticmethod
    def help_dumps(obj) -> str:
        a = type(obj)

        if isinstance(obj, (bool, float, int)):
            return str(obj).lower()
        elif isinstance(obj, str):
            return "\"" + obj + "\""
        elif obj is None:
            return "null"
        elif isinstance(obj, (tuple, list)):
            serialized = []
            response = ""

            for item in obj:
                serialized.append(JSONHelper.help_dumps(item))

            response = ", ".join(serialized)
            response = "[" + response + "]"

            return response
        elif isinstance(obj, dict):

            if not obj:  # если пустой
                return "{}"

            response = "{"

            for key in obj:
                if isinstance(key, (int, float)):
                    response += '"' + JSONHelper.help_dumps(key) + '"' + ": " + JSONHelper.help_dumps(obj[key]) + ", "
                else:
                    response += JSONHelper.help_dumps(key) + ": " + JSONHelper.help_dumps(obj[key]) + ", "

            response = response[:len(response) - 2] + "}"  # убираю последнюю запятую с пробелом

            return response
        elif isinstance(obj, bytes):
            response = str(list(obj))
        else:
            response = str(obj)

        return response

    @staticmethod
    def loads(json_string: str) -> object:
        def loads_list(string_to_list: str) -> (list, str):
            ans = []
            i = 0
            border = len(string_to_list)
            number_in_str = False
            buffer_str = ""

            while i < border:
                if string_to_list[i] == "[":
                    resp = loads_list(string_to_list[i + 1:])
                    ans.append(resp[0])
                    string_to_list = resp[1]
                    border = len(string_to_list)
                    i = - 1
                elif string_to_list[i] == "]":
                    if buffer_str != "":
                        if is_float(buffer_str):
                            if number_in_str:
                                ans.append(buffer_str)
                                number_in_str = False
                            else:
                                ans.append(float(buffer_str))
                        elif buffer_str.isdigit():
                            if number_in_str:
                                ans.append(buffer_str)
                            else:
                                ans.append(int(buffer_str))
                            number_in_str = False
                        elif buffer_str == "true":
                            ans.append(True)
                        elif buffer_str == "false":
                            ans.append(False)
                        elif buffer_str == "null":
                            ans.append(None)
                        else:
                            ans.append(buffer_str)

                    return (ans, string_to_list[i + 1:])


                elif string_to_list[i] == "{":
                    resp = loads_dict(string_to_list[i + 1:])
                    ans.append(resp[0])
                    string_to_list = resp[1]
                    border = len(string_to_list)
                    i = - 1
                # elif: # проверка на функцию
                # elif: # проверка на класс

                else:

                    if string_to_list[i].isdigit():
                        buffer_str += string_to_list[i]
                    elif string_to_list[i] == ".":
                        if string_to_list[i - 1].isdigit():
                            buffer_str += string_to_list[i]
                        else:
                            pass
                    elif string_to_list[i] == " ":
                        if string_to_list[i - 1] != ",":
                            buffer_str += string_to_list[i]
                            i += 1
                            continue
                        if is_float(buffer_str):
                            if number_in_str:
                                ans.append(buffer_str)
                                number_in_str = False
                            else:
                                ans.append(float(buffer_str))
                        elif buffer_str.isdigit():
                            if number_in_str:
                                ans.append(buffer_str)
                                number_in_str = False
                            else:
                                ans.append(int(buffer_str))
                        elif buffer_str == "":
                            pass
                        elif buffer_str == "true":
                            ans.append(True)
                        elif buffer_str == "false":
                            ans.append(False)
                        elif buffer_str == "null":
                            ans.append(None)
                        else:
                            ans.append(buffer_str)
                        buffer_str = ""
                        i += 1
                        continue
                    elif string_to_list[i] == ',':
                        i += 1
                        continue
                    elif string_to_list[i] == '"':
                        if string_to_list[i + 1].isdigit():
                            number_in_str = True
                        i += 1
                        continue
                    else:
                        buffer_str += string_to_list[i]
                i += 1

        def loads_dict(string_to_dict: str) -> (dict, str):
            ans = {}
            i = 0
            border = len(string_to_dict)
            buffer_value = ""
            buffer_key = ""
            number_in_str = False
            is_key = True

            while i < border:

                if string_to_dict[i] == "{":
                    resp = loads_dict(string_to_dict[i + 1:])
                    ans[buffer_key] = resp[0]
                    string_to_dict = resp[1]
                    border = len(string_to_dict)
                    i = -1
                    buffer_value = ""
                    buffer_key = ""
                elif string_to_dict[i] == "[":
                    resp = loads_list(string_to_dict[i + 1:])
                    ans[buffer_key] = resp[0]
                    string_to_dict = resp[1]
                    border = len(string_to_dict)
                    i = -1
                    buffer_value = ""
                    buffer_key = ""
                elif string_to_dict[i] == "}":
                    if buffer_key != "" and buffer_value != "":

                        if buffer_key == "false":
                            buffer_key = False
                        elif buffer_key == "true":
                            buffer_key = True
                        elif buffer_key == "null":
                            buffer_key = None

                        if buffer_value.isdigit():
                            buffer_value = int(buffer_value)
                        elif is_float(buffer_value):
                            buffer_value = float(buffer_value)
                        elif buffer_value == "false":
                            buffer_value = False
                        elif buffer_value == "true":
                            buffer_value = True
                        elif buffer_value == "null":
                            buffer_value = None
                        ans[buffer_key] = buffer_value

                    return ans, string_to_dict[i + 1:]
                else:
                    if string_to_dict[i] == '"':
                        i += 1
                        continue
                    elif string_to_dict[i] == ":":
                        is_key = False
                        i += 1
                        continue

                    elif string_to_dict[i] == ",":

                        if buffer_key == "false":
                            buffer_key = False
                        elif buffer_key == "true":
                            buffer_key = True
                        elif buffer_key == "null":
                            buffer_key = None

                        if buffer_value.isdigit():
                            buffer_value = int(buffer_value)
                        elif is_float(buffer_value):
                            buffer_value = float(buffer_value)
                        elif buffer_value == "false":
                            buffer_value = False
                        elif buffer_value == "true":
                            buffer_value = True
                        elif buffer_value == "null":
                            buffer_value = None
                        if buffer_value != "" and buffer_key != "":
                            ans[buffer_key] = buffer_value
                        buffer_value = ""
                        buffer_key = ""
                        is_key = True
                        i += 1
                        continue
                    elif string_to_dict[i] == " ":
                        if string_to_dict[i - 1] != "," and string_to_dict[i - 1] != ":":
                            if is_key:
                                buffer_key += string_to_dict[i]
                            else:
                                buffer_value += string_to_dict[i]
                        i += 1
                        continue
                    else:
                        if is_key:
                            buffer_key += string_to_dict[i]
                        else:
                            buffer_value += string_to_dict[i]
                i += 1

        def loads_primitives(string_to_prim: str) -> (object, str):
            pass

        def is_float(s):
            result = False
            if s.count(".") == 1:
                if s.replace(".", "").isdigit():
                    result = True
            return result

        ######################################################################################
        ######################################################################################
        ######################################################################################
        # int в кортеже возврата - индекс, по который нужно обрезать строку

        if json_string[0] == "[":
            response = []
        elif json_string[0] == "{":
            response = {}
        else:
            response = None

        i = -1
        border = len(json_string)
        simple_type_ans = ""

        while i < border:
            i += 1

            if simple_type_ans != "" and i == border:
                if simple_type_ans.isdigit():
                    response = int(simple_type_ans)
                elif is_float(simple_type_ans):
                    response = float(simple_type_ans)
                elif simple_type_ans == "false":
                    response = False
                elif simple_type_ans == "true":
                    response = True
                elif simple_type_ans == "null":
                    response = None
                if simple_type_ans[0] == '"' and simple_type_ans[-1] == '"':
                    response = simple_type_ans[1:-1]
                return response
            if json_string == "":
                if isinstance(response, list):
                    return response[0]
                if isinstance(response, dict):
                    return response["ans"]
            elif json_string[i] == "[":
                if isinstance(response, list):
                    resp = loads_list(json_string[i + 1:])
                    response.append(resp[0])
                    json_string = resp[1]
                    border = len(json_string)
                    i = -1
                elif isinstance(response, dict):  # ?????? не уверен
                    resp = loads_dict(json_string[i + 1:])
                    response["ans"] = resp[0]
                    json_string = resp[1]
                    border = len(json_string)
                    i = -1
            elif json_string[i] == "]":  # ??? зачем?
                pass
            elif json_string[i] == "{":
                resp = loads_dict(json_string[i + 1:])
                response["ans"] = resp[0]
                json_string = resp[1]
                border = len(json_string)
                i = -1
            elif json_string[i] == "}":
                return response["ans"]
            else:
                simple_type_ans += json_string[i]
        return response

    @staticmethod
    def ser_func(func: object) -> dict:
        def get_code_dict(code: object) -> dict:
            response = {}

            attrs = inspect.getmembers(code)

            for attr in attrs:
                if callable(attr[1]):
                    continue
                response[attr[0]] = attr[1]

            return response

        ans = {}
        attributes = inspect.getmembers(func)

        required_attributes = [att for att in attributes if att[0] in FUNCTION_ATTRIBUTES]

        for attr in required_attributes:
            if attr[0] == "__code__":
                ans[attr[0]] = get_code_dict(attr[1])
            else:
                ans[attr[0]] = attr[1]
        return ans


    @staticmethod
    def deser_func(str_dict: dict) -> object:

        func_dict = JSONHelper.dict_to_norm(str_dict)

        code = func_dict["__code__"]

        args = []

        for attr in CODE_ARGUMENTS:
            arg = code[attr]
            args.append(arg)


        det = [CodeType(*args)]

        glob = {"__builtins__": __builtins__}

        for name, obj in func_dict["__globals__"].items():
            glob[name] = obj

        for key in glob:
            if isinstance(glob[key], str):
                if glob[key].find('module') and not key.startswith('__') and key != "factory" and key != "JSONHelper" \
                        and key != str_dict["__name__"]  and key != "main":
                    glob[key] = import_module(key)

        det.append(glob)

        for attr in FUNCTION_ATTRIBUTES:
            if attr == "__code__" or attr == "__module__" or attr == "__globals__":
                continue
            if attr == "__defaults__":
                det.append(tuple(func_dict[attr]))
            else:
                det.append(func_dict[attr])

        resul_function = FunctionType(*det)

        return resul_function

    @staticmethod
    def dict_to_norm(str_dict) -> dict:

        for key in str_dict:
            if key == "__code__":
                str_dict["__code__"]["co_cellvars"] = tuple(str_dict["__code__"]["co_cellvars"])
                str_dict["__code__"]["co_consts"] = tuple(str_dict["__code__"]["co_consts"])
                str_dict["__code__"]["co_code"] = bytes(str_dict["__code__"]["co_code"])
                str_dict["__code__"]["co_freevars"] = tuple(str_dict["__code__"]["co_freevars"])
                str_dict["__code__"]["co_linetable"] = bytes(str_dict["__code__"]["co_linetable"])
                str_dict["__code__"]["co_lnotab"] = bytes(str_dict["__code__"]["co_lnotab"])
                str_dict["__code__"]["co_names"] = tuple(str_dict["__code__"]["co_names"])
                str_dict["__code__"]["co_varnames"] = tuple(str_dict["__code__"]["co_varnames"])
            if key == "__globals__":
                pass

        return str_dict



