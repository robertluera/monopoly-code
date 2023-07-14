import random


def roll_dice():
    dice_options = [1, 2, 3, 4, 5, 6]
    d1 = random.choice(dice_options)
    d2 = random.choice(dice_options)

    doubles = ''
    if d1 == d2:
        doubles = '   ---DOUBLES, ROLL AGAIN---'

    print(f'You rolled a {d1} and a {d2}, advance {d1+d2} spaces!{doubles}\n')
