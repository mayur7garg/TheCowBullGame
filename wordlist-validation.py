from pathlib import Path
wordlist_path = Path("./app/static/Wordlist.txt")

with wordlist_path.open('r') as word_list_file:
    word_list = list(map(lambda word: word[:4], word_list_file.readlines()))

print(f"There are currently {len(word_list)} words in the game.")

try:
    assert word_list == sorted(word_list), "The wordlist is not in order."
    print("The word list is in order.")
except Exception as e:
    print(e)
    for i, j in zip(word_list, sorted(word_list)):
        if i != j:
            print(i, j)

try:
    assert all([len(w) == 4 for w in word_list]), "All words are not 4 characters in length."
    print("All words are 4 characters in length.")
except Exception as e:
    print(e)
    for w in word_list:
        if len(w) != 4:
            print(w)

try:
    assert all([len(set(w)) == 4 for w in word_list]), "All words do not have 4 unique characters."
    print("All words have 4 unique characters.")
except Exception as e:
    print(e)
    for w in word_list:
        if len(set(w)) != 4:
            print(w)

try:
    assert all([w.upper() == w for w in word_list]), "All words are not in uppercase."
    print("All words are in uppercase.")
except Exception as e:
    print(e)
    for w in word_list:
        if w.upper() != w:
            print(w)