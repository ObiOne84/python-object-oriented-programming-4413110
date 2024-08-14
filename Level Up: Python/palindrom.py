import re


def is_palindrom(word):
  # remove all special signs, spaces and characters
  clean_word = re.sub(r'[^a-zA-Z]', '', word).lower()
  
  # compare word without special signs to reversed word
  return clean_word == clean_word[::-1]


print(is_palindrom("Level"))