from lib.Serializers.Serializer import Serializer


class JSONSerializer(Serializer):
    def dump(self):
        pass

    def dumps(self):
        pass

    def load(self):
        pass

    def loads(self):
        pass


class JSONHelper:
    """В данном классе будет находиться основная логика сериализации.
    Класс будет разбивать объекты для джейсона в словари и пихать это в один конечный словарь.
    Сам класс JSONSerializer будет лишь оборачивать в строку конечный результат, то есть, словарь.
    """
    pass