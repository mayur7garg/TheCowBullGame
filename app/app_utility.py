from typing import List

def parse_history(history: str):
    if (history is None) or (len(history) == 0):
        return 0, [], []
    else:
        if (len(history) + 2) % 4 != 0:
            raise ValueError("Invalid history key")
        else:
            tries = int(history[:2])
            history = history[2:]
            guesses = []
            results = []

            for i in range(tries):
                guesses.append(history[i * 8: (i * 8) + 4])
                results.append(history[(i * 8) + 4: (i + 1) * 8])
            
            return tries, guesses, _parse_results(results)

def create_history(tries: int, guesses: List[str], results: List[List[int]]):
    history = f"{tries:02}"

    results_str = _create_results(results)

    for i in range(tries):
        history += guesses[i]
        history += results_str[i]
    
    return history

def _parse_results(results: List[str]):
    parsed_results = []

    for result in results:
        parsed_results.append([int(result[0]), int(result[2])])
    
    return parsed_results

def _create_results(results: List[List[int]]):
    results_str = []

    for result in results:
        results_str.append(f"{result[0]}B{result[1]}C")
        
    return results_str

def get_guess_results(word: str, guess: str):
    results = [0, 0]
    
    for i in range(4):
        if guess[i] in word:
            if word.index(guess[i]) == i:
                results[0] += 1
            else:
                results[1] += 1
    
    return results

def print_possible_word_count(all_combs: list[str], guesses: list[str], results: list[list[int]], tries: int):
    possible_combs = all_combs.copy()

    for guess, result in zip(guesses, results):
        filtered_combs = []

        for comb in possible_combs:
            if get_guess_results(comb, guess) == result:
                filtered_combs.append(comb)
        
        possible_combs = filtered_combs

    print(f"{len(possible_combs)} words possible after {tries} tries.")

    if len(possible_combs) < 100:
        print(possible_combs)