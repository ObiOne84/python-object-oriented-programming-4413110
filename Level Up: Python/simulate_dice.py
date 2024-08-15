# monthe carlo simulation

from random import randint
from collections import Counter


def roll_dice(*dice, num_trials=1_000_000):
  counts = Counter()
  for _ in range(num_trials):
    counts[sum((randint(1, sides) for sides in dice))] += 1
  
  print('\nOUTCOME\tPROBABILITY')
  for outcome in range(len(dice), sum(dice) + 1):
    print(f'{outcome}\t{counts[outcome] * 100 / num_trials :0.2f}%')


roll_dice(6, 6, 6, 6)

notes = """
For my solution, I used the random module's randint function to simulate
dice rolls and a Counter from the collections module to keep track of how
often each outcome occurs. My roll_dice function on line four accepts a
variable number of arguments to represent the number of sides on the dice
and an optional named argument for the number of simulation trials to run,
which I give a default value of one million. Line five initializes a Counter
to keep track of outcomes and then the for loop on line six is where the magic
really happens. It simulates rolling dice for the number of trials. For each
simulation, I use the randint function to simulate rolling each of the dice
in the variable input parameter and then sum the individual outcomes together.
The resulting value serves as the index in the counts dictionary to increment
it by one. Finally, the code on lines 9 through 11 use a for loop to print out
how many times each possible outcomes occurred as a percentage. (screen whooshing)
Now, in the terminal, I've already started an interactive Python shell and imported
my roll_dice function. So I'll call it. And pass in 4, 6, 6 as arguments. This will
roll one four-sided die and two six-sided die. The output displays the simulated
probabilities for all possible outcomes from 3 to 16. Now, let's try adding a
fourth 20-sided die to that mix. And that gives us the probabilities for outcomes,
ranging from 4 to 36.
"""