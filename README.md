# bigrams
Guesses which book a sentence belongs to based on its punctuation, by picking the model that gives the lowest perplexity for the sentence.

## Usage
```sh
python whichisit.py <novel 1> <novel 2>
```

## Example
```sh
python whichisit.py bible.txt warandpeace.txt
Paste a sentence from your favorite book: While the earth remaineth, seedtime and harvest, and cold and heat, and summer and winter, and day and night shall not cease.
This is probably from bible.
```
