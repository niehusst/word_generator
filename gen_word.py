import sys
import json
import random

START = "<start>"
END = "<end>"

def gen_word(weights):
    word = []
    curr = START
    min_len = 3
    max_len = 20
    i = 0
    while curr != END and i < max_len:
        options = weights[curr]
        choice = random.random()
        running_weight = 0
        for char, weight in options.items():
            running_weight += weight
            if choice < running_weight:
                if char != END:
                    word.append(char)
                elif i < min_len and len(options) > 1:
                    # try again
                    continue
                curr = char
                break
        i += 1

    # probs not necessary
    if curr != END:
        word.append(curr)

    print(''.join(word))

def main(args):
    if len(args) < 2:
        print("Requires weights file path input.")
        exit(1)

    fname = args[1]
    with open(fname) as f:
        weights = json.loads(f.read())
        gen_word(weights)


if __name__ == "__main__":
    main(sys.argv)
