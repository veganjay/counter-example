#!/usr/bin/env python3

from collections import Counter


def main():
    counter = Counter()

    with open('wordlist', 'r') as words_fp:
        for word in words_fp:
            counter.update(word.strip())

    for name, count in counter.most_common():
        print(f'{name}: {count}')


if __name__ == '__main__':
    main()
