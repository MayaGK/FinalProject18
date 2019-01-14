import pygame
import random

pygame.init()

window = pygame.display.set_mode((700,700))

pygame.display.set_caption('Memory Match')

cardImg = pygame.image.load('cardback.png')

options = [pygame.image.load('2_of_hearts.png'), pygame.image.load('3_of_hearts.png'), pygame.image.load('4_of_hearts.png'), pygame.image.load('5_of_hearts.png'), pygame.image.load('6_of_hearts.png'), pygame.image.load('7_of_hearts.png'), pygame.image.load('8_of_hearts.png'), pygame.image.load('9_of_hearts.png'), pygame.image.load('10_of_hearts.png'), pygame.image.load('ace_of_hearts.png')]

card_count = 20

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

    i = 1
    for card in cards:
        if card.active:
            window.blit(cardImg, (i * 45, 45))
        else:
            window.blit(card.content, (i * 45, 45))
        i += 1


def playing(deck):

    active = False

    for card in deck:
        if card.active:
            active = True
            return active
    return active

done = False

def display_board():

    for card in cards:
        if card.active:
            window.blit(cardImg, (i * 45, 45))
        else:
            window.blit(card.content, (i * 45, 45))
    return

make_board()
while not done:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        
        # for card in cards:
        #     window.blit(cardImg, (i, 1))

        pygame.display.update()
        pygame.display.flip()
