import random
card = random.randint(1, 13)
type_card = random.randint(1, 4)

if card == 1:
    card = Ace
elif card == 2:
    card = 2
elif card == 3:
    card = 3
elif card == 4:
    card = 4
elif card == 5:
    card = 5
elif card == 6:
    card = 6
elif card == 7:
    card = 7
elif card == 8:
    card = 8
elif card == 9:
    card = 9
elif card == 10:
    card = 10
elif card == 11:
    card = Jack
elif card == 12:
    card = Queen
elif card == 13:
    card = King

Ace = 'Ace'
Jack = 'Jack'
Queen = 'Queen'
King = 'King'
Clubs = 'Clubs'
Diamonds = 'Diamonds'
Hearts = 'Hearts'
Spades = 'Spades'

if type_card == 1:
    type_card = Clubs
elif type_card == 2:
    type_card = Diamonds
elif type_card == 3:
    type_card = Hearts
elif type_card == 4:
    type_card = Spades

print("The card you picked is the", card, "of", type_card)
