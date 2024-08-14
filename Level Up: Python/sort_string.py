words = "apple ORANGE banana"

def sort_string(string):
  new_s = string.split()
  # bellow we append a copy of the word in lowercase to the fron of the word
  new_s = [w.lower() + w for w in new_s]
  new_s.sort()
  # here we remove the word that we appended, returning to the original state
  new_s = [w[len(w)//2:] for w in new_s]
  return ' '.join(new_s)


def sort_words(words):
  # in the single line, split the words into singular and sort ignoring letter case
  return ' '.join(sorted(words.split(), key=str.casefold))
print(sort_string(words))
print(sort_words(words))