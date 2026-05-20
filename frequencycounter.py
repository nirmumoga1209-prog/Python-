def count_word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print(count_word_frequency(text))
