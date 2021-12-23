# markov.py
# Uses Markov chains to randomly generate text

import markovify
import random

with open("assets/corpus.txt") as f:
    text = f.read()

def get_sentence():
  num = random.randint(0, 1)

  # 50% chance to use either NewlineText or Text for variety
  if num == 0:
    text_model = markovify.NewlineText(text, state_size=2, well_formed=False)
  else:
    text_model = markovify.Text(text, state_size=2, well_formed=False)

  # Generate a random message between 100 and 300 characters long
  sentence = text_model.make_short_sentence(random.randint(100, 300), tries=10)
  return remove_non_ascii(sentence)

# Strip all non-ASCII characters
def remove_non_ascii(s):
    return "".join(c for c in s if ord(c)<128)