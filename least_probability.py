#for at least given number-in-a-row
import random
NoE=10000 # number of experiments
StrL=6 # streak's length
numberOfStreaks = 0
for experimentNumber in range(NoE):
    # Code that creates a list of 100 'heads' or 'tails' values.
    htlist = ""
    for el in range(100):
        htlist = htlist + str(random.randint(0, 1)) # generates random sequence of 100 0's and 1's
    c0=htlist.find("0"*StrL) # check if a streak of "0..0" is present in the sequence
    c1=htlist.find("1"*StrL) # check if a streak of "1..1" is present in the sequence

    if c0!=-1 or c1!=-1:
        numberOfStreaks += 1 # if any of the above streaks is present, note it by increasing the numberOfStreaks
    print(numberOfStreaks)


print("Chance of streak: %s%%" % (numberOfStreaks / NoE * 100))

