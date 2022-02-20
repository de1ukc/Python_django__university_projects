#функция будет возвращать словарь с количеством повторений каждого слова

stopSymbols = ('.',',','?','!',':',';')


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

def repeatOfEveryWordtoFile(fileName,dic):
    file = open(fileName,"w")
    words = dic

    for word in words:
        file.write(word + ":" + str(words[word]) + "\n")
    file.write("\n")

    file.close()
    return


if __name__ == "__main__":
   repeatOfEveryWordtoFile("output.txt",repeatOfEveryWord("text.txt"))
   #test()
