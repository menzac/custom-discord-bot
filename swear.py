# -*- coding: utf-8 -*-

def count_swear_words(text):
    count = 0
    with open("swear/cs", encoding="utf-8") as cs, \
         open("swear/en", encoding="utf-8") as en:
        swear_words = cs.read().strip().split("\n") + \
                      en.read().strip().split("\n")
    count = sum((text.count(word) for word in swear_words))
    return count

if __name__ == '__main__':
    print(count_swear_words("piča kunda pussy fuckyou"))
