import re

from lib.Serializers.Serializer import Serializer


class JSONSerializer(Serializer):
    def dump(self):
        pass

    @staticmethod
    def dumps(obj) -> str:
        object_type = re.search("\'(\w+)\'", str(type(obj)))[1]

        response = {}

        if object_type == 'tuple':
            pass



    def load(self):
        pass

    def loads(self):
        pass


class JSONHelper:
    """В данном классе будет находиться основная логика сериализации.
    Класс будет разбивать объекты для джейсона в кортежи и пихать это в один конечный словарь.
    Сам класс JSONSerializer будет лишь оборачивать в строку конечный результат, то есть, словарь.
    """
    @staticmethod
    def get_obj_in_tuples(obj) -> tuple:
        """Рекурсивная функция. Получает объект, потом проверяет его тип. В случае словаря,
        запускается рекурсия и словарь разбивается на подобъекты. По итогу возвращается кортеж кортежей"""
        response_dict = dict()  # промежуточный словарь ответов. После будет преобразован в кортеж

        object_type = re.search("\'(\w+)\'", str(type(obj)))[1]


        if isinstance(obj, (int, str, float, bool)):
            response_dict["type"] = object_type  # сюда должно идти, судя по всему, название поля, в случае сериализации
                                                 # просто цифры ничего не должно идти
            response_dict["value"] = obj
        elif isinstance(obj, tuple):
            response_dict["type"] = object_type

            response_dict["value"] = tuple([JSONHelper.get_obj_in_tuples(tuple_object) for tuple_object in obj])
            # если сериализумем кортеж, то он превращается в список, то же самое и с вложенными кортежами

        response = tuple((key, response_dict[key]) for key in response_dict)  # будет возвращать кортеж с кортежами ключей и значений, которые потом будут сериализоваться


        return response

    @staticmethod
    def recursive_parse(obj: tuple) -> str:

        tuples = JSONHelper.get_obj_in_tuples(obj)

        object_type = re.search("\'(\w+)\'", str(type(obj)))[1]

        if object_type == "tuple":
            response = []

            response.append(JSONHelper.recursive_parse())


        elif isinstance(obj, (int, float, bool, str)):
            return f"{str(obj)}"




        pass


