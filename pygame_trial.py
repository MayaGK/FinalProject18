import pygame
import random
import time

pygame.init()

clock = pygame.time.Clock()

S = 1 

window = pygame.display.set_mode((700,700))

pygame.display.set_caption('Memory Match')

cardImg = pygame.image.load('cardback.png')

options = [pygame.image.load('2_of_hearts.png'), pygame.image.load('3_of_hearts.png'), pygame.image.load('4_of_hearts.png'), pygame.image.load('5_of_hearts.png'), pygame.image.load('6_of_hearts.png'), pygame.image.load('7_of_hearts.png'), pygame.image.load('8_of_hearts.png'), pygame.image.load('9_of_hearts.png'), pygame.image.load('10_of_hearts.png'), pygame.image.load('ace_of_hearts.png')]

first_card = -1
first_card_selected = False
second_card = -1
second_card_selected = False

card_count = 20

card_cood = []

card_location = 0

highlighted_card = pygame.Surface((100, 142))
highlighted_card.set_alpha(192)
highlighted_card.fill((128,0,128))

selected_card = pygame.Surface((100, 142))
selected_card.set_alpha(192)
selected_card.fill((255,215,0))

class Card:

    def __init__(self, content):
        self.content = content
        self.active = True
        self.selected = False
        self.pos = (0,0)

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


def playing(deck):

    active = False

    for card in deck:
        if card.active:
            active = True
            return active
    return active



def make_array():

    i = 1
    j = 0

    for card in cards:
        if j < 5: 
            card.pos = ((i * 110) - 25, 45)

        elif 5 <= j < 10:
            card.pos = (((i-5) * 110) - 25, 200)
        
        elif 10 <= j < 15:
            card.pos = (((i-10) * 110) - 25, 355)
        
        elif 15 <= j < 20:
            card.pos = (((i-15) * 110) - 25, 510)

        card_cood.append(card.pos)

        j += 1
        i += 1

def highlight_cards():
    global card_location

    key = pygame.key.get_pressed()

    try:
        window.blit(highlighted_card, card_cood[card_location])

    except IndexError:
        card_location = 0
        window.blit(highlighted_card, card_cood[card_location])

    if key[pygame.K_RIGHT]:
        card_location += 1
    
    if key[pygame.K_LEFT]:
        card_location -= 1

def select_first_card():
    global first_card
    global second_card
    global first_card_selected
    global second_card_selected
    

    key = pygame.key.get_pressed()
    

    if not first_card_selected:
        if key[pygame.K_1] and cards[card_location].active == True:
            first_card = card_location
            cards[first_card].selected = True
            first_card_selected = True

    return

def select_second_card():
    global second_card
    global second_card_selected
    
    key = pygame.key.get_pressed()
            
    if not second_card_selected:
        if key[pygame.K_2] and cards[card_location].active == True and card_location != first_card:
            second_card = card_location
            cards[second_card].selected = True
            second_card_selected = True

   

def flip_cards():
    global first_card_selected
    global second_card_selected
    global S
    
    key = pygame.key.get_pressed()


    if key[pygame.K_RETURN]:
       for card in cards:
            if first_card_selected and second_card_selected:
                cards[first_card].active = False
                cards[second_card].active = False
                cards[first_card].selected = False
                cards[second_card].selected = False 
                S = 2


    if key[pygame.K_SPACE]:
        if S == 2:
            if not cards[first_card].content == cards[second_card].content:
                cards[first_card].active = True
                cards[second_card].active = True
                first_card_selected = False
                second_card_selected = False
                S = 1
            else:
                first_card_selected = False
                second_card_selected = False
                S = 1
        else:
            pass

    return

def display_board():
    window.fill((0, 0, 0))
    for card in cards:
        if card.active: 
            window.blit(cardImg, card.pos)
        else:
            window.blit(card.content, card.pos)
           
    return

def game_won(): 
    if all(card.active == False for card in cards):
     window.blit(pygame.image.load('img_you_win.png'), (260,260))

done = False

show_instrustions = True


make_board()
make_array()

while not done:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        
        key = pygame.key.get_pressed()

        if show_instrustions:
            window.blit(pygame.image.load('instructions.png'), (10,20))
            pygame.display.update()
            if key[pygame.K_SPACE]:
                show_instrustions = False
        else:
            display_board()
            
            
            select_first_card()

            
            select_second_card()
            
            for card in cards:
                if card.selected == True:
                    window.blit(selected_card, card.pos)

            flip_cards()



            highlight_cards()

            game_won()

            pygame.display.update()
            pygame.display.flip()
            clock.tick(10)

