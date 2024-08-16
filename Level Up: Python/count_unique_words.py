import os
import re
import collections


script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, '/workspace/python-object-oriented-programming-4413110/Level Up: Python/romeo_julliet.txt')


def count_words(path):
  with open(path, 'r', encoding='utf-8') as file:
    all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
    all_words = [word.upper() for word in all_words]
    print(f'\nTotal Words: {len(all_words)}')

    word_counts = collections.Counter(all_words)

    print('\nTop 20 Words:')

    for word in word_counts.most_common(20):
      print(f'{word[0]}\t{word[1]}')

count_words(file_path)

notes = """
From my solution, I used two Python modules, the regular expressions module
to extract the individual words from the text file, and the collections module
for its counter class, which is a dictionary subclass that provides a convenient
way to keep a tally of unique items. It's exactly what this challenge needed.
With my count words function, I open the input file using a context manager
online six and then use a regular expression to find all of the words within the text.
The search pattern looks for any sequence of one or more letters, numbers, hyphens and
or apostrophes. Online eight, I convert the list of words that it finds into all upper
case, and then print out the length of that list, which indicates the total number of
words that were found. I create a new counter from the collections module on line 11,
passing in my list of words as an argument, which populates the counter's dictionary
with the number of times each word occurs. Finally, in the last section of code, I use
the counter's most common method to retrieve a list of the 20 most common words along
with their count values to display. Now, down in the terminal, I've already started an
interactive Python shell, and imported my count words function. So I'll call it as count words,
and then pass Shakespeare.text as the input argument. This is a text file containing
the complete works of William Shakespeare, which I downloaded from Gutenberg.org. When
I execute that function, I can see that Shakespeare wrote over 900,000 words, and his
favorite word was "The." Not too surprising. This is just one way to solve this challenge.
If you took a different approach, I encourage you to share your strategy with others in
the comment section.
"""