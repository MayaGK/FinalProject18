
import random
options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

card_count = 16

class Card:

    def __init__(self, content):
        self.content = content
        self.active = True

    def __str__(self):
        return str(self.content)

    __repr__ = __str__

cards = []

for n in range(card_count//2):
    for i in range(2):
        cards.append(Card(options[0]))
    del options[0]

print(cards)
random.shuffle(cards)
print(cards)

for card in cards:
    if card.active:
        print('*', end=' ')
    else:
        print(card.content, end=' ')
print('')

cards[3].active = False

for card in cards:
    if card.active:
        print('*', end=' ')
    else:
        print(card.content, end=' ')
print('')