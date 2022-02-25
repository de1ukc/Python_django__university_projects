from WorkingClass.WorkWithText import WorkWithText

def main():
    tool = WorkWithText()
    print("Введите путь к файлу")
    path = input()
    if path == '':
        path = "WorkingClass/text.txt"

    tool.RepeatOfEveryWordToConsole(tool.RepeatOfEveryWord(path))  # количество всех слов в тексте
    tool.AverageNumberOfWordsInASentenceToConsole(tool.AverageNumberOfWordsInASentence(path))
    tool.MedianNumberOfWordsInSentenceToConsole(tool.MedianNumberOfWordsInSentence(path))
    tool.TopKToConsole(tool.TopK(path, 3, 6), 6)

if __name__ == "__main__":
   main()
