


def factory(type_of_serializer: str):
    """
    Метод создания нужного нам сериализатора в зависимости от запроса

    :param type_of_serializer: тип нужного сериализатора
    :type type_of_serializer: str

    :return: Возвращает сериализатор нужного нам формата
    :rtype: Serializer
    """
    if type_of_serializer == "JSON":
        print("JSON HERE BABY")
