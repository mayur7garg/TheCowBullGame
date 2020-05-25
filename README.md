# The Cow Bull Game
*__A word guessing interactive Python based game written using the pygame module.__*

### How It Works-
1. The program chooses a _4-letter word_ and _your task is to guess it._
2. The key to remember is that _the word is meaningful_ and _all the 4 letters are distinct._
3. Enter an input and the program compares your input with the chosen word and gives you hints to narrow down your search.
4. __If the word you guessed has letter(s) common with the chosen word and its(theirs) position is identical, the program raises a flag - _Bull_. If their are letters common but with different positions, the program raises a flag - _Cow_.__
_Your goal is to get __4 Bulls__ i.e. guess the entire word accurately within __10 turns__._
5. You can use toe __Toggle Keys__ to toggle between __\*__, __?__ and __X__ that can be used to keep track of which alphabet is there in, which might be there and which is not there in the chosen word.

### Screenshots

__Welcome Screen__

![Welcome Screen](https://user-images.githubusercontent.com/26298346/29752197-5bb77cde-8b77-11e7-8a5e-6090fe9a3876.PNG)

__Game Screen 1__

![Game Screen 1](https://user-images.githubusercontent.com/26298346/29752198-5bc0585e-8b77-11e7-98d2-897b8211d47e.PNG)

__Game Screen 2__

![Game Screen 2](https://user-images.githubusercontent.com/26298346/29752199-5bc0b59c-8b77-11e7-9357-397bf88fc630.PNG)

__Game Screen 3__

![Game Screen 3](https://user-images.githubusercontent.com/26298346/29752201-5bc379a8-8b77-11e7-9e6e-41093a8e6e0d.PNG)

__Win Screen__

![Win Screen](https://user-images.githubusercontent.com/26298346/29752202-5bdfc2de-8b77-11e7-85b2-6770a7be095b.PNG)

__Lose Screen__

![Lose Screen](https://user-images.githubusercontent.com/26298346/29752200-5bc36260-8b77-11e7-8592-e6f7f99e6b14.PNG)

#### Key Features-
1. Interactive Interface
2. The word you hover your mouse on gets underlined to prevent misclicks.
3. The program make sure that you cannot enter a certain alphabet twice in the same input or a certain word again.
4. Your previous inputs are displayed with their results. You can use these results and the toggle keys to keep track of what alphabets might be there in the chosen word.
5. Erase button to update your input before submitting.
6. Scores to compare your performance.
7. Timer to compare how quickly you guessed the correct answer.

##### Requires _Pygame Module_ to run

> Developed by - _Mayur Garg_
