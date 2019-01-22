import pygame
import random




class Card:

    def __init__(self, content):
        self.content = content
        self.active = True
        self.selected = False
        self.pos = (0,0)

    def __str__(self):
        return str(self.content)

    __repr__ = __str__


def make_board():
    """Creates deck of paired cards with values assigned from options list and shuffles deck."""
    global cards

    for n in range(card_count//2):
        for i in range(2):
            cards.append(Card(options[0]))
        del options[0]

    random.shuffle(cards)
    
    return


def playing(deck):
    """Determines if any cards in the deck still need to be matched."""
    
    active = False

    #loops through all of the cards in a deck and if any are still active the 
    for card in deck:
        if card.active:
            active = True
            return active
    
    #prevent game from ending until last cards are compared
    if lock == False:
        active = True
        return active

    return active

def make_array():
    """Asigns every card its own position in a 5x4 grid pattern"""
    i = 1
    j = 0

    for card in cards:
        
        #first row 
        if j < 5: 
            card.pos = ((i * 110) - 25, 45)
        
        #second row 
        elif 5 <= j < 10:
            card.pos = (((i-5) * 110) - 25, 200)
        
        #third row
        elif 10 <= j < 15:
            card.pos = (((i-10) * 110) - 25, 355)
        
        #fourth row
        elif 15 <= j < 20:
            card.pos = (((i-15) * 110) - 25, 510)

        #adds the position of each card to a list
        card_cood.append(card.pos)

        j += 1
        i += 1
    
    return

def highlight_cards():
    """Blit purple overlay at the user's current card"""

    global card_location

    key = pygame.key.get_pressed()

    #try and except statement to protect against card_location being more or less than the number of cards
    try:
        window.blit(highlighted_card, card_cood[card_location])

    #if error occurs automatically return to first card
    except IndexError:
        card_location = 0
        window.blit(highlighted_card, card_cood[card_location])

    #move one card to right or if at rightmost card loop to next line
    if key[pygame.K_RIGHT]:
        card_location += 1

    #move one card to left or if at leftmost card loop to line above 
    if key[pygame.K_LEFT]:
        card_location -= 1

    return

    

def select_first_card():
    """Takes input from keys pressed to select first card"""

    global first_card
    global first_card_selected

    key = pygame.key.get_pressed()

    #set location the key is pressed to be the first card and tells card it has been selected
    if not first_card_selected:
        #makes sure already matched cards cannot be selected a second time
        if key[pygame.K_1] and cards[card_location].active == True:
            first_card = card_location
            cards[first_card].selected = True
            first_card_selected = True

    return

def select_second_card():
    """Takes input from keys pressed to select second card"""

    global second_card
    global second_card_selected
    
    key = pygame.key.get_pressed()
    
    #set location the key is pressed to be the second card and tells card it has been selected
    if not second_card_selected and first_card_selected:
        #makes sure already matched cards cannot be selected a second time and the second card cannot be the same as the first
        if key[pygame.K_2] and cards[card_location].active == True and card_location != first_card:
            second_card = card_location
            cards[second_card].selected = True
            second_card_selected = True 
   
    return

def flip_cards():
    """Displays selected cards' content to user and determines match"""

    global first_card_selected
    global second_card_selected
    global lock
    
    key = pygame.key.get_pressed()

    #when enter key is pressed and both cards have been selected, deselect them and show their content values
    if key[pygame.K_RETURN]:
       for card in cards:
            if first_card_selected and second_card_selected:
                cards[first_card].active = False
                cards[second_card].active = False
                cards[first_card].selected = False
                cards[second_card].selected = False 
                #lock turned off so that cards can now be compared
                lock = False

    #when space key is pressed and the lock is off
    if key[pygame.K_SPACE]:
        if lock == False:
            #if the cards don't match return them to active deck and resest selected variables
            if not cards[first_card].content == cards[second_card].content:
                cards[first_card].active = True
                cards[second_card].active = True
                first_card_selected = False
                second_card_selected = False
                lock = True
            #if the cards do match leave them in inactive deck and reset selected variables
            else:
                first_card_selected = False
                second_card_selected = False
                lock = True
        #if space key is pressed but lock is still on do nothing
        else:
            pass

    return

def display_board():
    """Blits card back or content depending on active status"""
   
    #fill window black to cover instructions
    window.fill((0, 0, 0))
   
    for card in cards:
        if card.active: 
            window.blit(cardImg, card.pos)
        else:
            window.blit(card.content, card.pos)
           
    return

def text_objects(text, font):
    """Creates text surface to display words on"""
    textSurface = font.render(text, True, (0,255,0))
    
    return textSurface, textSurface.get_rect()

def game_won(): 
    """Displays win image and gives option to restart"""
   
    global cards
   
    #win image
    window.blit(pygame.image.load('img_you_win.png'), (260,260))
    
    #explain how to restart game
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects('(press enter to replay)', largeText)
    TextRect.center = (350,475)
    window.blit(TextSurf, TextRect)
   
    key = pygame.key.get_pressed()

    #when enter key pressed shuffle board and restart
    if key[pygame.K_RETURN]:
        random.shuffle(cards)
        #assign cards their new positions
        make_array()
        for card in cards:
            card.active = True
    
    return


#set clock that game runs on
clock = pygame.time.Clock()

#saftey variable to make sure cards can't becompared before they are flipped
lock = True 

#set size of game window
window = pygame.display.set_mode((700,700))

#name the window the game pops up in
pygame.display.set_caption('Memory Match')

#image of the back of a playing card to be shown as default
cardImg = pygame.image.load('cardback.png')

#list of the front playing cards images to be used as content values
options = [pygame.image.load('2_of_hearts.png'), pygame.image.load('3_of_hearts.png'), pygame.image.load('4_of_hearts.png'), pygame.image.load('5_of_hearts.png'), pygame.image.load('6_of_hearts.png'), pygame.image.load('7_of_hearts.png'), pygame.image.load('8_of_hearts.png'), pygame.image.load('9_of_hearts.png'), pygame.image.load('10_of_hearts.png'), pygame.image.load('ace_of_hearts.png')]


first_card = -1
first_card_selected = False
second_card = -1
second_card_selected = False

card_count = 20

cards = []

card_cood = []

card_location = 0

done = False

show_instrustions = True

#purple overlay to indicate current location
highlighted_card = pygame.Surface((100, 142))
highlighted_card.set_alpha(192)
highlighted_card.fill((128,0,128))

#orange overlay to indicate selected cards
selected_card = pygame.Surface((100, 142))
selected_card.set_alpha(192)
selected_card.fill((255,215,0))

pygame.init()
make_board()
make_array()

while not done:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        done = True
    while playing(cards) and not done:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            done = True    
        
        key = pygame.key.get_pressed()

        #displays game instructions until the user hits the spacebar
        if show_instrustions:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                done = True 
            window.blit(pygame.image.load('updated_instructions.png'), (10,20))
            pygame.display.update()
            if key[pygame.K_SPACE]:
                show_instrustions = False
        
        else:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                done = True    

            display_board()
            
            select_first_card()

            select_second_card()
            
            #if a card is selected it blits the previously created selected_card overlay on top of it
            for card in cards:
                if card.selected == True:
                    window.blit(selected_card, card.pos)

            flip_cards()

            highlight_cards()

            #updates display as game gets input from user
            pygame.display.update()

            
            #set game to run at 10 frames per second so that graphics don't move too fast
            clock.tick(10)
   
    pygame.display.update()
    game_won()

