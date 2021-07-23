import sys
import fileinput
from pathlib import Path

def check_usage():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} /path/to/file')
        sys.exit(1)

def check_path():
    path = Path(sys.argv[1])
    if not path.is_file:
        print(f'{sys.argv[1]} is not a file, exiting')
        sys.exit(1)

def camel_to_snake(word: str) -> str:
    if word.isupper():
        return word

    new_word: str = ''
    for j in range(len(word)):
        letter = word[j]
        if j == 0:
            new_word += letter
            continue

        if letter.isupper():
            prev = word[j-1]
            if prev.isupper() or not prev.isalpha():
                new_word += letter
            else:
                new_word += '_' + letter.lower()
        else:
            new_word += letter

    return new_word

def update_file():
    for line in fileinput.input(sys.argv[1], inplace=True):
        words = line.split(' ')
        if len(words) == 0 or type(words[0]) is bytes:
            continue

        for i in range(len(words)):
            words[i] = camel_to_snake(words[i])

        print(" ".join(words).strip('\n\r'))

def main():
    check_usage()
    check_path()
    update_file()

if __name__ == "__main__":
    main()