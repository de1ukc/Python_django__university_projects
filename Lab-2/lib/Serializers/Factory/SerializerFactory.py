from ..JSONSerializer import JSONSerializer
from ..YAMLSerializer import YAMLSerializer
from ..TOMLSerializer import TOMLSerializer


def factory(type_of_serializer: str):
    """
    Метод создания нужного нам сериализатора в зависимости от запроса

    :param type_of_serializer: тип нужного сериализатора
    :type type_of_serializer: str

    :return: Возвращает сериализатор нужного нам формата
    :rtype: Serializer
    """

    type_of_serializer = type_of_serializer.lower()

    if type_of_serializer == 'json':
        return JSONSerializer()
    elif type_of_serializer == 'yaml':
        return YAMLSerializer()
    elif type_of_serializer == 'toml':
        return TOMLSerializer()