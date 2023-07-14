import random
from dice import roll_dice
from community_chest_cards import cc_cards
from chance_cards import chance_card

cc = cc_cards
chance = chance_card

random.shuffle(cc)
random.shuffle(chance)

starting_amount = float(input('input starting amount (in thousands):\n'))*1000

one = starting_amount
two = starting_amount
three = starting_amount
four = starting_amount


def show_scores():
    print('player 1 score:',one,'\nplayer 2 score:', two,'\nplayer 3 score:',three,'\nplayer 4 score:',four,'\n')


def draw_cc(player):
    global cc
    card = cc.pop(0)
    cc.append(card)
    card_value = list(card.values())[0]

    try:
        print(card)
        card_value = float(card_value)
        player += card_value
    except:
        print(card)

    return player


def draw_chance(player):
    global chance
    card = chance.pop(0)
    chance.append(card)
    card_value = list(card.values())[0]

    try:
        card_value = float(card_value)
        print(card)
        player += card_value
    except:
        print(card)
    return player


while True:
    person = input('input player to receive / give money, r (roll), done, or graph:\n')
    if person == '1':
        amnt = input('input amount of money to move (in thousands), or type "cc" or "ch":\n')

        if amnt == 'cc':
            one = draw_cc(one)
            show_scores()
            continue

        elif amnt == 'ch':
            one = draw_chance(one)
            show_scores()
            continue

        try:
            q = float(amnt)*1000
            one += q
        except:
            print('not a valid numerical input\n')
            continue


    elif person == '2':
        amnt = input('input amount of money to move (in thousands):\n')

        if amnt == 'cc':
            two = draw_cc(two)
            show_scores()
            continue

        elif amnt == 'ch':
            two = draw_chance(two)
            show_scores()
            continue

        try :
            q = float(amnt) * 1000
            two += q
        except:
            print('not a valid numerical input\n')
            continue

    elif person == '3':
        amnt = input('input amount of money to move (in thousands):\n')

        if amnt == 'cc':
            three = draw_cc(three)
            show_scores()
            continue

        elif amnt == 'ch':
            three = draw_chance(three)
            show_scores()
            continue

        try :
            q = float(amnt) * 1000
            three += q
        except:
            print('not a valid numerical input\n')
            continue

    elif person == '4':
        amnt = input('input amount of money to move (in thousands):\n')

        if amnt == 'cc':
            four = draw_cc(four)
            show_scores()
            continue

        elif amnt == 'ch':
            four = draw_chance(four)
            show_scores()
            continue

        try :
            q = float(amnt) * 1000
            four += q
        except:
            print('not a valid numerical input\n')
            continue

    elif person == 'r':
        roll_dice()

    elif person == 'done':
        print('--- FINAL SCORES --- \nplayer 1:',one,'\nplayer 2:',two,'\nplayer 3:',three,'\nplayer 4:',four)
        break
    else:
        print('no valid player input found, type 1, 2, 3, 4, "r", or done\n')
        continue
    show_scores()






