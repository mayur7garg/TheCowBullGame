from itertools import permutations

class Constants:
    ALPHA_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    TCBG_WordKey = "TCBG_WordID"
    TCBG_HistoryKey = "TCBG_History"

ALL_POSSIBLE_COMBS = ["".join(perm) for perm in permutations(Constants.ALPHA_CHARS, 4)]

def get_word_list(file_path: str):
    with open(file_path, 'r') as word_list_file:
        word_list = list(map(lambda word: word[:4], word_list_file.readlines()))
        
    return word_list