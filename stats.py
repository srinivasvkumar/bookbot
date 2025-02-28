from collections import Counter


def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    are_count = words.count("are")
 #   print(f"{are_count} is the total count of litereal are")
 #   print(f"{num_words} words found in the document")


def get_char_count_counter(file_contents):
    word_cnt = Counter(file_contents.lower())
   # print(f"the final count is {word_cnt}")


def get_char_count(file_contents):
    final_chr = {}
    word = file_contents.lower()
    for chr in word:
        if chr in final_chr:
            final_chr[chr] += 1
        else:
            final_chr[chr] = 1
    return final_chr


def report(file_cnt, final_chr):
    sorted_dict = {}
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {len(file_cnt)} total words")
    print(f"--------- Character Count -------")
    sorted_dict = dict(sorted(final_chr.items(), key=lambda item: item[1]))
    print(sorted_dict)

    for key in sorted(final_chr, key=final_chr.get):
        sorted_dict[key] = final_chr[key]
    print(sorted_dict)

    print(f"============= END ===============")
