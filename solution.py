#функция будет возвращать словарь с количеством повторений каждого слова

stopSymbols = ('.',',','?','!',':',';')

def repeatOfEveryWord(fileName):
    ans = dict()

    file = open(fileName,'r')
    text = file.read()
    text.replace('т.к.','так как',text.count('т.к.'))
    text.replace('т.п.','тому подобное',text.count('т.п.'))

    text.lower() #всё к нижнему регистру
    text.lstrip() # удаляю пробелы в начале
    text.rstrip() # удаляю пробелы в конце
    listOfWords = text.split()


    for word in listOfWords:
        symb = word[len(word - 1)]
        if word[:3] == '...':
            word.replace('...','')
        for sign in stopSymbols:
            if (symb == sign) and (word not 'т.д.') and (word not 'т.п.'):





    print(text)




    return ans

def test():
    text = "abcd."

    print(text[len(text)-1])



if __name__ == "__main__":
    #repeatOfEveryWord("text.txt")
    test()