#for the exact number-in-a-row
import random
numberOfStreaks = 0
NoE=20000 # number of experiments
StrL=6 # streak's length
for experimentNumber in range(NoE):
    htlist = ""
# generates random sequence of 100 0's and 1's
    for el in range(100):
        htlist = htlist + str(random.randint(0, 1))
#check for presence of the exact pattern
    if htlist.count("1" + "0"*StrL + "1") or htlist.count("0" + "1" * StrL + "0") or htlist.startswith("0"*StrL+"1") \
    or htlist.startswith("1" * StrL + "0") or htlist.endswith("1" + "0" * StrL) or htlist.endswith("0" + "1" * StrL):
        numberOfStreaks += 1 # if any of the above streaks is present, note it by increasing the numberOfStreaks
    print(numberOfStreaks)
print("Chance of streak: %s%%" % (numberOfStreaks / NoE * 100))

