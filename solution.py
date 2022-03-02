from WorkingClass.WorkWithText import WorkWithText
from WorkingClass.constants import stop_symbols
from WorkingClass.constants import stop_symbols2

def main():
    tool = WorkWithText()
    print("Введите путь к файлу")
    path = input()
    if path == '':
        path = "WorkingClass/text.txt"

    tool.repeat_of_every_word_to_console(tool.repeat_of_every_word(path))  # количество всех слов в тексте
    tool.average_number_of_words_in_a_sentence_to_console(tool.average_number_of_words_in_a_sentence(path))
    tool.median_number_of_words_in_sentence_to_console(tool.median_number_of_words_in_sentence(path))
    tool.top_k_to_console(tool.top_k(path, 3, 6), 6)


if __name__ == "__main__":
   main()
