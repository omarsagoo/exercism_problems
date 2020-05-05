def count_words(sentence):
    word_dict = dict()
    sentence = sentence.split()
    new_word = None

    for word in sentence:
        word = word.lower()
        
        if not word[0].isalnum():
            word = word.replace(word[0], "")
        if len(word) == 0:
            continue
        if not word[len(word) - 1].isalnum():
            word = word.replace(word[len(word) - 1],  "")
        for char in word:
            if not char.isalnum() and char != "'":
                word = word.replace(char, " ")
                new_word = word
        if new_word != None:
            for wrd in new_word.split():
                word_dict[wrd] = word_dict.get(wrd, 0) + 1
            new_word = None
            continue

        word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict

if __name__ == "__main__":
    print(count_words("hey,my_spacebar_is_broken"))