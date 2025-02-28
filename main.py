from stats import get_num_words, get_char_count_counter, get_char_count, report
import sys


def get_book_text(filePath):
    file = open(filePath, encoding="utf8")
    file_contents = file.read()
    return file_contents

    # Defining main function


def main():
    filePath = sys.argv[1]  # r"/home/srinivas/bookbot/books/frankenstein.txt"
    file_cont = get_book_text(filePath)
    get_num_words(file_cont)
    get_char_count_counter(file_cont)
    char_cnt = get_char_count(file_cont)
    report(file_cont, char_cnt)


# Using the special variable
# __name__
main()
