#start in neutral
gear = 0
if gear == 0:
    print("Neutral")
else:
    print(gear)
#shifting up and down
while gear <= 5 and gear >= 0:
    knob = input()
    if knob == "up":
        gear = gear + 1
        print(gear)
    elif knob == "dn":
        gear = gear - 1
        if gear == -1:
            print("Reverse")
        if gear == 0:
            print("Neutral")
        if gear >= 1:
            print(gear)
    else:
        print(gear)
#not ending
    if gear == -1:
        gear = gear + 1
    if gear == 5:
        gear = gear - 1