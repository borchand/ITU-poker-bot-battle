from test import run_benchmark, run_table

from example_bots import bluff_bot, chicken_bot, hardcore_ai_bot, knockout_bot, never_bluff_bot, random_bot, range_bot

import my_bot

bots = [ my_bot,
    bluff_bot, chicken_bot, hardcore_ai_bot, knockout_bot, never_bluff_bot, random_bot, range_bot
]  # Add your bot and bots you want to test against to this list

stacksize = 1000  # Change this variable for a different stack size. The stack size of the real game will be 1000.



#run_table(
 #   bots, stacksize
#)

# This runs 1 single tournament to the end, and outputs details to the console.
# This is a simulation of how the real game will be run.
# Check the output in the console and make sure your bot works as intended!

rounds = 100  # Change this variable for a different number of test runs

run_benchmark(bots, rounds, stacksize)  # This runs <rounds> tournaments and outputs win count for each bot.
