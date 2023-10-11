import random
from pathlib import Path
from typing import Union, Optional

from fastapi import FastAPI, Request, Cookie, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .app_consts import Constants as consts
from .app_consts import get_word_list

from .app_utility import parse_history, create_history, get_guess_results

BASE_PATH = Path(__file__).parent.resolve()

app = FastAPI(title = 'The Cow Bull Game')
app.mount("/static", StaticFiles(directory = f"{BASE_PATH}/static"), name = "static")
templates = Jinja2Templates(directory=f"{BASE_PATH}/templates")

word_list = get_word_list(f'{BASE_PATH}/static/Wordlist.txt')

@app.get("/", response_class = HTMLResponse)
async def index(request: Request,
        TCBG_WordID: Optional[int] = Cookie(None),
        TCBG_History: Optional[str] = Cookie(None)):

    try:
        tries, guesses, results = parse_history(TCBG_History)
    except Exception as exc:
        tries, guesses, results = 0, [], []

    response_data_dict = {"request": request, "tries": tries, "guesses": guesses, "results": results}
    response = templates.TemplateResponse("index.html", response_data_dict)

    if (TCBG_WordID is None) or (TCBG_History is None):
        response.set_cookie(key = consts.TCBG_WordKey, value = random.randrange(len(word_list)))
        response.set_cookie(key = consts.TCBG_HistoryKey, value = create_history(tries, guesses, results))
    
    return response

@app.post("/", response_class = Union[HTMLResponse, RedirectResponse])
async def process_guess(request: Request, new_guess: str = Form(), 
        TCBG_WordID: Optional[int] = Cookie(None),
        TCBG_History: Optional[str] = Cookie(None)):

    
    try:
        tries, guesses, results = parse_history(TCBG_History)
    except Exception as exc:
        tries, guesses, results = 0, [], []

    new_guess = new_guess.strip().upper()
    word_to_guess = word_list[TCBG_WordID]
    response_data_dict = {"request": request}

    if len(new_guess) != 4:
        response_data_dict["error_msg"] = "Your guess must be a 4 letter word!"
    elif len(set(new_guess)) != 4:
        response_data_dict["error_msg"] = "All characters in your guessed word must be unique!"
    elif new_guess in guesses:
        response_data_dict["error_msg"] = "You have already guessed this word before!"
    elif tries < 10:
        tries += 1
        guesses.append(new_guess)
        results.append(get_guess_results(word_to_guess, new_guess))

    reset_game = False

    if new_guess == word_to_guess:
        response_data_dict["game_over_msg"] = f"You guessed it in {tries} attempts!"
        reset_game = True
    elif tries >= 10:
        response_data_dict["game_over_msg"] = "You lost as you exhausted all your attempts!"
        reset_game = True

    if reset_game:
        tries, guesses, results = 0, [], []
        response_data_dict["correct_word"] = word_to_guess

    response_data_dict["tries"] = tries
    response_data_dict["guesses"] = guesses
    response_data_dict["results"] = results
    
    response = templates.TemplateResponse("index.html", response_data_dict)

    if reset_game:
        response.set_cookie(key = consts.TCBG_WordKey, value = random.randrange(len(word_list)))

    response.set_cookie(key = consts.TCBG_HistoryKey, value = create_history(tries, guesses, results))
    return response

@app.get("/reset")
async def reset_sessionID():
    response = RedirectResponse("/")
    response.delete_cookie(key = consts.TCBG_WordKey)
    response.delete_cookie(key = consts.TCBG_HistoryKey)
    return response

@app.get("/how-to-play")
async def reset_sessionID(request: Request):
    response_data_dict = {"request": request}
    response = templates.TemplateResponse("how-to-play.html", response_data_dict)
    return response