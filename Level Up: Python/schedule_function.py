import sched
import time


def schedule_function(even_time, function, *args):
  s = sched.scheduler(time.time, time.sleep)
  s.enterabs(even_time, 1, function, argument=args)
  print(f'{function.__name__}() scheduled for {time.asctime(time.localtime(even_time))}')
  s.run()


schedule_function(time.time() + 3, print, 'Howdy!')

# Notes to solution
notes = """
 All right, for my solution, I used two modules from the Python standard library.
 The sched module, which implements a general purpose event scheduler and the time module,
 to manipulate the time units, and delay function for the scheduler. My schedule function
 has three parameters named event time, function, which is the function to execute and args,
 which has the wild card or star operator, to accept a variable number of arguments. Within
 my function I instantiate a new scheduler object named s, and pass it the time modules,
 time and sleep functions. It will use those two functions to deal with the outside world
 and control when scheduled events execute. On line six, I use the schedulers enterabs
 function to schedule the event to execute at an absolute time. The first event time
 argument should be a numeric type that's compatible with the return value of the time
 function that I pass to the scheduler constructor on line five. The next argument
 configures the event to have a high priority by setting the priority to one.
 For the third argument, I pass in the function to execute at the specified time,
 and I also pass along any given arguments for that function to execute. The next line
 prints a message to let me know what function was scheduled and for when, using the name
 variable to get the function's name and using the local time and ASC time to format the event
 time into a useful string. Finally, I call the schedulers run function to run the scheduled
 events. Now down in the terminal, I've already started an interactive Python shell and
 imported the time module in my scheduling function. I'll call that function as schedule
 function, time dot time plus one to schedule the event for one second from now. I'll pass
 print as the function to execute and the message will be howdy. When I press enter, I get
 a message that the print function was scheduled and then one second later I get the howdy
 message. Since my function accepts a variable number of arguments, I can add a second string
 to pass to that print function. How are you? And when I run that, after one second, the print
 function executes saying, howdy, how are you? (video game bleeps) My solution is just one way
 to solve this challenge.
"""