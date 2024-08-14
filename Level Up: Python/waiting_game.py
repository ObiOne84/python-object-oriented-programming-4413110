import time
import random



def waiting_game():
  target = random.randint(2, 4)
  print(f"Your target time is {target} seconds.")
  print("Press Enter key to start.")
  input()
  start_time = time.time()
  # Could also use this one here
  # start = time.perf_counter()
  print("First Enter key pressed. Press Enter again to stop timing...")
  input()  # This pauses the program until Enter is pressed again
  end_time = time.time()
  # Calculate the elapsed time
  elapsed_time = end_time - start_time
  if elapsed_time > target:
    print(f"Too slow! Elapsed time: {elapsed_time:.2f} seconds")
  elif elapsed_time < target:
    print(f"Too fast! Elapsed time: {elapsed_time:.2f} seconds")
  else:
    print(f"Perfect! Elapsed time: {elapsed_time:.2f} seconds")

waiting_game()