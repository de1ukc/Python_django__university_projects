import math
from statistics import median
stopSymbols = ('.',',','?','!',':',';')

#функция будет возвращать словарь с количеством повторений каждого слова
def repeatOfEveryWord(fileName):
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
def repeatOfEveryWordToFile(fileName,dic):
    file = open(fileName,"w")
    words = dic

    for word in words:
        file.write(word + ":" + str(words[word]) + "\n")
    file.write("\n")

    file.close()
    return

def averageNumberOfWordsInASentence(fileName):
    countOfWords = 0
    countOfSentences = 0

    text = textHelper(fileName)

    #получения количества слов.
    buff = text.split()
    countOfWords = len(buff)
    countOfSentences = len(text.split('.')) - 1
    print(countOfWords)
    print(countOfSentences)

    if countOfSentences == 0:
        return 0
    else:
        return countOfWords/countOfSentences

def averageNumberOfWordsInASentenceToFile(fileName,ans):
    file = open(fileName, "a")

    file.write("Среднее количество слов в предложении = " + str(ans))
    file.write('\n')

    file.close()
    return

def textHelper(fileName):
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

def medianNumberOfWordsInSentence(fileName):
    text = textHelper(fileName)

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

def medianNumberOfWordsInSentenceToFile(fileName,ans):
    file = open(fileName,"a")

    file.write("Медианное количество слов в предложении = " + str(ans))
    file.write('\n')

    file.close()
    return

def main():
    repeatOfEveryWordToFile("output.txt", repeatOfEveryWord("text.txt")) # количество всех слов в тексте
    averageNumberOfWordsInASentenceToFile("output.txt",averageNumberOfWordsInASentence("text.txt"))
    medianNumberOfWordsInSentenceToFile("output.txt",medianNumberOfWordsInSentence("text.txt"))

if __name__ == "__main__":
   main()
