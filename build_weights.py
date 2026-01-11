import sys
import os
import json

START = "<start>"
END = "<end>"

# { char : { char : <sum of occurences of char2 following char1> } }
chars = {}

def process_word(word):
    # strip punctuation from end
    word = word.strip().lower()
    word_end = len(word)-1
    while word_end > 0 and not word[word_end].isalpha():
        word_end -= 1
    word = word[:word_end+1]
    if not word:
        return

    prev = START
    i = 0
    while i < len(word):
        c = word[i]
        if not c:
            i+=1
            continue

        if prev not in chars:
            chars[prev] = {}
        if c not in chars[prev]:
            chars[prev][c] = 0
        chars[prev][c] += 1
        prev = c
        i+=1

    if prev not in chars:
        chars[prev] = {}
    if END not in chars[prev]:
        chars[prev][END] = 0
    chars[prev][END] += 1


def normalize_weights():
    """convert sums to percentage on scale of 1"""
    for weight_map in chars.values():
        total = sum(weight_map.values())
        for k in weight_map.keys():
            weight_map[k] = weight_map[k] / total

def main(args):
    if len(args) < 2:
        print("Requires text file path input to build weights from")
        exit(1)

    # read all file
    fname = args[1]
    with open(fname) as f:
        for line in f:
            words = line.split(" ")
            for word in words:
                if len(word) < 3:
                    # imo interesting words are longer than 2 chars
                    continue
                process_word(word)

    normalize_weights()

    out_name = f"weights/{os.path.basename(fname)}_weights.json"
    with open(out_name, 'w') as f:
        f.write(json.dumps(chars))

    print(f"wrote weights to path: {out_name}")

if __name__ == "__main__":
    main(sys.argv)
