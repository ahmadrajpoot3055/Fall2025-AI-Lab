import random

low = 23
high = 25

temp = random.uniform(20, 30)
prev = None
ac = False
old = []

old.append(round(temp, 2))

if prev is None:
    change = "start"
else:
    if temp > prev:
        change = "up"
    elif temp < prev:
        change = "down"
    else:
        change = "same"

if temp > high and not ac:
    ac = True
    print(f"{prev if prev is not None else 'NA'} -> {temp:.2f} {change} | AC ON")
elif temp < low and ac:
    ac = False
    print(f"{prev if prev is not None else 'NA'} -> {temp:.2f} {change} | AC OFF")
else:
    print(f"{prev if prev is not None else 'NA'} -> {temp:.2f} {change} | AC {'ON' if ac else 'OFF'}")

prev = temp