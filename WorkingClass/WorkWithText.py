import math

class WorkWithText:
    '''Класс для работы с входным текстом'''

    def __init__(self) -> None:
        '''Конструктор класса'''
        self.stopSymbols = ['.', ',', '?', '!', ':', ';']
        self.stopSymbols2 = [',', '?', '!', ':', ';']

        return

    def RepeatOfEveryWord(self,fileName) -> dict:
        """
                    Метод нахождения количества повторений каждого слова в тексте.
                    :rtype: dict
                    :return: Возвращает контейнер с повторяющимися словами и количеством их повторений.
                """
        ans = dict()

        file = open(fileName, 'r')
        text = file.read()
        text = text.lower()  # всё к нижнему регистру
        text = text.lstrip()  # удаляю пробелы в начале
        text = text.rstrip()  # удаляю пробелы в конце

        # удаляем всё парные знаки, тире. Расшифровываю сокращения в полные слова
        text = text.replace('т.к.', 'так как', text.count('т.к.'))
        text = text.replace('т.п.', 'тому подобное', text.count('т.п.'))
        text = text.replace('т.д.', 'так далее', text.count('т.д.'))
        text = text.replace('др.', 'другое', text.count('др.'))
        text = text.replace('...', '', text.count('...'))
        text = text.replace('-', '', text.count('-'))
        text = text.replace('(', '', text.count('('))
        text = text.replace(')', '', text.count(')'))
        text = text.replace('"', '', text.count('"'))
        text = text.replace("'", '', text.count("'"))
        text.replace("/", '', text.count('/'))

        listOfWords = text.split()
        outputList = listOfWords.copy()

        for word in listOfWords:
            symb = word[-1]
            for sign in self.stopSymbols:
                if sign == symb:
                    outputList.remove(word)
                    word = word.replace(symb, '')
                    outputList.append(word)

        for word in outputList:
            if word in ans:
                ans[word] += 1
            else:
                ans[word] = 1
        return ans

    def RepeatOfEveryWordToFile(self,fileName,dic) -> None:
        '''Функция записывает результат работы аналогичного метода в файл

        '''
        file = open(fileName,"w")
        words = dic

        for word in words:
            file.write(word + ":" + str(words[word]) + "\n")
        file.write("\n")

        file.close()
        return

    def RepeatOfEveryWordToConsole(self,dic) -> None:
        '''Функция записывает результат работы аналогичного метода на консоль

        '''
        words = dic

        for word in words:
            print(word + ":" + str(words[word]))
        print('')
        return

    def AverageNumberOfWordsInASentence(self,fileName) -> float:
        '''Функция поодсчитывает среднее количество слов в предложении
        :rtype: float
        :return: Среднее число слов в предложении
        '''

        countOfWords = 0
        countOfSentences = 0

        text = self.TextHelper(fileName)

        # получения количества слов.
        buff = text.split()
        countOfWords = len(buff)
        countOfSentences = len(text.split('.')) - 1

        if countOfSentences == 0:
            return 0
        else:
            return countOfWords / countOfSentences

    def AverageNumberOfWordsInASentenceToFile(self,fileName, ans) -> None:
        '''Функция заносит результат аналогичного метода в файл'''
        file = open(fileName, "a")

        file.write("Среднее количество слов в предложении = " + str(ans))
        file.write('\n')

        file.close()
        return

    def AverageNumberOfWordsInASentenceToConsole(self, ans) -> None:
        '''Функция заносит результат аналогичного метода на консоль'''

        print("Среднее количество слов в предложении = " + str(ans)+"\n")
        return

    def TextHelper(self,fileName) -> str:
        '''Функция чистит текст от лишних символов. ? ! ... Также раскрывает сокращения согласно правилам
        :rtype: str
        :return: Выходная строка - почищенный текст
        '''

        file = open(fileName, 'r')

        text = file.read()
        text = text.lstrip()  # удаляю пробелы в начале
        text = text.rstrip()  # удаляю пробелы в конце
        text = text.replace('?', '.').replace('!', '.').replace('...', '.')
        text = text.replace('-', '', text.count('-'))

        text = text.replace('т.к.', 'так как', text.count('т.к.'))
        text = text.replace('т.п.', 'тому подобное', text.count('т.п.'))
        text = text.replace('т.д.', 'так далее', text.count('т.д.'))
        text = text.replace('др.', 'другое', text.count('др.'))
        file.close()
        return text

    def MedianNumberOfWordsInSentence(self,fileName) -> int:
        '''Функция подсчитывает медианное количество слов в предложении
        :rtype:int
        :return: Медианное число слов в предложении'''

        text = self.TextHelper(fileName)
        if text == '':
            return -1

        listOfNumbersForEverySentence = []

        listOfSentences = text.split(".")
        if '' in listOfSentences:
            listOfSentences.remove('')

        for sentense in listOfSentences:
            words = sentense.split()
            listOfNumbersForEverySentence.append(len(words))
        listOfNumbersForEverySentence.sort()

        medianAns = 0.
        medianPos = (len(listOfNumbersForEverySentence) + 1) / 2
        if medianPos is not int:
            medianAns = (listOfNumbersForEverySentence[math.ceil(medianPos) - 1] + listOfNumbersForEverySentence[
                math.floor(medianPos) - 1]) / 2
        else:
            medianAns = listOfNumbersForEverySentence[int(medianPos) - 1]

        # print(median(listOfNumbersForEverySentence))

        return medianAns

    def MedianNumberOfWordsInSentenceToFile(self,fileName, ans)-> None:
        '''Функция заносит результат аналогичного метода в файл'''
        file = open(fileName, "a")

        file.write("Медианное количество слов в предложении = " + str(ans))
        file.write("\n\n")

        file.close()
        return

    def MedianNumberOfWordsInSentenceToConsole(self, ans)-> None:
        '''Функция заносит результат аналогичного метода на консоль'''

        print("Медианное количество слов в предложении = " + str(ans)+"\n")
        return

    def HelpforTopfunc(self,fileName) -> str:
        '''Функция подчищает текст в помощь основной чистящей функции. Она убирает парные знаки, которые для работы в поставленном ТЗ не нужны.
        :rtype:str'''
        text = self.TextHelper(fileName)
        text = text.lower()
        for item in self.stopSymbols2:
            text = text.replace(item, '', text.count(item))

        text = text.replace('...', '', text.count('...'))
        text = text.replace('-', '', text.count('-'))
        text = text.replace('(', '', text.count('('))
        text = text.replace(')', '', text.count(')'))
        text = text.replace('"', '', text.count('"'))
        text = text.replace("'", '', text.count("'"))
        text.replace("/", '', text.count('/'))
        return text

    def GetKey(self,dictionary, value)->str:
        '''Функция реализована для поиска ключа по значению в словаре.
        :rtype: str
        :return: Возращает ключ(строку)'''
        for key, val in dictionary.items():
            if val == value:
                return key

    def TopK(self,fileName, N=4, K=10):
        '''Функция возвращает словарь самых популярных N-грамм в тексте
        :rtype:dict
        :return: Словарь самых популярных N-грамм'''

        text = self.HelpforTopfunc(fileName)
        # text = text.replace(item,'',text.count(item)) for item in stopSymbols2  как это провернуть?
        ans = dict()

        listOfSentences = [sentence.split() for sentence in text.split(".")]
        for listOfWords in listOfSentences:
            for word in listOfWords:
                if len(word) >= N:
                    for i in range(0, len(word) - N + 1):
                        if word[i: i + N] in ans:
                            ans[word[i: i + N]] += 1
                        else:
                            ans[word[i: i + N]] = 1
                else:
                    continue

        return ans

    def TopKToFile(self,ans, fileName, K=10)-> None:
        '''Функция заносит результат аналогичного метода в файл'''

        file = open(fileName, "a")

        sortedValues = sorted(ans.values())
        sortedValues.reverse()

        file.write(f"Топ {K}:" + "\n")
        for i in range(0, K):
            file.write(self.GetKey(ans,sortedValues[i]) + '-' + str(sortedValues[i]) + "\n")
            ans.pop(self.GetKey(ans, sortedValues[i]))

        file.close()
        return

    def TopKToConsole(self,ans, K=10)-> None:
        '''Функция заносит результат аналогичного метода на консоль'''

        sortedValues = sorted(ans.values())
        sortedValues.reverse()

        print(f"Топ {K}:")
        for i in range(0, K):
            print(self.GetKey(ans,sortedValues[i]) + '-' + str(sortedValues[i]))
            ans.pop(self.GetKey(ans, sortedValues[i]))
        print("\n")
        return