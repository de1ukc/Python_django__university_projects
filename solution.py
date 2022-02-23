import math
#from statistics import median проверял
stopSymbols = ('.',',','?','!',':',';')
stopSymbols2 = (',','?','!',':',';')

#функция будет возвращать словарь с количеством повторений каждого слова
def RepeatOfEveryWord(fileName):
    ans = dict()

    file = open(fileName,'r')
    text = file.read()
    text = text.lower()  # всё к нижнему регистру
    text = text.lstrip()  # удаляю пробелы в начале
    text = text.rstrip()  # удаляю пробелы в конце

    #удаляем всё парные знаки, тире. Расшифровываю сокращения в полные слова
    text = text.replace('т.к.','так как',text.count('т.к.'))
    text = text.replace('т.п.','тому подобное',text.count('т.п.'))
    text = text.replace('т.д.', 'так далее', text.count('т.д.'))
    text = text.replace('др.','другое',text.count('др.'))
    text = text.replace('...', '', text.count('...'))
    text = text.replace('-','',text.count('-'))
    text = text.replace('(','',text.count('('))
    text = text.replace(')','',text.count(')'))
    text = text.replace('"','',text.count('"'))
    text = text.replace("'",'',text.count("'"))
    text.replace("/",'',text.count('/'))

    listOfWords = text.split()
    outputList = listOfWords.copy()

    for word in listOfWords:
        symb = word[-1]
        for sign in stopSymbols:
            if sign == symb:
                outputList.remove(word)
                word = word.replace(symb,'')
                outputList.append(word)

    for word in outputList:
        if word in ans:
            ans[word] += 1
        else:
            ans[word] = 1
    return ans

#функция записывать полученный словарь ответов в файл
def RepeatOfEveryWordToFile(fileName,dic):
    file = open(fileName,"w")
    words = dic

    for word in words:
        file.write(word + ":" + str(words[word]) + "\n")
    file.write("\n")

    file.close()
    return

def AverageNumberOfWordsInASentence(fileName):
    countOfWords = 0
    countOfSentences = 0

    text = TextHelper(fileName)

    #получения количества слов.
    buff = text.split()
    countOfWords = len(buff)
    countOfSentences = len(text.split('.')) - 1

    if countOfSentences == 0:
        return 0
    else:
        return countOfWords/countOfSentences

def AverageNumberOfWordsInASentenceToFile(fileName,ans):
    file = open(fileName, "a")

    file.write("Среднее количество слов в предложении = " + str(ans))
    file.write('\n')

    file.close()
    return

def TextHelper(fileName):
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

def MedianNumberOfWordsInSentence(fileName):
    text = TextHelper(fileName)
    if text == '':
        return -1

    listOfNumbersForEverySentence = []

    listOfSentences = text.split(".")
    listOfSentences.remove('')

    for sentense in listOfSentences:
        words = sentense.split()
        listOfNumbersForEverySentence.append(len(words))
    listOfNumbersForEverySentence.sort()

    medianAns = 0.
    medianPos = (len(listOfNumbersForEverySentence) + 1)/2
    if medianPos is not int:
        medianAns = (listOfNumbersForEverySentence[math.ceil(medianPos) - 1] + listOfNumbersForEverySentence[math.floor(medianPos) - 1]) /2
    else:
        medianAns = listOfNumbersForEverySentence[int(medianPos) - 1]

    #print(median(listOfNumbersForEverySentence))

    return medianAns

def MedianNumberOfWordsInSentenceToFile(fileName,ans):
    file = open(fileName,"a")

    file.write("Медианное количество слов в предложении = " + str(ans))
    file.write("\n\n")

    file.close()
    return

def HelpforTopfunc(fileName):
    text = TextHelper(fileName)
    text = text.lower()
    for item in stopSymbols2:
        text = text.replace(item,'',text.count(item))

    text = text.replace('...', '', text.count('...'))
    text = text.replace('-', '', text.count('-'))
    text = text.replace('(', '', text.count('('))
    text = text.replace(')', '', text.count(')'))
    text = text.replace('"', '', text.count('"'))
    text = text.replace("'", '', text.count("'"))
    text.replace("/", '', text.count('/'))
    return text

def GetKey(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key

def TopK(fileName,N=4,K=10):
    text = HelpforTopfunc(fileName)
    #text = text.replace(item,'',text.count(item)) for item in stopSymbols2  как это провернуть?
    ans = dict()

    listOfSentences = [sentence.split() for sentence in text.split(".")]
    for listOfWords in listOfSentences:
        for word in listOfWords:
            if len(word) >= N:
                for i in range(0,len(word) - N + 1):
                    if word[i: i + N] in ans:
                        ans[word[i: i + N]] += 1
                    else:
                        ans[word[i: i + N]] = 1
            else:
                continue

    return ans

def TopKToFile(ans,fileName,K=10):
    file = open(fileName, "a")

    sortedValues = sorted(ans.values())
    sortedValues.reverse()

    file.write(f"Топ {K}:" + "\n")
    for i in range(0, K):
        file.write(GetKey(ans, sortedValues[i]) + '-' + str(ans[GetKey(ans, sortedValues[i])])+"\n")
        ans.pop(GetKey(ans, sortedValues[i]))

    file.close()
    return


def main():
    RepeatOfEveryWordToFile("output.txt", RepeatOfEveryWord("text.txt")) # количество всех слов в тексте
    AverageNumberOfWordsInASentenceToFile("output.txt",AverageNumberOfWordsInASentence("text.txt"))
    MedianNumberOfWordsInSentenceToFile("output.txt",MedianNumberOfWordsInSentence("text.txt"))
    TopKToFile(TopK("text2.txt",3,6),"output.txt",6)

if __name__ == "__main__":
   main()
