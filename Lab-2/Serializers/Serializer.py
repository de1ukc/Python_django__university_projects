from abc import abstractmethod


class Serializer:
    @abstractmethod
    def dump(self):
        """
        Cериализует Python объект в файл
        """
        pass

    @abstractmethod
    def dumps(self):
        """
        Cериализует Python объект в строку
        """
        pass

    @abstractmethod
    def load(self):
        """
        Десериализует Python объект из файла
        """
        pass

    @abstractmethod
    def loads(self):
        """
        Десериализует Python объект из строки
        """
        pass
