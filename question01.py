def number_of_character(sen):
    print(len(sen))

def number_of_words(sen):
    print(len(sen.split()))

def number_of_vowels(sen):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in sen if char in vowels)
    print(count)