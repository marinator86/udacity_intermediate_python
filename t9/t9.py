from collections import defaultdict

import helper
import itertools

# https://towardsdatascience.com/uploading-files-to-google-drive-directly-from-the-terminal-using-curl-2b89db28bb06

def parse_content(content):
    return {word: occ for word, occ in [line.split() for line in content.split("\n")]}

def make_tree(words):

    def sort(l, r, v, map):
        if r == '':
            map['$'+l] = v
            return
        if r[0] not in map.keys():
            map[r[0]] = {}
        sort(l + r[0], r[1:], v, map.get(r[0]))

    res = {}
    for word, occ in words.items():
        sort('', word, occ, res)
    return res

def predict(tree, numbers):

    def dig_in(map, result):
        for k, v in map.items():
            if "$" == k[0]:
                result.append((k[1:], v))
            else:
                dig_in(v, result)

    seq = [helper.keymap[r] for r in numbers]
    product = list(itertools.product(*seq))
    result = []
    for path in product:
        entrypoint = tree
        for elem in path:
            entrypoint = entrypoint.get(elem, {})
        if entrypoint != {}:
            dig_in(entrypoint ,result)
    return result


if __name__ == '__main__':
    content = helper.read_content(filename='ngrams-10k.txt')

    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    words = parse_content(content)

    # PART 2: Building a trie from a collection of words.
    tree = make_tree(words)

    while True:
        # PART 3: Predict words that could follow
        numbers = helper.ask_for_numbers()
        predictions = predict(tree, numbers)

        if not predictions:
            print('No words were found that match those numbers. :(')
        else:
            for prediction, frequency in predictions[:10]:
                print(prediction, frequency)

        response = input('Want to go again? [y/N] ')
        again = response and response[0] in ('y', 'Y')
        if not again:
            break
