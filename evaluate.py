import glob
import random
from whichisit import main


def pick(x, y):
    book = x if random.randint(0, 1) == 0 else y
    with open(book, 'r') as f:
        text = f.read()
        return book, text[len(text) / 2 - random.randint(10, 30):len(text) / 2 + random.randint(10, 30)]

if __name__ == '__main__':
    books = glob.glob('books/*.TXT')
    random.shuffle(books)
    results = []
    for i, (a, b) in enumerate(zip(books, books[1:])):
        print '{}/{}'.format(i + 1, len(books) - 1)
        answer, sent = pick(a, b)
        guess = main(a, b, sent)
        # print guess, answer
        results.append((guess + 'TXT') == answer)
    print sum(results) / float(len(results))
