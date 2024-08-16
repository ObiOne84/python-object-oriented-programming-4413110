import os
import secrets


script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, '/workspace/python-object-oriented-programming-4413110/Level Up: Python/diceware.txt')


def generate_passphrase(num_words, wordlist_path=file_path):
  with open(wordlist_path, 'r', encoding='utf-8') as file:
    # read all the lines from the text document
    lines = file.readlines()[1:7776]
    # print(lines)
    # separates words and takes only word (not numbers) and create a list of words
    word_list = [line.split()[1] for line in lines]

  words = [secrets.choice(word_list) for i in range(num_words)]

  return '-'.join(words)

print(generate_passphrase(5))