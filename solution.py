from WorkingClass.WorkWithText import WorkWithText
def main():
    tool = WorkWithText()
    tool.RepeatOfEveryWordToFile("WorkingClass/output.txt", tool.RepeatOfEveryWord("WorkingClass/text.txt")) # количество всех слов в тексте
    tool.AverageNumberOfWordsInASentenceToFile("WorkingClass/output.txt",tool.AverageNumberOfWordsInASentence("WorkingClass/text.txt"))
    tool.MedianNumberOfWordsInSentenceToFile("WorkingClass/output.txt",tool.MedianNumberOfWordsInSentence("WorkingClass/text.txt"))
    tool.TopKToFile(tool.TopK("WorkingClass/text2.txt",3,6),"WorkingClass/output.txt",6)

if __name__ == "__main__":
   main()
