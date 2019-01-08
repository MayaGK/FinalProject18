
import random
options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

first_card = 0
second_card = 0
selected = False
card_count = 16

class Card:

    def __init__(self, content):
        self.content = content
        self.active = True

    def __str__(self):
        return str(self.content)

    __repr__ = __str__

cards = []
def make_board():
    global cards

    for n in range(card_count//2):
        for i in range(2):
            cards.append(Card(options[0]))
        del options[0]

    random.shuffle(cards)

    for card in cards:
        if card.active:
            print('*', end=' ')
        else:
            print(card.content, end=' ')
    print('')

    return

def playing(deck):

    active = False

    for card in deck:
        if card.active:
            active = True
            return active
    return active

def guess_match():
   global first_card
   global second_card
   global selected

   while not selected:

       try:
           first_card = int(input("Select first card (input card number)"))

           if 0 < first_card < 15 and cards[first_card].active == True:
               selected = True
           elif first_card > 15 or first_card < 0:
               print("Please select a number from 0 to 15")
           elif cards[first_card].active == False:
               print('You already found the match for that card')
               selected = False

       except ValueError:
           print("Please input a number")

   selected = False

   while not selected:

       try:
           second_card = int(input("Select second card (input card number)"))

           if 0 < second_card < 15 and cards[second_card].active == True:
               selected = True
           elif second_card > 15 or second_card < 0:
               print("Please select a number from 0 to 15")
           elif cards[second_card].active == False:
               print('You already found the match for that card')
           if second_card == first_card:
               print('You can\'t choose the same first and second card!')
               selected = False


       except ValueError:
           print("Please input a number")

   selected = False

   cards[first_card].active = False
   cards[second_card].active = False

   return


def display_board():

    for card in cards:
        if card.active:
            print('*', end=' ')
        else:
            print(card.content, end=' ')
    print('')
    return

def compare_match():
    if cards[first_card].content == cards[second_card].content:
        print('Congrats! you found a match')
    else:
        print('Those cards do not match. Try again')
        cards[first_card].active = True
        cards[second_card].active = True
    return

def game_won():
    print('Congrats you wont the game')
    return

make_board()

while playing(cards):
    guess_match()
    display_board()
    compare_match()
    display_board()

game_won()