import math
from WorkingClass.constants import stop_symbols
from WorkingClass.constants import stop_symbols2


class WorkWithText:
    """Класс для работы с входным текстом"""

    def __init__(self) -> None:
        return

    def repeat_of_every_word(self, file_name: str) -> dict:
        """
        Метод нахождения количества повторений каждого слова в тексте.
        :rtype: dict
        :return: Возвращает контейнер с повторяющимися словами и количеством их повторений.
        """

        response = dict()

        text = self.text_helper(file_name)

        text = text.replace('-', '', text.count('-'))
        text = text.replace('(', '', text.count('('))
        text = text.replace(')', '', text.count(')'))
        text = text.replace('"', '', text.count('"'))
        text = text.replace("'", '', text.count("'"))
        text = text.replace("/", '', text.count('/'))

        list_of_words = text.split()
        output_list = list_of_words.copy()

        for word in list_of_words:
            symb = word[-1]
            for sign in stop_symbols:
                if sign == symb:
                    output_list.remove(word)
                    word = word.replace(symb, '')
                    output_list.append(word)

        for word in output_list:
            if word in response:
                response[word] += 1
            else:
                response[word] = 1

        return response

    @staticmethod
    def repeat_of_every_word_to_file(file_name: str, dic: dict) -> None:
        """
        Функция записывает результат работы аналогичного метода в файл
        """

        file = open(file_name, "w")

        words = dic

        for word in words:
            file.write(word + ":" + str(words[word]) + "\n")
        file.write("\n")

        file.close()

        return

    @staticmethod
    def repeat_of_every_word_to_console(dic: dict) -> None:
        """
        Функция записывает результат работы аналогичного метода на консоль
        """

        words = dic

        for word in words:
            print(word + ":" + str(words[word]))
        print('')

        return

    def average_number_of_words_in_a_sentence(self, file_name: str) -> float:
        """
        Функция поодсчитывает среднее количество слов в предложении
        :param file_name: name of file
        :type file_name: str
        :rtype: float
        :return: Среднее число слов в предложении
        """

        count_of_words = 0
        count_of_sentences = 0

        text = self.text_helper(file_name)

        # получения количества слов.
        buff = text.split()
        count_of_words = len(buff)
        count_of_sentences = len(text.split('.')) - 1

        if count_of_sentences == 0:
            return 0
        else:
            return count_of_words / count_of_sentences

    @staticmethod
    def average_number_of_words_in_a_sentence_to_file(file_name: str, ans: float) -> None:
        """
        Функция заносит результат аналогичного метода в файл
        :param file_name : name of file
        :type file_name: str
        :param ans : average number of words in sentence
        :type ans: float
        """

        file = open(file_name, "a")

        file.write("Среднее количество слов в предложении = " + str(ans))
        file.write('\n')

        file.close()

        return

    @staticmethod
    def average_number_of_words_in_a_sentence_to_console(ans: float) -> None:
        """
        Функция заносит результат аналогичного метода на консоль
        :param ans : average number of words in sentence
        :type ans: float
        """

        print("Среднее количество слов в предложении = " + str(ans)+"\n")

        return

    @staticmethod
    def text_helper(file_name: str) -> str:
        """
        Функция чистит текст от лишних символов. ? ! ... Также раскрывает сокращения согласно правилам
        :param file_name : name of file
        :type file_name: str
        :rtype: str
        :return: Выходная строка - почищенный текст
        """

        file = open(file_name, 'r')

        text = file.read().lstrip().rstrip()
        text = text.replace('?', '.').replace('!', '.').replace('...', '.')
        text = text.replace('-', '', text.count('-'))
        text = text.replace('т.к.', 'так как', text.count('т.к.'))
        text = text.replace('т.п.', 'тому подобное', text.count('т.п.'))
        text = text.replace('т.д.', 'так далее', text.count('т.д.'))
        text = text.replace('др.', 'другое', text.count('др.'))

        file.close()

        return text

    def median_number_of_words_in_sentence(self, file_name: str) -> int:
        """
        Функция подсчитывает медианное количество слов в предложении
        :param file_name: name of file
        :type file_name:str
        :rtype:int
        :return: Медианное число слов в предложении
        """

        text = self.text_helper(file_name)

        if text == '':
            return -1

        list_of_numbers_for_every_sentence = []

        list_of_sentences = text.split(".")

        if '' in list_of_sentences:
            list_of_sentences.remove('')

        for sentence in list_of_sentences:
            words = sentence.split()
            list_of_numbers_for_every_sentence.append(len(words))
        list_of_numbers_for_every_sentence.sort()

        median_ans = 0.
        median_pos = (len(list_of_numbers_for_every_sentence) + 1) / 2
        if median_pos is not int:
            median_ans = (list_of_numbers_for_every_sentence[math.ceil(median_pos) - 1]
                          + list_of_numbers_for_every_sentence[
                math.floor(median_pos) - 1]) / 2
        else:
            median_ans = list_of_numbers_for_every_sentence[int(median_pos) - 1]

        return median_ans

    @staticmethod
    def median_number_of_words_in_sentence_to_file(file_name: str, ans: int) -> None:
        """
        Функция заносит результат аналогичного метода в файл
        :param file_name: name of file
        :type file_name: str
        :param ans: median number of words in sentence
        :type ans: int
        """
        file = open(file_name, "a")

        file.write("Медианное количество слов в предложении = " + str(ans))
        file.write("\n\n")

        file.close()

        return

    @staticmethod
    def median_number_of_words_in_sentence_to_console(ans: int) -> None:
        """
        Функция заносит результат аналогичного метода на консоль
        :param ans: median number of words in sentence
        :type ans: int
        """

        print("Медианное количество слов в предложении = " + str(ans)+"\n")

        return

    def helpfor_topfunc(self, file_name: str) -> str:
        """Функция подчищает текст в помощь основной чистящей функции. Она убирает парные знаки,
         которые для работы в поставленном ТЗ не нужны.
        :param file_name: name of file
        :type: str
        :rtype:str
        """

        text = self.text_helper(file_name)
        text = text.lower()

        for item in stop_symbols2:
            text = text.replace(item, '', text.count(item))

        text = text.replace('...', '', text.count('...'))
        text = text.replace('-', '', text.count('-'))
        text = text.replace('(', '', text.count('('))
        text = text.replace(')', '', text.count(')'))
        text = text.replace('"', '', text.count('"'))
        text = text.replace("'", '', text.count("'"))
        text.replace("/", '', text.count('/'))

        return text

    @staticmethod
    def get_key(dictionary: dict, value: int) -> str:
        """
        Функция реализована для поиска ключа по значению в словаре.
        :param dictionary: словарь, в котором ищем
        :type dictionary: dict
        :param value: значение, по которому вернётся ключ
        :type: int
        :rtype: str
        :return: Возвращает ключ(строку)
        """

        for key, val in dictionary.items():
            if val == value:
                return key

    def top_k(self, file_name: str, n=4) -> dict:
        """
        Функция возвращает словарь самых популярных N-грамм в тексте
        :param file_name: name of file
        :type file_name: str
        :param n: number of symbols in N-gramm
        :type n; int
        :rtype:dict
        :return: Словарь самых популярных N-грамм
        """

        text = self.helpfor_topfunc(file_name)
        # text = text.replace(item,'',text.count(item)) for item in stopSymbols2  как это провернуть?
        ans = dict()

        list_of_sentences = [sentence.split() for sentence in text.split(".")]

        for list_of_words in list_of_sentences:
            for word in list_of_words:
                if len(word) >= n:
                    for i in range(0, len(word) - n + 1):
                        if word[i: i + n] in ans:
                            ans[word[i: i + n]] += 1
                        else:
                            ans[word[i: i + n]] = 1

        return ans

    @staticmethod
    def top_k_to_file(ans, file_name, k=10) -> None:
        """
        Функция заносит результат аналогичного метода в файл
        :param ans : dictionary with N-gramms
        :type ans: dict
        :param file_name: name of file
        :type file_name: str
        :param k: number of Top-K
        :type k: int
        """

        file = open(file_name, "a")

        sorted_values = sorted(ans.values())
        sorted_values.reverse()

        file.write(f"Топ {k}:" + "\n")
        for i in range(0, k):
            file.write(WorkWithText.get_key(ans, sorted_values[i]) + '-' + str(sorted_values[i]) + "\n")
            ans.pop(WorkWithText.get_key(ans, sorted_values[i]))

        file.close()

        return

    @staticmethod
    def top_k_to_console(ans: dict, k=10) -> None:
        """
        Функция заносит результат аналогичного метода на консоль
        :param ans : dictionary with N-gramms
        :type ans: dict
        :param k: number of Top-K
        :type k: int
        """

        sorted_values = sorted(ans.values())
        sorted_values.reverse()

        print(f"Топ {k}:")

        for i in range(0, k):
            print(WorkWithText.get_key(ans, sorted_values[i]) + '-' + str(sorted_values[i]))
            ans.pop(WorkWithText.get_key(ans, sorted_values[i]))
        print("\n")

        return
