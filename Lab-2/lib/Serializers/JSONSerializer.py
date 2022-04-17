import re


from lib.Serializers.Serializer import Serializer


class JSONSerializer(Serializer):
    def dump(self):
        pass

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
            response = "{" + response

            for key in obj:
                if isinstance(key, (int, float, bool)) or key is None: # оборчиваю численные аргументы в ковычки
                    response += "\"" + JSONHelper.help_dumps(key) + "\"" + ": " + JSONHelper.help_dumps(obj[key]) + ", "
                else:
                    response += JSONHelper.help_dumps(key) + ": " + JSONHelper.help_dumps(obj[key])+", "
            response = response[:len(response) - 2] + "}" # убираю последнюю запятую с пробелом
        return response

    def load(self):
        pass
    @staticmethod
    def loads(serialized_str: str) -> object:
        obj = JSONHelper.help_loads(serialized_str)

        return obj


class JSONHelper:

    @staticmethod
    def help_dumps(obj) -> str:
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
            response = "{"

            for key in obj:
                response += JSONHelper.help_dumps(key) + ": " + JSONHelper.help_dumps(obj[key]) + ", "

            response = response[:len(response) - 2] + "}"  # убираю последнюю запятую с пробелом

            return response

    @staticmethod
    def help_loads(string: str):
        answer = None

        if string[0] == "[":
            answer = []
            #print(sys.getrecursionlimit())
            buffer_string = ""

            string = string[1:len(string) - 1]

            for item in string:
                if item == "[" or item == "{":
                    resp = JSONHelper.help_loads(string[string.index(item) + 1:])
                    answer.append(resp)
                    to_delete = str(resp).replace("'",'"',str(resp).count("'"))
                    item = string[string.index(item) - 1]
                    string.__iter__ = string.replace(to_delete,"").__iter__()
                    continue
                elif item == "]" or item == "}":
                    return answer
                elif item == '"' or item == "'" or item == " ":
                    continue
                elif item != "," and item != " ":
                    buffer_string += item
                else:
                    if buffer_string.isdecimal():
                        answer.append(int(buffer_string))
                    elif JSONHelper.is_float(buffer_string):
                        answer.append(float(buffer_string))
                    elif buffer_string == 'true':
                        answer.append(True)
                    elif buffer_string == 'false':
                        answer.append(False)
                    elif buffer_string == 'null':
                        answer.append(None)
                    else:
                        answer.append(buffer_string)
                    buffer_string = ""
        elif string[0] == "{":
            pass
        else:
            buffer_string = ""
            answer = []

            for item in string:
                if item == "[" or item == "{":
                    answer.append(JSONHelper.help_loads(string[string.index(item) + 1:]))

                elif item == "]" or item == "}":
                    answer.append(buffer_string)
                    return answer

                elif item == '"' or item == "'" or item == " ":
                    continue

                elif item != "," and item != " ":
                    buffer_string += item
                else:
                    if buffer_string.isdecimal():
                        answer.append(int(buffer_string))
                    elif JSONHelper.is_float(buffer_string):
                        answer.append(float(buffer_string))
                    elif buffer_string == 'true':
                        answer.append(True)
                    elif buffer_string == 'false':
                        answer.append(False)
                    elif buffer_string == 'null':
                        answer.append(None)
                    else:
                        answer.append(buffer_string)
                    buffer_string = ""

        return answer

    def is_float(num):
        try:
            float(num)
            return True
        except ValueError:
            return False









