# word_generator

Generate a statistically believable "word" from weights trained on input texts.

I plan to soon play a game called [Dialect](https://thornygames.com/pages/dialect) where I will be a robot developing a dialect with my community, which inspired me to write a little program to help generate potentially interesting words.
I'm not sure what they mean yet. But I'm sure figuring that out will be the fun part.

`May you beseacalle, my foft friends.`

## Usage

Download a text corpus to build weights from. An easy source would be project gutenburg txt files.

```
# download the iliad
curl https://www.gutenberg.org/cache/epub/51355/pg51355.txt > data/iliad.txt
```

Then build a weights file:
```
python build_weights.py data/iliad.txt
```

Lastly, use a generated weights file:
```
python gen_word.py weights/iliad.txt_weights.json
```
