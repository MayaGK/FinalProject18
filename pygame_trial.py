import pygame
import random

pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((700,700))

pygame.display.set_caption('Memory Match')

cardImg = pygame.image.load('cardback.png')

options = [pygame.image.load('2_of_hearts.png'), pygame.image.load('3_of_hearts.png'), pygame.image.load('4_of_hearts.png'), pygame.image.load('5_of_hearts.png'), pygame.image.load('6_of_hearts.png'), pygame.image.load('7_of_hearts.png'), pygame.image.load('8_of_hearts.png'), pygame.image.load('9_of_hearts.png'), pygame.image.load('10_of_hearts.png'), pygame.image.load('ace_of_hearts.png')]

card_count = 20

card_cood = []

card_location = 0

selected_card = pygame.Surface((100, 142))
selected_card.set_alpha(192)
selected_card.fill((128,0,128))

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

    # i = 1
    # for card in cards:
    #     if card.active:
    #         window.blit(cardImg, (i * 45, 45))
    #     else:
    #         window.blit(card.content, (i * 45, 45))
    #     i += 1


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
            pos = ((i * 110) - 25, 45)

        elif 5 <= j < 10:
            pos = (((i-5) * 110) - 25, 200)
        
        elif 10 <= j < 15:
            pos = (((i-10) * 110) - 25, 355)
        
        elif 15 <= j < 20:
            pos = (((i-15) * 110) - 25, 510)

        card_cood.append(pos)

        j += 1
        i += 1

def select_cards():
    global card_location

    key = pygame.key.get_pressed()

    try:
        window.blit(selected_card, card_cood[card_location])

    except IndexError:
        card_location = 0
        window.blit(selected_card, card_cood[card_location])

    if key[pygame.K_RIGHT]:
        card_location += 1
    
    if key[pygame.K_LEFT]:
        card_location -= 1

def display_board():

    i = 1
    j = 0

    for card in cards:
        if j < 5:
            if card.active: 
                window.blit(cardImg, ((i * 110) - 25, 45))
            else:
                window.blit(card.content, ((i * 110) - 25, 45))
           
        elif 5 <= j < 10:
            if card.active:   
                window.blit(cardImg,(((i-5) * 110) - 25, 200))
            else:
                window.blit(card.content, (((i-5) * 110) - 25, 200))
        
        elif 10 <= j < 15:
            if card.active: 
                window.blit(cardImg,(((i-10) * 110) - 25, 355))
            else:
                window.blit(card.content, (((i-10) * 110) -25, 355))
        
        elif 15 <= j < 20:
            if card.active: 
                window.blit(cardImg,(((i-15) * 110) - 25, 510))
            else:
                window.blit(card.content, (((i-15) * 110) - 25, 510))

        j += 1
        i += 1
    return

done = False

make_board()
make_array()
while not done:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        
        display_board()
        select_cards()

        pygame.display.update()
        pygame.display.flip()
        clock.tick(10)
