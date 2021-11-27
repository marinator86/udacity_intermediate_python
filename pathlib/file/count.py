import collections
import operator

def count_unique_words(filename):
    # your code here
    result = collections.defaultdict(lambda: 1)
    with open(filename, "r") as f:
        t = f.read()
        for w in t.split():
            result[w] = result[w] + 1
    return sorted(result.items(), key = operator.itemgetter(1), reverse = True)

if __name__ == '__main__':
    print(*count_unique_words('file/hamlet.txt')[:10], sep="\n")